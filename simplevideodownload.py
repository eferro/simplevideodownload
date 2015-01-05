#!/usr/bin/python
import tempfile
import os
import sys
import shutil
import subprocess
import datetime
import json



for url in sys.argv[1:]:
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

	shutil.move(final_path, "../")
	shutil.move(mp3_path, "../")



	os.chdir('../')
	
	with open(base_path + '.json', 'w') as f:
		f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
	
	shutil.rmtree(tempdir, ignore_errors=True)
