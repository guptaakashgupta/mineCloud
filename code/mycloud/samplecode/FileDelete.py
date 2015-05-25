import httplib2
from apiclient import errors
from apiclient.http import MediaFileUpload
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

storage_1 = Storage('a_credentials_file')
credentials_1 = storage_1.get()

http = httplib2.Http()
http = credentials_1.authorize(http)

drive_service = build('drive', 'v2', http=http)
file_id='0B7lmC0WYmBTZdFVKS2hoblBpX2s'

try:
	drive_service.files().delete(fileId=file_id).execute()
except errors.HttpError, error:
	print 'An error occurred: %s' % error

