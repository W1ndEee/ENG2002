from Vector_ThreeD import vecThreeD # Import the vecThreeD class from Vector_ThreeD.py
from Vector_ThreeD import vecAzm # Import the vecAzm class from Vector_ThreeD.py

"""Credit Start"""
def login(): # Login function for registered users to log in and new users to register
    f = open("logins.txt", "r")
    fread = f.read()
    fsplit = fread.split() # Split the file into a list of strings
    usernames = [] # Create empty lists for usernames and passwords
    passwords = []
    for i in range(1, len(fsplit), 4): # Loop through stored logins file. Since [1] is the first username and every 4 elements after that is a username, we start at 1 and increment by 4
        usernames.append(fsplit[i])
    for j in range(3, len(fsplit), 4): # Same as above but for passwords. [3] is the first password.
        passwords.append(fsplit[j])
    f.close()

    for k in range(3, 0, -1): # Loop for 3 attempts to log in
        inputuser = input('Enter your username: ')
        if inputuser in usernames: # Check if the input username is in the list of usernames
            inputpass = input('Enter your password: ') # Username is found in list, ask for password
            idx = usernames.index(inputuser) # Get the index of the username in the list of usernames
            if inputpass == passwords[idx]: # Check if the input password matches the password at the index of the username
                print('\nLogin successful. Welcome!\n')
                return True # Return True to indicate successful login
            else:
                print('\nIncorrect password. You have {} attempts left.\n'.format(k-1)) # Incorrect password. Show number of attempts left.
        else: # Username not found in list
            print('\nNew user. Please register.\n')
            inputpass = input('New password: ')
            try:
                ap = open("logins.txt", "a") # Open the logins file in append mode to add new username and password
                ap.write("\nUsername: {} Password: {}".format(inputuser, inputpass)) # Add new username and password on a new line.
                ap.close()
                print('\nLogin information stored. Welcome!\n')
                return True # Return True to indicate successful registration
            except Exception as e: # Catch any exceptions that occur while trying to write to the file
                print('Error storing login information:', e) 
    
    return False # Return False after 3 failed login attempts
"""Credit End"""

if __name__ == '__main__':

    exitflag = True # Flag to exit the program
    while exitflag: # Loop until the user chooses to exit or login fails

        exitflag = login() # Calls login function. Login successful returns True, Login failed returns False
        if not exitflag: # If login fails, exit the program
            break

        while True: # Login successful, continue
            # Try to get the values for the first vector
            try:
                print("Please enter the x(a), y(b), z(c) values for your 3D Vector")
                a = float(input("a = "))
                b = float(input("b = "))
                c = float(input("c = "))
                vector = vecAzm(a, b, c) # Vector 1 initialized
                break # Break out of the loop if no exception is raised
            except ValueError as e: # Catch the exception if the user enters a non-numeric value or all values are zero
                print(f'{e}. Please try again\n')

        while True:
            # Options menu, only option B is implemented since we are group 16.
            print("\nPlease choose one of these options (We are group 16, option c)")
            print("a. Azimuthal Angle")
            print("b. Addition")
            print("c. Substraction")
            print("d. Product")
            print("e. Cross-Product")
            print("f. Magnitude-Comparison")
            print("q. Quit")
            op = input("Option = ")

            if(op == "a" or op == "A"):
                # User chooses A for Azimuthal angle calculation
                while True:
                    # Try to get the number of terms for the Azimuthal angle calculation
                    try:
                        print("\nPlease enter the number of terms for the azimuthal angle calculation (Should be greater than 0)")
                        terms = int(input("Number of terms = "))
                        print('\n{}'.format(vector.findAzm(terms))) # Call the findAzm method to calculate the azimuthal angle
                        break
                    except Exception as e: # Handle any errors in the process
                        print('{}. Please try again'.format(e))

            elif(op == "c" or op == "C"):
                # User chooses C for subtraction
                while True:
                    # Try to get the values for the second vector
                    try:
                        print("\nPlease enter the x(d), y(e), z(f) values of the second vector (To be subtracted)")
                        d = float(input("d = "))
                        e = float(input("e = "))
                        f = float(input("f = "))
                        vector.updatev2(d, e, f) # Vector 2 initialized
                        break # Break out of the loop if no exception is raised
                    except ValueError as e: # Catch the exception if the user enters a non-numeric value or all values are zero
                        print(f'{e}. Please try again')
                
                #Display the result
                resultvector = vector.sub() # Store the result of the subtraction in a new vector
                print('\nResult: {} = {}'.format(vector, resultvector.result())) # Print result. Vector is the operation itself, resultvector is the result of the operation

            elif(op == 'q' or op == 'Q'):
                # User chooses to quit the program
                print('\nThank you for using the program. Goodbye!')
                exitflag = False # Set the exit flag to false to exit the program
                break

            else:
                print("Invalid option. Please try again") # Invalid option, prompt the user to try again

            