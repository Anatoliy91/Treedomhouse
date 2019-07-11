from warrant import Cognito

u = Cognito('us-east-2_fGnG7ZCyk', '30vvmsivo3l54mm4780ecgvvqg')

u.add_base_attributes(email='you@you.com', some_random_attr='random value')

u.register('username', 'password')