import os

def getCredFileName():
	DirectoryName='../conf'
	count=0
	if os.path.exists(DirectoryName)==False:
		os.mkdir(DirectoryName)
	for file in os.listdir(DirectoryName):
		count=count+1
	#print(DirectoryName+'/'+str(count))
	return count+1

if __name__=="__main__":
	GetCredFileName()
		
