import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

redirect_uri = 'http://localhost:8080/'
client_secret = 'muazSCTF033|tzyKKG87*?~'
client_id='2cffd357-331f-4a5e-a460-df4f4b39bbf2'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

client = onedrivesdk.get_default_client(
    client_id=client_id, scopes=scopes)

auth_url = client.auth_provider.get_auth_url(redirect_uri)

#this will block until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

client.auth_provider.authenticate(code, redirect_uri, client_secret)