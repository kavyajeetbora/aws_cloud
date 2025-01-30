import boto3

## Create a session using the default profile
aws_management_console = boto3.session.Session(profile_name='default')

## create a client for the IAM service
iam_console = aws_management_console.client('iam')

for user in iam_console.users.all():
    print(user.name)

