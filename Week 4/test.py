import requests

ride = {
    "PULocationID": 13,
    "DOLocationID": 34,
    "trip_distance": 59
}
response = requests.post(url='http://localhost:8080/predict', json=ride)
print(response.body)
