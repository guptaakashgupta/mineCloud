import os
import GetDriveServiceInstance

from apiclient import errors
from apiclient.http import MediaFileUpload



def insertFile(drive_service,filename):
	"""Insert new file.
	
	Args:
	service: Drive API service instance.
	filename: Filename of the file to insert.
	Returns:
	Inserted file id if successful, None otherwise.
	"""
	title=os.path.basename(filename)
	media_body = MediaFileUpload(filename,mimetype='text/plain',resumable=True)
	body = {
	  'title': title,
	}
	try:
		file = drive_service.files().insert(body=body,media_body=media_body).execute()
		return file['id']
	except errors.HttpError,error:
		print 'An error occured: %s' % error
		return None

def updateFile(drive_service,file_id,filepath):
	try:
		# First retrieve the file from the API.
		file = drive_service.files().get(fileId=file_id).execute()

		# File's new metadata.
		file['title'] = os.path.basename(filepath)
		
		# File's new content.
		media_body = MediaFileUpload(filepath,resumable=True)
		
		# Send the request to the API.
		updated_file = drive_service.files().update(fileId=file_id,body=file,newRevision=False,media_body=media_body).execute()
		return updated_file
	except errors.HttpError, error:
		print 'An error occurred: %s' % error
		return None

	
def deleteFile(drive_service,file_id):
	"""Permanently delete a file, skipping the trash.
	
	Args:
	service: Drive API service instance.
	file_id: ID of the file to delete.
	"""
	try:
		drive_service.files().delete(fileId=file_id).execute()
	except errors.HttpError, error:
		print 'An error occurred: %s' % error
		
def insertProperty(drive_service,file_meta_dict,filepath):
	"""Insert new custom file property.
	
	Args:
	drive_service: Drive API service instance.
	visibility: 'PUBLIC' to make the property visible by all apps,
		or 'PRIVATE' to make it only available to the app that created it.
	Returns:
	Inserted custom file property if successful, None otherwise.
	"""
	body = {
	'key':'filepath',
	'value':filepath,
	'visibility':'PUBLIC'
	}
	list=file_meta_dict[filepath]
	file_id=list[0]
	#print(file_id)
	try:
		p = drive_service.properties().insert(fileId=file_id, body=body).execute()
		#print("yoyo")
		return p
	except errors.HttpError, error:
		print 'error occurred hoho: %s' % error
		return None

	
if __name__=="__main__":
	service=GetDriveServiceInstance.getInstance(1)
	#deleteFile(service,'0B7lmC0WYmBTZSWNkT2FNNER2b00')
	p1 = service.properties().get(fileId='0B7lmC0WYmBTZYnRwMmFOV0ZpUUk', propertyKey='filepath', visibility='PUBLIC').execute()
	print(p1['value'])
