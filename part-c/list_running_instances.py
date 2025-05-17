import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

print("🟢 Running EC2 Instances:\n")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"ID: {instance['InstanceId']}")
        print(f"Type: {instance['InstanceType']}")
        print(f"State: {instance['State']['Name']}")
        print(f"Public IP: {instance.get('PublicIpAddress', 'None')}")
        print(f"Private IP: {instance.get('PrivateIpAddress', 'None')}")
        print(f"AZ: {instance['Placement']['AvailabilityZone']}")
        print("-" * 40)
