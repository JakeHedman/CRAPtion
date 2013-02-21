#coding: utf-8

import subprocess

def upload(local_file, filename, scpconf):
	cmd = [
			'scp',
			local_file,
			"%s@%s:%s/%s" % (
					scpconf['user'],
					scpconf['host'],
					scpconf['path'],
					filename	
				),
		]
	nullw = open('/dev/null', 'w')
	nullr = open('/dev/null')
	print " ".join(cmd)
#	subprocess.call(cmd)
	p = subprocess.Popen(cmd, stdout=nullw, stdin=nullr, stderr=nullw)
	p.wait()
	return scpconf['url'].replace('{f}', filename)
