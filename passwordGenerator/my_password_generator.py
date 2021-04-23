import secrets, string

def MY_PASSWORD():
    """
    A program that displays a secure random password 
    : return: None
    """
    try:
        length_of_password = int(input('Enter the length of your desired password: '))
    except ValueError:
        print('Invalid Input!')
    else:
        password_picks = string.ascii_letters + string.digits + string.punctuation
        yourPassword = ''.join(secrets.choice(password_picks) for i in range(length_of_password))
        password_list = list(yourPassword)
        secrets.SystemRandom().shuffle(password_list)
        print('Your password is',''.join(password_list) )

MY_PASSWORD()
