def create_user(username, email, password, **kwargs):
    if len(username) < 5:
        print("Username must be at least 5 characters")
    elif "@" not in email:
        print("Email must have @ in it")
    elif len(password) < 8:
        print("Password must be at least 8 characters")
    else:
        return f'Validation is successful: \n Name: {username} \n Email: {email} \n Password: {password} \n {kwargs}'


result = create_user("john", "johnexample.com", "pass123")
if result:
    print(result)

result2 = create_user("vasya", "vasya@example.com", "password123", age=45)
if result2:
    print(result2)