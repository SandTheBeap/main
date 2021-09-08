import random
from random import choice
from os import system
import time

# Texts

digits = '0123456789'
letters = 'abdcefghijklmn' \
        'opqrstuvwxyz'
special = '_@!$%?&'
up = letters.upper()
all = digits+letters+special+up

# Final

number = int(input("How Long Would You Like The Password To Be? "))
password = ''.join(choice(all) for i in range(number))

# Print

print(password)

# Timer

time.sleep(5)
system('clear')
print('Timeout 404')
time.sleep(0.25)
system('clear')
