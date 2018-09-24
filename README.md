# BookAPI

requires 'pip install pyjwt'
Can create new credentials via createUser function.
(default username: user1, password: password)

Run API.py
POST valid username and password to http://127.0.0.1:5000/login
retrieve token

example POST:
 http://127.0.0.1:5000/books?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAi
