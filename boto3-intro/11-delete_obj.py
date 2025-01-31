import boto3

client = boto3.client("s3")

response = client.delete_object(
    Bucket = "s3-bucket-xxyy7751",
    Key = "co2.csv"
)

print(response)