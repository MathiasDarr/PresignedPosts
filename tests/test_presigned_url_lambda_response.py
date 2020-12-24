"""


"""
import logging
import boto3
from botocore.exceptions import ClientError
import requests


# user = 'dakobedbard'
# BUCKET = 'dakobed-sqs-transform-bucket'
# key = '{}/{}'.format(user, fileName)


# presigned_post_url = response_body['url']
# access_key = response_body['fields']['AWSAccessKeyId']
# policy = response_body['fields']['policy']
# signature = response_body['fields']['signature']


url = 'https://cr5nlv4c58.execute-api.us-west-2.amazonaws.com/Prod/signedURL'

def create_presigned_post(bucket_name, object_name, fields=None, conditions=None, expiration=3600):
    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3', region_name='us-east-1')
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL and required fields
    return response



def test_upload_file_with_presigned_url_received_from_lambda():
    """
    This function uses the presigned url returned and uploads to s3.
    :return: requests.response
    """
    fileName = 'small.jpg'
    userID = "dakobedbard@gmail.com"

    body = {"filename": fileName, "userID": userID}
    lambda_presigned_post = requests.post(url, json=body)

    assert lambda_presigned_post.status_code == 200

    response_body = lambda_presigned_post.json()['presigned']
    fields = response_body['fields']
    response = {'url': response_body['url'], 'fields': fields}

    with open(fileName, 'rb') as f:
        files = {'file': (fileName, f)}
        http_response = requests.post(response['url'], data=response['fields'], files=files)

    assert http_response.status_code == 204

fileName = 'small.jpg'
user = 'dakobedbard'
BUCKET = 'dakobed-sqs-transform-bucket'
key = '{}/{}'.format(user, fileName)

s3 = boto3.resource('s3')
s3.Object(BUCKET, key).delete()

#response = create_presigned_post(BUCKET, key)
test_upload_file_with_presigned_url_received_from_lambda()

# response['fields']['bucket'] = 'dakobed-sqs-transform-bucket'
#
# with open(fileName, 'rb') as f:
#     files = {'file': (fileName, f)}
#     http_response = requests.post(response['url'], data=response['fields'], files=files)
#     print(http_response)
