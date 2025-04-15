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



if __name__ == '__main__':

    exitflag = True # Flag to exit the program
    while exitflag: # Loop until the user chooses to exit
        while True:
            # Try to get the values for the first vector
            try:
                print("Please enter the x(a), y(b), z(c) values for your 3D Vector")
                a = float(input("a = "))
                b = float(input("b = "))
                c = float(input("c = "))
                vector = vecThreeD(a, b, c) # Vector 1 initialized
                break # Break out of the loop if no exception is raised
            except ValueError as e: # Catch the exception if the user enters a non-numeric value or all values are zero
                print(f'{e}. Please try again\n')

        while True:
            # Options menu, only option B is implemented since we are group 16.
            print("\nPlease choose one of these options (We are group 16, option b)")
            print("a. Addition")
            print("b. Substraction")
            print("c. Product")
            print("d. Cross-Product")
            print("e. Magnitude-Comparison")
            print("q. Quit")
            op = input("Option = ")
            if(op == "b" or op == "B"):
                # User chooses B for subtraction
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
                print('\nResult: {} = {}\n'.format(vector, resultvector.result())) # Print result. Vector is the operation itself, resultvector is the result of the operation
                break

            elif(op == 'q' or op == 'Q'):
                # User chooses to quit the program
                print('\nThank you for using the program. Goodbye!')
                exitflag = False # Set the exit flag to false to exit the program
                break
            else:
                print("Please try again") # Invalid option, prompt the user to try again

            