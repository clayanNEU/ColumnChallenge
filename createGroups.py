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


def create_group(service, email, name, description):    
    group_body = {
        "email": email,
        "name": name,
        "description": description
    }
    # create group
    try:
        group = service.groups().insert(body=group_body).execute()
        print(f'Group created: {group["email"]}')
        logging.info(f'Group created: {group["email"]}')
    except Exception as e:
        print(f'Error in creating group: {e}')
        logging.error(f'Error in creating group: {e}')

def create_groups_for_departments(filename, service):
    departments = set()
    with open(filename, 'r') as file:
        next(file) # skips header
        for line in file:
            _, _, _, department = line.strip().split(',')
            departments.add(department.lower())

        for department in departments:
            group_email_and_name = f"{department}@column30.com".lower()
            create_group(service, group_email_and_name, group_email_and_name, f"This is the {department} group, welcome!")

create_groups_for_departments('parsed_data.txt', service)