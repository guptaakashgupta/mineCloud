import json
import os
import upload
import GetDriveServiceInstance

def getFileMetadata(filename,filepath):
	DirectoryName='../db'
	FileName=filename
	file_meta_dict={}
	
	if os.path.exists(DirectoryName+"/"+FileName)==False:
		f=file(DirectoryName+"/"+FileName,'w')
		json.dump(file_meta_dict,f)
		f.close()
	if os.path.exists(DirectoryName+"/"+FileName):
		with open(DirectoryName+"/"+FileName,'r') as f:
			file_meta_dict = json.load(f)
			f.close()
		list=file_meta_dict.get(filepath)
	   	if list:
			return list
		else:
			return None


def storeFileMetaData(filename,filemetadata):
	DirectoryName='../db'
	FileName=filename
	file_meta_dict={}
	if os.path.exists(DirectoryName+"/"+FileName)==False:
		f=file(DirectoryName+"/"+FileName,'w')
		json.dump(file_meta_dict,f)
		f.close()
	if os.path.exists(DirectoryName+"/"+FileName):
		with open(DirectoryName+"/"+FileName,'r') as f:
			file_meta_dict = json.load(f)
			file_meta_dict.update(filemetadata)
			f.close()
		with open(DirectoryName+"/"+FileName,'w') as f:
			json.dump(file_meta_dict,f)
			f.close()

def updateFileMetaData(filename,filepath,list):
	DirectoryName='../db'
	FileName=filename
	file_meta_dict={}
	if os.path.exists(DirectoryName+"/"+FileName):
		with open(DirectoryName+"/"+FileName,'r') as f:
			file_meta_dict = json.load(f)
			file_meta_dict[filepath]=list
			f.close()
		with open(DirectoryName+"/"+FileName,'w') as f:
			json.dump(file_meta_dict,f)
			f.close()

def deleteFileMetaData(filename,filepathlist):
	DirectoryName='../db'
	FileName=filename
	file_meta_dict={}
	if os.path.exists(DirectoryName+"/"+FileName):
		with open(DirectoryName+"/"+FileName,'r') as f:
			file_meta_dict = json.load(f)
			f.close()
		keys=file_meta_dict.keys()
		for key in keys:
			num=filepathlist.count(key)
			if num==1:
				continue
			if num==0:
				drive_instance_number=file_meta_dict[key][2]
				drive_service=GetDriveServiceInstance.getInstance(drive_instance_number)
				file_id=file_meta_dict[key][0]
				upload.deleteFile(drive_service,file_id)
				del file_meta_dict[key]
		with open(DirectoryName+"/"+FileName,'w') as f:
			json.dump(file_meta_dict,f)
			f.close()
				
if __name__=="__main__":
	getFileMetadata('../document.txt')
