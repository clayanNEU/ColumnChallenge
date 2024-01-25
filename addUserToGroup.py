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
    KEY_FILE_LOCATION, scopes=['https://www.googleapis.com/auth/admin.directory.group'], subject='claytest@column30.com'
)

# building the service
service = build('admin', 'directory_v1', credentials=credentials)

# call the Admin SDK Directory API
print('Adding user to group')

def add_member_to_group(service, member_email, group_key):
    print(f"Adding {member_email} to {group_key}")
    logging.info(f"Attempting to add {member_email} to {group_key}")
    member_body = {
        "email": member_email,
        "role": "MEMBER" # we can change to 'MANAGER' or 'OWNER'
    }

    try:
        added_member = service.members().insert(groupKey=group_key, body=member_body).execute()
        print(f'Member {member_email} added to group: {group_key}')
        logging.info(f'Member {member_email} added to group: {group_key}')
    except Exception as e:
        print(f'Error in adding member to group: {e}')
        logging.error(f'Error in adding member to group: {e}')


def add_member_to_departments(filename, service):
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            _, _, email, department = line.strip().split(',')
            group_key = f"{department.lower()}@column30.com"
            add_member_to_group(service, email, group_key)

add_member_to_departments('parsed_data.txt', service)