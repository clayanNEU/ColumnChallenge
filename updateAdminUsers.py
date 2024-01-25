from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import logging

log_file = 'script.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


# specify path to key file
KEY_FILE_LOCATION = './column-user-config-443ad4ad8fab.json'

# load the service account creds
credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE_LOCATION, scopes=['https://www.googleapis.com/auth/admin.directory.user'], subject='claytest@column30.com'
)

# building the service
service = build('admin', 'directory_v1', credentials=credentials)


def promote_to_super_admin(service, user_email):
    admin_body = {
        "status": True
    }

    # make admin
    try:
        service.users().makeAdmin(userKey=user_to_promote, body=admin_body).execute()
        print(f'{user_to_promote} has been promoted to super admin')
        logging.info(f'{user_to_promote} has been promoted to super admin')
    except Exception as e:
        print(f'Error is making this user a super admin: {e}')
        logging.error(f'Error is making this user a super admin: {e}')





# user email
user_to_promote = 'jjones@column30.com'

# call the Admin SDK Directory API
promote_to_super_admin(service, user_to_promote)