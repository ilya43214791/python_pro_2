import requests

payload = {
    "email": "gdgd@gmail.com",
    "password": "getgid",
    "first_name": "Dolby",
    "last_name": "gffhfh",
    "role": "senior",

}
response = requests.post("http://localhost:8000/users/create", data=payload)
breakpoint()
print(response.json())
