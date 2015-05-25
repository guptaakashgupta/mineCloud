import httplib2
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

FILENAME='temp'
parent_id='root'
storage_1 = Storage('a_credentials_file')
credentials_1 = storage_1.get()

http = httplib2.Http()
http = credentials_1.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Insert a file
#media_body = MediaFileUpload(FILENAME, mimetype='application/vnd.google-apps.folder', resumable=True)
body = {
  'title': 'Temp',
  'mimeType': 'application/vnd.google-apps.folder'
}
body['parents'] = [{'id': parent_id}]


file = drive_service.files().insert(body=body).execute()
print(file['id'])

