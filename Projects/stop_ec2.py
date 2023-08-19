# Import the boto3 library, which provides the Python interface to AWS services
import boto3

# Create a boto3 EC2 resource object to interact with EC2 instances
ec2 = boto3.resource('ec2')

# Filter and retrieve running instances with a specific tag (ENV: Development)
instances = ec2.instances.filter(
     Filters=[
         {'Name': 'instance-state-name', 'Values': ['running']},  # Filter by instance state (running)
         {'Name': 'tag:ENV', 'Values': ['Development']}  # Filter by tag "ENV" with value "Development"
     ]
)

# Iterate through each running instance and attempt to stop it
for instance in instances:
     try:
          instance.stop()  # Stop the instance
          print(f'{instance.id} is stopped')  # Print instance ID and status message
     except:
          print(f'There are no instances to be stopped')  # Print message if no instances match the filters
