import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

storage_1 = Storage('a_credentials_file')
credentials_1 = storage_1.get()

http = httplib2.Http()
http = credentials_1.authorize(http)

drive_service_1 = build('drive', 'v2', http=http)

about=drive_service_1.about().get().execute()
print(type(about))
print(about['name'])
print(about['quotaBytesUsed'])
print(about['quotaBytesTotal'])
print(about['quotaBytesUsedAggregate'])
print(about['rootFolderId'])
