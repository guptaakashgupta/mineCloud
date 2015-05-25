#!/usr/bin/python

import httplib2

from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

import GetCredFileName
def adduser():
	DirectoryName='../conf'
	# Copy your credentials from the console
	CLIENT_ID = '900594103395-77jt7nsij0nit8hp56co9eki60vbjptm.apps.googleusercontent.com'
	CLIENT_SECRET = 'WUKLFqWn9s-HYsLvqsaAJRrb'
	
	# Check https://developers.google.com/drive/scopes for all available scopes
	OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
	
	# Redirect URI for installed apps
	REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
	
	
	# Run through the OAuth flow and retrieve credentials
	flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
	authorize_url = flow.step1_get_authorize_url()
	print 'Go to the following link in your browser: ' + authorize_url
	code = raw_input('Enter verification code: ').strip()
	credentials = flow.step2_exchange(code)
	
	#Get Credential FileName
	CredFileName=str(GetCredFileName.getCredFileName())
	storage = Storage(DirectoryName+'/'+CredFileName)
	storage.put(credentials)

if __name__=="__main__":
	adduser()
