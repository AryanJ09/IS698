import boto3
import json

client = boto3.client('lambda')

response = client.invoke(
    FunctionName='LogS3Uploads',  # Replace with your function name
    InvocationType='RequestResponse',
    Payload=json.dumps({
        "key1": "value1",
        "key2": "value2"
    }),
)

print(response['Payload'].read().decode())
