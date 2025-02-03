user_password = input('Enter your password: ')
try:
    if len(user_password) < 8:
        raise ValueError('Password is invalid. Password must be at least 8 characters long')
    if "Python" not in user_password:
        raise ValueError('Password is invalid. Password must contain "Python" word')
    if " " in user_password:
        raise ValueError('Password is invalid. Password must not contain space')

    print('Password is valid')
except ValueError as e:
    print(e)