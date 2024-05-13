import requests
import json
import jsonpath
import random

# base Url
baseUrl = "https://reqres.in/"

def test_successful_registration() :
    path = "api/register"
    request_json=json.loads('{"email": "eve.holt@reqres.in","password": "'+randomDigits(6)+'"}')
    # Make POST request with Json Input body
    response = requests.post(url=baseUrl+path, json=request_json)
    # Parse Response to Json Format
    response_json = json.loads(response.text)
    assert response.status_code == 200
    assert type(jsonpath.jsonpath(response_json, '$.token')[0]) == str

def test_unsuccessful_registration() :
    path = "api/register"
    request_json =json.loads('{"email": "testemail@pytest.com"}')
    # Make POST request with Json Input body
    response = requests.post(url=baseUrl+path,json=request_json)
    # Parse Response to Json Format
    response_json = json.loads(response.text)
    assert response.status_code == 400
    assert jsonpath.jsonpath(response_json,'$.error')[0] == 'Missing password'

def randomDigits(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return str(random.randint(lower, upper))