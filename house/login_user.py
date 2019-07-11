import boto3
from house.utils import *
from house.create_user import *

client = boto3.client('cognito-idp')
response = client.initiate_auth(
    #UserPoolId='us-east-2_fGnG7ZCyk',
    ClientId='30vvmsivo3l54mm4780ecgvvqg',
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': Username,
        'PASSWORD': Password,
}
)
print(response)

#text_data = default_json_to_dict(response)
#print(text_data)
# t = response["ChallengeParameters"]
# print(t)
#t2 = t["AuthenticationResult"]
#print(t2)