import GetDriveServiceInstance
from apiclient import errors

def searchFile(drive_service,confFileName):
	"""search file belonging to a folder.
	
	Args:
	service: Drive API service instance.
	folder_id: ID of the folder to search files from.
	"""
	page_token = None
	while True:
		try:
			param = {}
			param['q']="title="+"'"+confFileName+"'"
			#print(param['q'])
			if page_token:
				param['pageToken'] = page_token
			children =drive_service.children().list(folderId='root', **param).execute()

			for child in children.get('items', []):
				return child['id']
			page_token = children.get('nextPageToken')
			if not page_token:
				break
		except errors.HttpError, error:
			print 'An error occurred: %s' % error
			break


def getFileInstance(drive_service,file_id):
	"""returns file instance.
	
	  Args:
	    service: Drive API service instance.
	    file_id: ID of the file to print metadata for.
	"""
	try:
		file = drive_service.files().get(fileId=file_id).execute()
		return file
	except errors.HttpError, error:
		print 'An error occurred: %s' % error
	
def downloadFile(drive_service,drive_file):
	"""Download a file's content.

  Args:
    service: Drive API service instance.
    drive_file: Drive File instance.

  Returns:
    File's content if successful, None otherwise.
	"""
	download_url = drive_file.get('downloadUrl')
	if download_url:
		resp, content = drive_service._http.request(download_url)
		if resp.status == 200:
			#print 'Status: %s' % resp
			return content
		else:
			print 'An error occurred: %s' % resp
			return None
	else:
		# The file doesn't have any content stored on Drive.
		return None

def retrieveAllFiles(drive_service):
	"""Retrieve a list of File resources.
	
	Args:
	service: Drive API service instance.
	Returns:
	List of File resources.
	"""
	result = []
	page_token = None
	while True:
		try:
			param = {}
			if page_token:
				param['pageToken'] = page_token
			children = drive_service.children().list(folderId='root', **param).execute()

			for child in children.get('items', []):
				result.append(child['id'])
			page_token = children.get('nextPageToken')
			if not page_token:
				break
		except errors.HttpError, error:
			print 'An error occurred: %s' % error
			break
	return result


def getProperty(drive_service,file_id,key,visibility):
	"""returns information about the specified custom property.
	
	Args:
	service: Drive API service instance.
	file_id: ID of the file to print property for.
	key: ID of the property to print.
	visibility: type of property ('PUBLIC' or 'PRIVATE').
	"""
	try:
		p = drive_service.properties().get(fileId=file_id, propertyKey=key, visibility=visibility).execute()
		if p['value']:
			return p['value']
		else:
			return None
	except errors.HttpError, error:
		print 'property not attached to file so no need to download' 


if __name__=="__main__":
	drive_service=GetDriveServiceInstance.getInstance(1)
	fileid=getProperty(drive_service,'0B7lmC0WYmBTZUEtaeWJOVDBIcmM','filepath','PUBLIC')
	print(fileid)
