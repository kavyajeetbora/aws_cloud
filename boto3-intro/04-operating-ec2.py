import boto3


aws_console = boto3.session.Session(profile_name='default')
ec2 = aws_console.client('ec2')

# print(ec2.describe_instances())

## Print the instance ids for all running ec2 instances
for instance in ec2.describe_instances()['Reservations']:
    print(instance['Instances'][0]['InstanceId'])
    
# ## Stop an instance
# response = ec2.stop_instances(
#     InstanceIds = ['i-067500745110f11ba']
# )

## Starting an instance

# response = ec2.start_instances(
#     InstanceIds = ['i-067500745110f11ba']
# )

## Terminating the ec2 instance

response = ec2.terminate_instances(
    InstanceIds = ['i-067500745110f11ba']
)

print(response)