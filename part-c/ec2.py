import boto3

ec2 = boto3.resource('ec2')

# Your values
subnet_id = 'subnet-00eb5c83dd1839619'
security_group_id = 'sg-0378e3586d69394e3'
key_name = 'my_key'

# Launch EC2 instance with public IP association
instance = ec2.create_instances(
    ImageId='ami-0953476d60561c955',  # Amazon Linux 2 AMI
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName=key_name,
    NetworkInterfaces=[
        {
            'SubnetId': subnet_id,
            'DeviceIndex': 0,
            'AssociatePublicIpAddress': True,
            'Groups': [security_group_id]
        }
    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'Boto3InstanceWithPublicIP'}]
        }
    ]
)

# Wait and display results
print("⏳ Waiting for instance to launch...")
instance[0].wait_until_running()
instance[0].reload()
print("✅ EC2 Instance Launched!")
print(f"🆔 Instance ID: {instance[0].id}")
print(f"🌐 Public IP Address: {instance[0].public_ip_address}")
