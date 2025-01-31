import pandas as pd
import boto3
from io import BytesIO

'''

What is BytesIO in Python?
BytesIO is a memory buffer that acts like a file, allowing you to handle byte streams in memory instead of writing/reading from disk.

It is part of Python’s io module and is useful when working with binary data, such as files downloaded from S3.

🔥 Why Use BytesIO?
Acts like a file: You can read/write to it like a file, but it's in memory.
Avoids writing to disk: Keeps data in RAM, making it faster for temporary operations.
Works well with Pandas and S3: Since AWS S3 returns binary data, BytesIO helps convert it into a readable format.
'''

# Define S3 path
s3_client = boto3.client("s3")

response = s3_client.get_object(
    Bucket = "s3-bucket-xxyy7751",
    Key = 'data/co2.csv'
)

data = response['Body'].read()
# Read CSV directly into Pandas DataFrame
df = pd.read_csv(BytesIO(data))
print(df.head())
