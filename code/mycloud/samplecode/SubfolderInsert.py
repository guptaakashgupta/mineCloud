import httplib2
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

FILENAME='./temp/temp1/document1.txt'
parent_id='0B7lmC0WYmBTZV295bG1HLVhkSTQ'
storage_1 = Storage('a_credentials_file')
credentials_1 = storage_1.get()

http = httplib2.Http()
http = credentials_1.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Insert a file
#media_body = MediaFileUpload(FILENAME, mimetype='application/vnd.google-apps.folder', resumable=True)
body = {
  'title': 'temp1',
  'mimeType': 'application/vnd.google-apps.folder'
}
body['parents'] = [{'id': parent_id}]

file = drive_service.files().insert(body=body).execute()
print(file['id'])

media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
  'title': 'document1.txt',
  'description': 'A test document',
  'mimeType': 'text/plain'
}
body['parents'] = [{'id': file['id']}]

file1 = drive_service.files().insert(body=body, media_body=media_body).execute()
print(file1['id'])

