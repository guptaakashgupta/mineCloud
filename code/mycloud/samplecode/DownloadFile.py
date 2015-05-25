import GetDriveServiceInstance
import xattr

from apiclient.discovery import build
from apiclient.http import MediaFileUpload

service=GetDriveServiceInstance.getInstance(1)

drive_file = service.files().get(fileId='0B7lmC0WYmBTZbWVyNDAzdl9QSW8').execute()
download_url = drive_file.get('downloadUrl')
resp, content = service._http.request(download_url)
chunkf = file('document.txt', 'wb')
chunkf.write(content)
chunkf.close()
