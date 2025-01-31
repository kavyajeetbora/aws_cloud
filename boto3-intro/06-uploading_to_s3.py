import boto3

aws_console = boto3.session.Session(profile_name="default")
s3_client = aws_console.client("s3")

response = s3_client.upload_file(
    Filename = r"/home/kavyajeet/Dev/Cloud Computing/AWS boto3/data/co2_pcap_cons.csv",
    Bucket = 's3-bucket-xxyy7751',
    Key = "data/co2.csv"
)

print(response)