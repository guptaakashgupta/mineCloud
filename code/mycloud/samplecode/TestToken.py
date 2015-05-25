import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

FILENAME = 'document1.txt'
storage_1 = Storage('a_credentials_file')
credentials_1 = storage_1.get()

storage_2 = Storage('b_credentials_file')
credentials_2 = storage_2.get()

http = httplib2.Http()
http = credentials_1.authorize(http)

drive_service_1 = build('drive', 'v2', http=http)

http = httplib2.Http()
http = credentials_2.authorize(http)

drive_service_2 = build('drive', 'v2', http=http)

# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
  'title': 'Script',
  'description': 'A test document',
  'mimeType': 'text/plain'
}

file = drive_service_1.files().insert(body=body, media_body=media_body).execute()
#pprint.pprint(file)

# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
  'title': 'Script',
  'description': 'A test document',
  'mimeType': 'text/plain'
}

file = drive_service_2.files().insert(body=body, media_body=media_body).execute()
#pprint.pprint(file)

