import GetDriveServiceInstance
import xattr

from apiclient.discovery import build
from apiclient.http import MediaFileUpload

FILENAME='../document.txt'
service=GetDriveServiceInstance.getInstance(1)
#xattr.setxattr("../document.txt","user.comment","samnk file")
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
  'title': 'document.txt',
  'description': 'A test document',
  'mimeType': 'text/plain',
}

file = service.files().insert(body=body, media_body=media_body).execute()
print(file['id'])

body = {
    'key': 'comment',
    'value': 'lmas asmncla',
    'visibility': 'PUBLIC'
  }
p = service.properties().insert(fileId=file['id'], body=body).execute() 
p1 = service.properties().get(fileId=file['id'], propertyKey='comment', visibility='PUBLIC').execute()
print(p1['value'])
