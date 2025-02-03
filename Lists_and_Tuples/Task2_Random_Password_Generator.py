import random
import string

list_of_characters = list(string.ascii_letters) + list(string.digits)
random_password    = ''.join(random.choices(list_of_characters, k=8))

print(random_password)
