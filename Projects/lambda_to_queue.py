# Import required libraries
import json                             # Import the json module for working with JSON data.
import boto3                            # Import the boto3 library for AWS service interaction.
from datetime import datetime           # Import the datetime class from the datetime module.

# Define the Lambda function handler. This is the entry point for the Lambda function.
def lambda_handler(event, context):
    
    # Get the current date and time
    date_time  = datetime.now()                # Get the current date and time.
   
    # Create an SQS (Simple Queue Service) client instance.
    sqs = boto3.client('sqs')

    # Send a message to an SQS queue.
    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/015620821371/shipping_queue",   # URL of the target SQS queue.
        MessageBody=("Message received on: " + str(date_time.strftime('%Y-%m-%d %H:%M:%S')))               # The message body containing the formatted time.
    )

    # Return a response from the Lambda function.
    return {
        'statusCode': 200,              # HTTP status code indicating success (200 OK).
        'body': json.dumps('Time to place another order!')  # A JSON-encoded message to be included in the response body.
    }
