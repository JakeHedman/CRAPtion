#coding: utf-8
import datetime
import os
import random
import re
import string
import time

def mkfilename(fileconf):
	filename = fileconf['name']
	now = time.time()
	for match in re.finditer("{r(\d+)}", filename):
		chars = string.letters + string.digits
		filename = filename.replace(
				match.group(0),
				"".join([random.choice(chars) for _ in range(int(match.group(1)))]), 1
			)
	
	filename = filename.replace('{u}',	str(int(now)))
	filename = filename.replace('{d}', datetime.datetime.fromtimestamp(now).strftime(fileconf['datetime_format']))
	
	return filename + ".png"

def move(frm, todir, toname):
	todir = os.path.normpath(os.path.expanduser(todir))
	if not os.path.isdir(todir):
		os.makedirs(todir)
	path = "%s/%s" % (todir, toname)
	os.rename(frm, path)
	return path
