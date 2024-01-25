from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import logging

log_file = 'script.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# specify path to key file
KEY_FILE_LOCATION = './column-user-config-443ad4ad8fab.json'

def create_user(service, email, first_name, last_name, password):
    # unique emails for testing purposes
    user_body = {
        "primaryEmail": email,
        "name": {
            "givenName": first_name,
            "familyName": last_name
        },
        "password": password,
        "changePasswordAtNextLogin": True
    }
    # create user
    try:
        user = service.users().insert(body=user_body).execute()
        print('User created: %s' % user['primaryEmail'])
        logging.info(f'User created: {user["primaryEmail"]}')
    except Exception as e:
        print('Error when creating: %s' % e)
        logging.error(f'Error when creating user {email}: {e}')

def process_parsed_data(filename, service):
    with open(filename, 'r') as file:
        next(file) # skips header
        for line in file:
            firstname, lastname, email, _= line.strip().split(',')
            create_user(service, email, firstname, lastname, 'JoinColumn2Pass')

# load the service account creds
credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE_LOCATION, scopes=['https://www.googleapis.com/auth/admin.directory.user'], subject='claytest@column30.com'
)

# building the service
service = build('admin', 'directory_v1', credentials=credentials)

# Process the data file
process_parsed_data('parsed_data.txt', service)