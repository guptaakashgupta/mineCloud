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

new_filename='CurrentUser.py'
file_id='0B7lmC0WYmBTZUU9ReGZBb0M5WmM'

# First retrieve the file from the API.
file = drive_service.files().get(fileId=file_id).execute()
# File's new metadata.
file['title'] = 'CurrentUser.py'

# File's new content.
media_body = MediaFileUpload(new_filename,resumable=True)

# Send the request to the API.
updated_file = drive_service.files().update(fileId=file_id,body=file,newRevision=False,media_body=media_body).execute()
print(updated_file['id'])
