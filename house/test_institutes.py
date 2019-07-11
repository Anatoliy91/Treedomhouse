from house.api_client import *
from house.http_client import *


# def test_post_institution():
#     resp = post_institution()
#     print(resp.text)
#     print(resp.status_code)
#     #assert message_error == 'SUCCESS'
#     assert resp.status_code == 200

# def test_put_institutions():
#     resp = put_institutions()
#     print(resp.text)
#     print(resp.status_code)
#     #assert message_error == 'SUCCESS'
#     assert resp.status_code == 200


def test_get_institution():
    resp = get_institution()
    print(resp.text)
    print(resp.status_code)
    text_data = default_json_to_dict(resp.text)
    print(text_data)
    t = text_data["data"]
    print(t)
#    t2 = t["id"]
 #   print(t2)
    assert resp.status_code == 200



def test_put_institution_verify():
    resp = put_institution_verify()
    print(resp.text)
    print(resp.status_code)
    #assert message_error == 'SUCCESS'
    assert resp.status_code == 200


def test_get_institution_schools():
    resp = get_institution_schools()
    print(resp.text)
    print(resp.status_code)
    #assert message_error == 'SUCCESS'
    assert resp.status_code == 200


# test_post_institution()
# test_put_institutions()
test_get_institution()
test_put_institution_verify()
test_get_institution_schools()