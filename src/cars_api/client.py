import requests

# response = requests.post(
#     'http://127.0.0.1:8000/cars/',
#     json={
#     "brand": 'Toyota',
#     "model": "Corolla",
#     "year_of_issue": 2010,
#     "fuel_type": "Petrol",
#     "gearbox_type": "Automatic",
#     "mileage": 100000,
#     "price": 10000.0
# },
#
#
# )
# print(response.status_code)
# print(response.json())

# response = requests.patch(
#     'http://127.0.0.1:8000/cars/7',
#     json={
#     "brand": 'Toy',
#     "model": "Corolla",
#     "year_of_issue": 2010,
#     "fuel_type": "Petrol",
#     "gearbox_type": "Automatic",
#     "mileage": 100000,
#     "price": 10000.0
# },
#
#
# )
# print(response.status_code)
# print(response.json())

response = requests.get(
    'http://127.0.0.1:8000/2/',
)

print(response.status_code)
print(response.json())


# response = requests.delete(
#     'http://127.0.0.1:8000/cars/3',
#
# )
# print(response.status_code)
# print(response.json())
