def EmailSlicer():
    emailAddress = input('Enter your email address: ')
    split_address = emailAddress.split('@')
    print(f'Your username is {split_address[0]}, while the domain name is {split_address[1]}')

EmailSlicer()