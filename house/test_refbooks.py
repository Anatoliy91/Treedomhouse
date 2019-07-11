from house.api_client import *

def test_get_refbooks():
    resp = get_refoobks1()
    print(resp.text)
    print(resp.status_code)
    #assert message_error == 'SUCCESS'
    assert resp.status_code == 200

test_get_refbooks()