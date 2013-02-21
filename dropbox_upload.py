#coding: utf-8
import dropbox

def upload(local_path, filename, dropconf):
	sess = dropbox.session.DropboxSession(
			dropconf['app']['key'],
			dropconf['app']['secret'],
			"app_folder"
		)
	sess.set_token(
			dropconf['token']['key'],
			dropconf['token']['secret']
		)
	client = dropbox.client.DropboxClient(sess)
	uploaded = client.put_file("/" + filename, open(local_path))
	return client.share(uploaded['path'])['url']
