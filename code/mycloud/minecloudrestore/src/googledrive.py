import sys
import os
import re

import GetDriveServiceInstance
import download
import TraverseFileSys
import FileMetaJson

def downloadFiles():
	downloadConfFiles()
	
	DirectoryName='../conf'
	FileName='FileMeta.json'
	file_meta_dict={}
	pattern=re.compile('^([0-9]|[1-9][0-9])$')
	
	for filepath in TraverseFileSys.index(DirectoryName):
		drive_instance_number=int(os.path.basename(filepath))
		#print(drive_instance_number)
		drive_service=GetDriveServiceInstance.getInstance(drive_instance_number)
		file_id_list=download.retrieveAllFiles(drive_service)
		
		for file_id in file_id_list:
			filepath=download.getProperty(drive_service,file_id,'filepath','Public')
			#print(filepath)
			if filepath==None:
				continue
			else:
				if os.path.exists(os.path.dirname(filepath))==False:
					os.makedirs(os.path.dirname(filepath))
				if re.search(pattern,os.path.basename(filepath)):
					continue
				drive_file=download.getFileInstance(drive_service,file_id)
				if drive_file:
					content=download.downloadFile(drive_service,drive_file)
					chunkf = file(filepath,'wb')
					chunkf.write(content)
					chunkf.close()
					
					modify_time=os.path.getmtime(filepath)
					file_meta_dict[filepath]=[file_id,modify_time,drive_instance_number]
					FileMetaJson.storeFileMetaData(FileName,file_meta_dict)
		
		
	
	print("system restored")				
					
									

def downloadConfFiles():
	DirectoryName='../conf'
	
	if os.path.exists(DirectoryName)==False:
		print("please run adduser.py once first to generate the conf files")
		sys.exit()
	
	confFileName=2
	
	while True:
		drive_service=GetDriveServiceInstance.getInstance(1)
		file_id=download.searchFile(drive_service,str(confFileName))
		
		if file_id:
			drive_file=download.getFileInstance(drive_service,file_id)
			if drive_file:
				content=download.downloadFile(drive_service,drive_file)
				chunkf = file(DirectoryName+'/'+str(confFileName), 'wb')
				chunkf.write(content)
				chunkf.close()
				confFileName=confFileName+1
			else:
				print("file instance not got")
		else:
			print("conf folder updated")
			break 


if __name__=="__main__":
	downloadFiles()
