#!/usr/bin/python
# -*- coding: utf-8 -*-

import tempfile
import os
import sys
import shutil
import subprocess
import datetime
import json
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--uid', action='store', type=int, help='User id for the downloaded files')
	parser.add_argument('--gid', action='store', type=int, help='Group id for the downloaded files')
	parser.add_argument('url', action='store', nargs='*', help='Url to download')
	args = parser.parse_args()
	
	for url in args.url:
		tempdir = tempfile.mkdtemp(dir=os.getcwd())
		os.chdir(tempdir)
		subprocess.call(["youtube-dl", url])

		initial_path = os.listdir('.')[0]
		subprocess.call(["rename", "s/ /_/g", initial_path])
		final_path = initial_path.replace(' ', '_')
		base_path = final_path[:final_path.rfind('.')]
		mp3_path = base_path + '.mp3'
		
		subprocess.call(["ffmpeg", "-i", final_path, mp3_path])

		date_str = datetime.datetime.today().strftime("%Y%m%d")
		data = {
			'date':date_str,
			'url': url,
			'final_path': final_path,
			'mp3_path': mp3_path,
		}

		dest_dir = '../' + date_str
		if not os.path.exists(dest_dir):
			os.makedirs(dest_dir)
			os.chown(dest_dir, args.uid or -1, args.gid or -1)

		shutil.move(final_path, dest_dir)
		shutil.move(mp3_path, dest_dir)
		json_file = dest_dir + '/' + base_path + '.json'
		with open(json_file, 'w') as f:
			f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
		
		for file_path in [json_file, final_path, mp3_path]:
			os.chown(dest_dir + '/' + file_path, args.uid or -1, args.gid or -1)

		os.chdir('../')
		shutil.rmtree(tempdir, ignore_errors=True)


if __name__ == '__main__':
	main()