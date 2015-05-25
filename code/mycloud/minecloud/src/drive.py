import GetDriveServiceInstance
import TraverseFileSys
import FileMetaJson
import upload

import os

def uploadFiles():
	uploadConfFiles()
	DirectoryName='..'
	FileName='FileMeta.json'
	file_meta_dict={}
	for filepath in TraverseFileSys.index(DirectoryName):
		#print(filepath)
		if os.path.isfile(filepath):
			list=FileMetaJson.getFileMetadata(FileName,filepath)
			#print(list)
			modify_time=os.path.getmtime(filepath)
			if list==None:
				filesize=os.path.getsize(filepath)
				drive_service=GetDriveServiceInstance.getUser(filesize)
				drive_instance_number=GetDriveServiceInstance.getNumber(filesize)
				file_id=upload.insertFile(drive_service,filepath)
				#print(file_id)
				file_meta_dict[filepath]=[file_id,modify_time,drive_instance_number]
				#print(file_meta_dict)
				success=upload.insertProperty(drive_service,file_meta_dict,filepath)
				FileMetaJson.storeFileMetaData(FileName,file_meta_dict)
			if list:
				#print(list)
				if list[1]!=modify_time:
					updateFile(FileName,filepath,list,modify_time)		 
		if os.path.isdir(filepath) and not os.path.islink(filepath):
			#print(filepath)
			continue
			

def updateFile(filename,filepath,list,modify_time):
	FileName=filename
	number=len(list)-1
	drive_service=GetDriveServiceInstance.getInstance(list[number])
	file_id=list[0]
	updated_file=upload.updateFile(drive_service,file_id,filepath)
	list[1]=modify_time
	FileMetaJson.updateFileMetaData(FileName,filepath,list)

def delete():
	DirectoryName='..'
	FileName='FileMeta.json'
	list=[]
	for filepath in TraverseFileSys.index(DirectoryName):
		if os.path.isfile(filepath):
			list.append(filepath)
	
	FileMetaJson.deleteFileMetaData(FileName,list)
			
def uploadConfFiles():
	DirectoryName='../conf'
	FileName='Conf.Json'
	file_meta_dict={}
	for filepath in TraverseFileSys.index(DirectoryName):
		#print(filepath)
		if os.path.isfile(filepath):
			list=FileMetaJson.getFileMetadata(FileName,filepath)
			modify_time=os.path.getmtime(filepath)
			if list==None:
				drive_service=GetDriveServiceInstance.getInstance(1)
				file_id=upload.insertFile(drive_service,filepath)
				file_meta_dict[filepath]=[file_id,modify_time,1]
				#print(file_meta_dict)
				success=upload.insertProperty(drive_service,file_meta_dict,filepath)
				FileMetaJson.storeFileMetaData(FileName,file_meta_dict)
			if list:
				#print(list)
				if list[1]!=modify_time:
					updateFile(FileName,filepath,list,modify_time)		 
		if os.path.isdir(filepath) and not os.path.islink(filepath):
			#print(filepath)
			continue

if __name__=="__main__":
	uploadFiles()
