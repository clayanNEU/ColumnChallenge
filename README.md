# Instructions on Use

https://drive.google.com/file/d/1xpzUV5tIn1rbPaLsfeUTTKcGR_AUgKe0/view

1. Set up Google organization
    1. payments
    2. domain
    3. structure
2. Set up the local environment
    1. Bash - run an example to check bash works
    2. Python - ensure it is installed
3. Understand Service Accounts and scope for resources
    1. API Documentation
    2. https://console.cloud.google.com/ 
        1. Google Workspaces → Enable [Admin SDK API](https://console.cloud.google.com/workspace-api/apis/admin.googleapis.com/metrics?authuser=3&project=column-user-config&supportedpurview=project) → IAM & Admin - create service account → create and download keys to be used in script, copy client id
        2. https://admin.google.com/ → Security → Access and Data Control → API Controls → Domain-wide Delegation
        3. add new API client(client ID from service account) and scopes needed
4. Bash Script used as an entry point
    1. load CSV into the same folder
    2. run bash script to output parse_data.txt, python scripts will utilize this
    3. Check parse_data.txt is created
5. Python Scripts needed to access Google APIs
    1. [createUsers.py](http://createUsers.py) run to create users from data
    2. [updateAdminUsers.py](http://updateAdminUsers.py) run to update a user to super admin
    3. [createGroups.py](http://createGroups.py) run to create groups from data
        1. allow 1-2 minutes after group creation before adding users to groups
    4. [addUserToGroup.py](http://addUserToGroup.py) run to add created users to their respective groups
6. Logging and error handling
    1. script.log - all successful calls and errors logged here for debugging and auditing
    2. where useful, you will see print statements in the command line
