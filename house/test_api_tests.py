from house.constants import *
from house.http_client import *
from house.api_client import *
import requests

def test_get_request():
    resp = get_users()
    print(resp.text)
    print(resp.status_code)
    #assert message_error == 'SUCCESS'
    assert resp.status_code == 200

def test_post_request():
    resp = post_users()
    print(resp.text)
    print(resp.status_code)
    #assert message_error == 'SUCCESS'
    assert resp.status_code == 200


test_get_request()
test_post_request()
