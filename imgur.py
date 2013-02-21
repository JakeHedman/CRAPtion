#coding: utf-8

import urllib
import urllib2
import base64
import json

def upload(path, key):
	img_data = base64.b64encode(open(path).read())
	params = {
			'key': key,
			'image': img_data
		}
	data = urllib.urlencode(params)

	url = 'http://api.imgur.com/2/upload.json'
	req = urllib2.Request(url, data)
	res = json.loads(urllib2.urlopen(req).read())["upload"]
	return res['links']['original']
