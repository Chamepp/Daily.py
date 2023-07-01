import boto3

def provision_ec2_instance(instance_type, image_id, key_name, security_group, subnet_id):
    ec2_client = boto3.client('ec2')

    response = ec2_client.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group],
        SubnetId=subnet_id,
        MinCount=1,
        MaxCount=1
    )

    instance_id = response['Instances'][0]['InstanceId']
    return instance_id

# Example usage
instance_type = 't2.micro'
image_id = 'ami-12345678'  # Replace with the desired image ID
key_name = 'my-keypair'  # Replace with your key pair name
security_group = 'sg-12345678'  # Replace with your security group ID
subnet_id = 'subnet-12345678'  # Replace with your subnet ID

new_instance_id = provision_ec2_instance(instance_type, image_id, key_name, security_group, subnet_id)
print(f"New EC2 instance provisioned with Instance ID: {new_instance_id}")

