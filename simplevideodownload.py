#!/usr/bin/python
import tempfile
import os
import sys
import shutil
import subprocess

for url in sys.argv[1:]:
	print url
	tempdir = tempfile.mkdtemp()
	print tempdir
	os.chdir(tempdir)
	subprocess.call(["youtube-dl", url])

	for root, dirs, files in os.walk('./'):
		print root, dirs, files

	os.chdir('../')
	shutil.rmtree(tempdir, ignore_errors=True)

    

    

