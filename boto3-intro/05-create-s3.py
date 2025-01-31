import boto3

aws_console = boto3.session.Session(profile_name="default")
s3_client = aws_console.client('s3')

try:
    response = s3_client.create_bucket(
        ACL='private',
        Bucket='s3-bucket-xxyy5684',
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1',
        }
    )

    print(response)

except Exception as e:
    print(e)


'''
✅ Valid Bucket Name Rules
- Must be globally unique across all AWS accounts.
- Must be between 3 and 63 characters long.
- Only lowercase letters (a-z), numbers (0-9), dots (.), and hyphens (-) are allowed.
- Must not start or end with a hyphen (-) or dot (.).
- Must not be an IP address format (e.g., 192.168.1.1).
'''