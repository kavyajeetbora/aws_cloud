import boto3

## Create a session using the default profile
aws_management_console = boto3.session.Session(profile_name='default')

## create a client for the IAM service
iam_console_client = aws_management_console.client('iam')
iam_console_resource = aws_management_console.resource('iam')

## Listing the user names from IAM using the client and resource
for user in iam_console_resource.users.all():
    print(user.user_name)

for user in iam_console_client.list_users()['Users']:
    print(user['UserName'])

'''
Resource is high level api, only is availabe for some services
Whereas client is low level api, available for all services
but needs more programming effort
'''

## Resource vs client 
resources = aws_management_console.get_available_resources()
print(resources)
