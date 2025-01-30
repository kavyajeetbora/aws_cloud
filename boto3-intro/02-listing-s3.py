import boto3


aws_console = boto3.session.Session(profile_name="default")
s3 = aws_console.client("s3")
response = s3.list_buckets()

for bucket in response["Buckets"]:
    print(bucket)