from house.constants import *
from house.http_client import *
from house.utils import *


def get_users():
    resp = requests.get(url=get_users_link, data=None, headers=get_headers())
    return resp


def post_users():
    body = {"roleId": 0, "title": "tester", "id": "sg"}
    body1 = default_dict_to_json(body)
    headers = get_headers()
    resp = requests.post(url=post_users_link, data=body1, headers=headers)
    return resp


def post_institution():
    body = {"fullName": "sdfsdf", "shortName": "strdfdfing", "address": "stridfdng", "website": "strindfdg",
            "typeId": 0}
    body1 = default_dict_to_json(body)
    headers = get_headers()
    resp = requests.post(url=post_institutions_link, data=body1, headers=headers)
    return resp


def put_institutions():
    body = {
        "eventPoolTypeId": 1,
        "isHoursRequired": "true",
        "isReflectionRequired": "true",
        "requiredHours": [
            {
                "yearGradeTypeId": 1,
                "requiredHours": 20
            },
            {
                "yearGradeTypeId": 2,
                "requiredHours": 20
            },
            {
                "yearGradeTypeId": 3,
                "requiredHours": 20
            },
            {
                "yearGradeTypeId": 4,
                "requiredHours": 20
            }
        ]
    }
    body1 = default_dict_to_json(body)
    headers = get_headers()
    resp = requests.put(url=put_institutions_link, data=body1, headers=headers)
    return resp


def get_institution():
    headers = get_headers()
    resp = requests.get(url=get_institutions_link, data=None, headers=headers)
    return resp


def put_institution_verify():
    body = {"verificationCode": "12345"}
    body1 = default_dict_to_json(body)
    headers = get_headers()
    resp = requests.put(url=put_institutions_verify_link, data=body1, headers=headers)
    return resp


def get_institution_schools():
    body = {"institutionName": "string11111111"}
    body1 = default_dict_to_json(body)
    headers = get_headers()
    resp = requests.get(url=get_institutions_schools_link, data=body1, headers=headers)
    return resp


def post_events():
    headers = get_headers()
    body = {
        "title": "High school",
        "institutionId": "38cf1fbc-f309-4a56-a1e7-a023653ba496",
        "categories": [
            1, 2, 3, 4, 5, 6, 7
        ],
        "eventSchedule": [
            {
                "startTime": "2019-07-05T19:23:00+05:00",
                "endTime": "2008-07-05T23:53:00+05:00"
            }
        ]
    }
    body1 = default_dict_to_json(body)
    resp = requests.post(url=post_events_link, data=body1, headers=headers)
    return resp


def post_auth1():
    body = {"email" : "dubina@mydigicode.com", "password" : "6PE40nf9"}
    body1 = default_dict_to_json(body)
    headers1 = get_headers1()
    resp = requests.post(url=post_auth, data=body1, headers=headers1)
    return resp


def get_refoobks1():
    headers1 = get_headers1()
    resp = requests.get(url=get_refbooks_link, data=None, headers=headers1)
    return resp

def post_login():
    body = {"email": "dubina@mydigicode.com", "password": "6PE40nf9"}
    body1 = default_dict_to_json(body)
    headers1 = get_headers1()
    resp = requests.post(url=login_link, data=body1, headers=headers1)
    return resp