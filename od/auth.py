import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
from onedrivesdk.helpers.resource_discovery import ResourceDiscoveryRequest

redirect_uri = 'http://localhost:8080'
client_id = "2cffd357-331f-4a5e-a460-df4f4b39bbf2"
client_secret = "muazSCTF033|tzyKKG87*?~"
discovery_uri = 'https://api.office.com/discovery/'
auth_server_url='https://login.microsoftonline.com/common/oauth2/authorize'
auth_token_url='https://login.microsoftonline.com/common/oauth2/token'

http = onedrivesdk.HttpProvider()
auth = onedrivesdk.AuthProvider(http,
                                client_id,
                                auth_server_url=auth_server_url,
                                auth_token_url=auth_token_url)
auth_url = auth.get_auth_url(redirect_uri)
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
auth.authenticate(code, redirect_uri, client_secret, resource=discovery_uri)
# If you have access to more than one service, you'll need to decide
# which ServiceInfo to use instead of just using the first one, as below.
service_info = ResourceDiscoveryRequest().get_service_info(auth.access_token)[0]
auth.redeem_refresh_token(service_info.service_resource_id)
client = onedrivesdk.OneDriveClient(service_info.service_resource_id + '/_api/v2.0/', auth, http)