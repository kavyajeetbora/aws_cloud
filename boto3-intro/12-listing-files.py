import boto3

client = boto3.client("s3")

response = client.list_objects_v2(
    Bucket = "s3-bucket-xxyy7751",
)

for key in response['Contents']:
    print(key)