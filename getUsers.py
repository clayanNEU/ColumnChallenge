from google.oauth2 import service_account
from googleapiclient.discovery import build

# specify path to key file
KEY_FILE_LOCATION = './column-user-config-443ad4ad8fab.json'

# GSuite domain
GSUITE_DOMAIN = 'column30.com'

# load the service account creds
credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE_LOCATION, scopes=['https://www.googleapis.com/auth/admin.directory.user'], subject='claytest@column30.com'
)

# building the service
service = build('admin', 'directory_v1', credentials=credentials)

# call the Admin SDK Directory API
print('Getting the first 10 users in the domain')
results = service.users().list(domain=GSUITE_DOMAIN, maxResults=10, orderBy='email').execute()
users = results.get('users', [])

if not users:
    print('No users found.')
else:
    print('Users:')
    for user in users:
        # access the JSON object and return
        print(f'{user["primaryEmail"]} ({user["name"]["fullName"]}) ({user["id"]})')