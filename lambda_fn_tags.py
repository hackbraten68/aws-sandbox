import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    print(event)

    instanceId = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']

    user = event['detail']['userIdentity']['userName']

    ec2.create_tags(
        Resources=[
            instanceId
        ],
        Tags=[
            {
                'Key': 'Owner',
                'Value': user
            }
        ]
    )

    return