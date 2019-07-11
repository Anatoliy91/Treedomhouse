import boto3

from house.utils import *

Username = get_random_email()
Password = get_random_password()

# Create user
client = boto3.client('cognito-idp')
response = client.sign_up(
    ClientId='30vvmsivo3l54mm4780ecgvvqg',
    Username=Username,
    Password=Password,
    UserAttributes=[
        {'Name': 'email',
         'Value': Username
         },
        {'Name': 'name',
         'Value': 'FirstName'
         },
        {
            'Name': 'family_name',
            'Value': 'draftUe1'
        },
        {
            'Name': 'custom:role_id',
            'Value': '2'
        }
        # {
        #     'Name': 'custom:role_id',
        #     'Value': '0'
        # }
    ]
)

# Confirm
client = boto3.client('cognito-idp')
response = client.admin_confirm_sign_up(
    UserPoolId='us-east-2_fGnG7ZCyk',
    Username=Username,
)

# Login
client = boto3.client('cognito-idp')
response = client.initiate_auth(
    ClientId='30vvmsivo3l54mm4780ecgvvqg',
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': Username,
        'PASSWORD': Password,
    }
)

# Getting token

t = response["AuthenticationResult"],
token = t["AccessToken"],
print(token)



# def get_token():
#     client = boto3.client('cognito-idp')
#     response = client.initiate_auth(ClientId='30vvmsivo3l54mm4780ecgvvqg', AuthFlow='USER_PASSWORD_AUTH',AuthParameters={  'USERNAME': Username,   'PASSWORD': Password,)
#     t = response["AuthenticationResult"],
#     token = t["AccessToken"],
#     print(token)
