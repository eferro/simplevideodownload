#!/usr/bin/python
import tempfile
import os
import sys
import shutil
import subprocess



for url in sys.argv[1:]:
	print url
	tempdir = tempfile.mkdtemp(dir=os.getcwd())
	print tempdir
	os.chdir(tempdir)
	subprocess.call(["youtube-dl", url])

	initial_path = os.listdir('.')[0]
	subprocess.call(["rename", "s/ /_/g", initial_path])
	final_path = initial_path.replace(' ', '_')
	mp3_path = final_path + '.mp3'
	
	subprocess.call(["ffmpeg", "-i", final_path, mp3_path])
	print initial_path
	print final_path
	print mp3_path
	
	shutil.move(final_path, "../")
	shutil.move(mp3_path, "../")

	os.chdir('../')

	print "EFA1", os.listdir('.')
	print "EFA2", os.getcwd()
	shutil.rmtree(tempdir, ignore_errors=True)

    

    

