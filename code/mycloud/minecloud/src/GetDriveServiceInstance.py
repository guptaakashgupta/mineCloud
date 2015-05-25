import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage

def getInstance(number):
	DirectoryName='../conf'
	storage = Storage(DirectoryName+'/'+str(number))
	credentials = storage.get()
	
	http = httplib2.Http()
	http = credentials.authorize(http)
	
	drive_service = build('drive', 'v2', http=http)
	
	return drive_service

def getUser(filesize):
	return getInstance(1)

def getNumber(filesize):
	return 1
if __name__=="__main__":
	getInstance(1)
	
