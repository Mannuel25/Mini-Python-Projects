import secrets
import string

def password_generator():
    """
    A program that generates a secure random password
    : return: None
    """
    length_of_alphabets = int(input('Enter the length of alphabets (upper and lower case inclusive): '))
    length_of_digits = int(input('Enter the length of digits: '))
    length_of_special_characters = int(input('Enter the length of special characters: '))
    passwordLength = length_of_alphabets + length_of_digits + length_of_special_characters
    securePassword = ''.join(secrets.choice(string.ascii_letters) for i in range(length_of_alphabets))
    securePassword += ''.join(secrets.choice(string.digits) for i in range(length_of_digits))
    securePassword += ''.join(secrets.choice(string.punctuation) for i in range(length_of_special_characters))
    generated_password = list(securePassword)
    secrets.SystemRandom().shuffle(generated_password)
    print('Your password of length {} is {}'.format(passwordLength,''.join(generated_password)))

password_generator()
