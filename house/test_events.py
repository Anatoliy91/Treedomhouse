from house.api_client import *

def test_post_events():
    resp = post_events()
    print(resp.text)
    print(resp.status_code)
    assert resp.status_code == 200

test_post_events()