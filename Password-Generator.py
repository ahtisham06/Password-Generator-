import random
import string

def password_generator(length, use_numbers, use_special_charc, use_uppercase):
  
  lowercase = string.ascii_lowercase
  uppercase = string.ascii_uppercase
  numbers = string.digits
  special_characters = string.punctuation

  all_characters = lowercase
  if use_numbers:
    all_characters += numbers
  if use_special_charc:
    all_characters += special_characters
  if use_uppercase:
    all_characters += uppercase

  password = ''.join(random.choice(all_characters) for _ in range(length))
  return password

print(' -------- Welcome to the password generator -------\n')

length = int(input('Enter the length of the password: '))
use_uppercase = input('Do you want to use uppercase letters? (y/n): ').lower() == 'y'
use_numbers = input('Do you want to use numbers? (y/n): ').lower() == 'y'
use_special_charc = input('Do you want to use special characters? (y/n): ').lower() == 'y'

password = password_generator(length, use_numbers, use_special_charc, use_uppercase)

print('\nYour generated password is: ', password)