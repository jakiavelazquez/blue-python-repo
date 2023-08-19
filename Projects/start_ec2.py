# Import the boto3 library, which provides the Python interface to AWS services
import boto3

# Create a boto3 EC2 resource object to interact with EC2 instances
ec2 = boto3.resource('ec2')

# Create EC2 instances for development environment
dev = ec2.create_instances(
    ImageId='ami-08a52ddb321b32a8c',  # ID of the Amazon Machine Image (AMI) to use
    InstanceType='t2.micro',  # Type of EC2 instance
    MaxCount=3,  # Number of instances to create
    MinCount=3,
    TagSpecifications=[
        {
            'ResourceType': 'instance',  # Type of AWS resource to tag
            'Tags': [
                {'Key': 'Name', 'Value': 'Development'},  # Set tags for identification
                {'Key': 'ENV', 'Value': 'Development'}
            ]
        }
    ]
)

# Create EC2 instances for production environment
prod = ec2.create_instances(
    ImageId='ami-08a52ddb321b32a8c',  # ID of the Amazon Machine Image (AMI) to use
    InstanceType='t2.micro',  # Type of EC2 instance
    MaxCount=1,  # Number of instances to create
    MinCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',  # Type of AWS resource to tag
            'Tags': [
                {'Key': 'Name', 'Value': 'Production'},  # Set tags for identification
                {'Key': 'ENV', 'Value': 'Production'}
            ]
        }
    ]
)
