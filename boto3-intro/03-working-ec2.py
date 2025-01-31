import boto3

aws_console = boto3.session.Session(profile_name='default')
ec2 = aws_console.client('ec2')

print(ec2.describe_instances())

## Initialize the EC2 resource
response = ec2.run_instances(
    ImageId = "ami-05fa46471b02db0ce",
    InstanceType = "t2.micro",
    MinCount=1,
    MaxCount=1
)