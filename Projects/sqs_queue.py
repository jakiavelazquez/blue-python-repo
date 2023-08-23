# Import the boto3 library, which provides an interface to interact with AWS services.
import boto3

# Create an SQS client using boto3.
sqs = boto3.client('sqs')

# Create an SQS queue with specified attributes.
response = sqs.create_queue(
    QueueName='shipping_queue',  # Name of the queue to be created
    Attributes={
        'DelaySeconds': '60',  # The delay before newly sent messages become visible (in seconds)
        'MessageRetentionPeriod': '86400'  # The time a message will be retained in the queue (in seconds)
    }
)

# Get the URL for the created SQS queue.
response = sqs.get_queue_url(QueueName='shipping_queue')

# Print the URL of the created SQS queue.
print(response['QueueUrl'])
