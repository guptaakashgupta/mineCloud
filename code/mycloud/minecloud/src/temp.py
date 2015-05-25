import upload
import GetDriveServiceInstance

drive=GetDriveServiceInstance.getInstance(1)
upload.insertFile(drive,'../conf/1')
