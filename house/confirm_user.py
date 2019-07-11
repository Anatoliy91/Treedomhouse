import boto3
from house.create_user import *

client = boto3.client('cognito-idp')
response = client.admin_confirm_sign_up(
    UserPoolId='us-east-2_fGnG7ZCyk',
    Username="testqwe@gmail.com"
)

print(response)