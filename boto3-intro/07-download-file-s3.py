import boto3

aws_console = boto3.session.Session(profile_name = 'default')
s3_client = aws_console.client("s3")

response = s3_client.download_file(
    Bucket = 's3-bucket-xxyy7751',
    Key = "data/co2.csv",
    Filename = "./data/co2.csv"
)

print(response)