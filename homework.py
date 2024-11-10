user_credentials = {
    'bangladesh': '@shakib_alhassan',
    'india': '@virat_kohli',
    'pro1123mast': '@bloxfruits',
    'Chad': '@chad2345',
    'dekuoneforall': '@oneforall',
    'Layslover778878': '5980@gh',
    'chip': '@alpenrondweg',
    'swiftie7867': '@kreprep',
    'hoola7896': '@hoolayt',
    'coolbroace': 'Suvan'
}

# Ask user for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the username is in the dictionary
if username in user_credentials:
    # Check if the entered password matches the stored password
    if user_credentials[username] == password:
        print("You are now logged in to the system.Have fun ;)")
    else:
        print("Invalid password. Please try again.")
else:
    print("Invalid username. You are not a valid user of the system.")