import requests, os
import json

# variables - read from shell
aad_tenant_id = os.environ["AAD_TENANT_ID"]
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
m365_tenant_name = os.environ["M365_TENANT_NAME"]
shp_site_name = os.environ["SHP_SITE_NAME"]

# do a login on AAD
request_url = "https://login.microsoftonline.com/" + aad_tenant_id + "/oauth2/v2.0/token"
r = requests.post(url = request_url,
                  headers = {'Content-Type': 'application/x-www-form-urlencoded'},
                  data = {'grant_type': 'client_credentials',
                        'client_id': client_id,
                        'client_secret': client_secret,
                        'scope': 'https://graph.microsoft.com/.default'}
                )
#print(json.dumps(r.json(), indent=4, sort_keys=True))
access_token = r.json()['access_token']

# prepare default headers to use for auth
HEADERS = {'Authorization': 'Bearer ' + access_token}

# get site_id from our website name
request_url = "https://graph.microsoft.com/v1.0/sites/" + m365_tenant_name + ".sharepoint.com:/sites/" + shp_site_name
r = requests.get(url = request_url, headers = HEADERS)
site_id = r.json()['id']
print("site_id: " + site_id)

# get drive_id from our site_id
request_url = "https://graph.microsoft.com/v1.0/sites/" + site_id + "/drive"
r = requests.get(url = request_url, headers = HEADERS)
drive_id = r.json()['id']
print("drive_id: " + drive_id)

# upload a binary test file on our sharepoint drive and get its url
filename = "dummy.pdf"
pdf_file = open(filename, "rb")
request_url = "https://graph.microsoft.com/v1.0/drives/" + drive_id + "/items/root:/" + filename + ":/content";
r = requests.put(url = request_url, headers = HEADERS, data = pdf_file.read())
pdf_file.close()
file_url = r.json()['webUrl']
print("file_url: " + file_url)
