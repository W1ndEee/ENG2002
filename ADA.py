class vecThreeD:
    """A 3D vector"""
    def __init__(self, a, b, c):
        if a == 0 and b == 0 and c == 0: # Check if all values are zero
            raise ValueError("a,b,c values cannot all be zero") # Raise an error if all values are zero
        self.a, self.b, self.c = a, b, c # Values are not all zero, safe to assign
        self.d, self.e, self.f = 1, 1, 1 # Initialize second vector to 1 for the time being

    def __str__(self): # Default string when calling the object on it's own
        return '({a} - {d})i + ({b} - {e})j + ({c} - {f})k'.format(a = self.a, b = self.b, c = self.c, d = self.d, e = self.e, f = self.f) # Format the string to show operation
    
    def sub(self): # Subtraction method
        return vecThreeD(self.a - self.d, self.b - self.e, self.c - self.f) # Subtract the second vector from the first vector
    
    def updatev2(self, d, e, f): # Initialize the second vector
        if d == 0 and e == 0 and f == 0: # Check if all values are zero
            raise ValueError("d,e,f values cannot all be zero") # Raise an error if all values are zero
        self.d, self.e, self.f = d, e, f # Values are not all zero, safe to assign

    def result(self): # Result method to return the result string of the operation
        def formatresult(val): # Format the result string to show the sign of the value
            sign = '+' if val >= 0 else '' # Check if the value is positive or negative, if positive, add a '+' sign
            return '{}{}'.format(sign, val)
        return '{}i{}j{}k'.format(self.a, formatresult(self.b), formatresult(self.c)) 

"""Disctinction Start"""    
class vecAzm(vecThreeD): # Subclass of vecThreeD, has two new methods arctan and findAzm
    """A 3D vector with with option to find zimuthal angle (Subclass of vecThreeD)"""
    def arctan(self, z, t): # Method to calculate the arctan of z with t terms using the Taylor series expansion
        if t >= 1: # Check if the number of terms is greater than or equal to 1
            result = z - (z**3) / 3 # First term added since there is at least 1 terms
            num = 5 # Initialize num to 5 since the next term will be z^5 / 5
            for i in range(t-1): # t-1 because we already added the first term
                if i % 2 == 0: # Even i means second, fourth, sixth, etc. terms
                    result = result + (z**num) / num
                elif i % 2 == 1: # Odd i means third, fifth, seventh, etc. terms
                    result = result - (z**num) / num
                num += 2 # Increment num by 2 for the next term
        else: ## If the number of terms is less than 1 (e.g. 0, -1, -2), raise an error
            raise AssertionError('Your number of terms should not be 0 or less than 0')
        return result
    
    def findAzm(self, terms): # Method to find the azimuthal angle
        z = self.b / self.a # Calculate z as b/a from the user's vector
        if z < -1 or z > 1: # Check if z is within the valid range (-1 <= z <= 1), if not, raise an error
            raise AssertionError('The input argument for the method is out of the valid range (b/a must be between -1 and 1)')
        elif terms <= 0: # Check if the number of terms is less than or equal to 0, if so, raise an error
            raise AssertionError('Your number of terms should not be 0 or less than 0')
        else: # All checks are good. Return the azimuthal angle with 3 decimal places
            return 'Azimuth: {:.3f}'.format(self.arctan(z, terms)) # Call arctan function with z and user's terms
"""Distinction End"""

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

            