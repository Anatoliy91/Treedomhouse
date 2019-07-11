from house.api_client import *

def test_login():
    resp = post_login()
    print(resp.text)
    print(resp.status_code)
    assert resp.status_code == 200

test_login()