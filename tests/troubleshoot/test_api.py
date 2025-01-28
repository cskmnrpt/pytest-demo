import requests


def test_api_status_code():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200


def test_api_response_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    response_data = response.json()
    assert response_data["id"] == 1
