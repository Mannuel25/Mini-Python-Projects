def EMAIL_ADDRESS_SLICER():
    """
    Displays the username and domain name of an email address
    : return: None
    """
    emailAddress = input('Enter your email address: ').strip()
    split_address = emailAddress.split('@')
    print(f'Your username is {split_address[0]}, while the domain name is {split_address[1]}')

EMAIL_ADDRESS_SLICER()