import requests
import json
import jsonpath

# base Url
baseUrl = "https://reqres.in/"


def test_fetch_user():
    path = "api/users/2"
    # Send Get Requests
    response = requests.get(url=baseUrl + path)
    # Parse Response to Json Format
    json_response = json.loads(response.text)
    print(str(jsonpath.jsonpath(json_response, '$.data.first_name')[0]))
    assert response.status_code == 200
    assert jsonpath.jsonpath(json_response, '$.data.first_name')[0] == 'Janet'
    assert jsonpath.jsonpath(json_response, '$.data.id')[0] == 2


def test_fetch_users():
    path = "api/users?page=2"
    # Send Get Requests
    response = requests.get(url=baseUrl + path)
    # Parse Response to Json Format
    json_response = json.loads(response.text)
    first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
    uid = jsonpath.jsonpath(json_response, 'data[1].id')
    assert response.status_code == 200
    assert str(first_name[0]) == 'Michael'
    assert int(uid[0]) == 8


def test_create_delete_user():
    path = "api/users"

    # Read input json file
    file = open('TestData/user.json', "r")
    json_input = file.read()
    request_json = json.loads(json_input)

    # Make POST request with Json Input body
    response = requests.post(url=baseUrl + path, json=request_json)
    response_json = json.loads(response.text)
    assert response.status_code == 201
    assert jsonpath.jsonpath(response_json, '$.name')[0] == request_json["name"]
    id = jsonpath.jsonpath(response_json, '$.id')[0]
    response = requests.delete(url=baseUrl + path + '/' + id)
    assert response.status_code == 204
