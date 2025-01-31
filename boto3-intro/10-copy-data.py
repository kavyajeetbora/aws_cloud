import boto3

s3 = boto3.resource('s3')

copy_source = {
    'Bucket': "s3-bucket-xxyy7751",
    'Key': 'data/co2.csv'
}

bucket = s3.Bucket('s3-bucket-xxyy5684')
bucket.copy(copy_source, "data/data.csv")