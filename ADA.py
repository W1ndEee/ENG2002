class vecThreeD:
    """A 3D vector"""
    def __init__(self, a, b, c):
        if a == 0 and b == 0 and c == 0: # Check if all values are zero
            raise ValueError("a,b,c values cannot all be zero") # Raise an error if all values are zero
        self.a, self.b, self.c = a, b, c # Values are not all zero, safe to assign
        self.d, self.e, self.f = 1, 1, 1 # Initialize second vector to 1 for the time being

    def __str__(self): # Default string when calling the object on it's own
        return '({a} - {d})i + ({b} - {e})j + ({c} - {f})k'.format(a = self.a, b = self.b, c = self.c, d = self.d, e = self.e, f = self.f) # Format the string to show operation
    
    def sub(self):
        return vecThreeD(self.a - self.d, self.b - self.e, self.c - self.f)
    
    def updatev2(self, d, e, f):
        if d == 0 and e == 0 and f == 0:
            raise ValueError("d,e,f values cannot all be zero")
        self.d, self.e, self.f = d, e, f

    def result(self):
        def formatresult(val):
            sign = '+' if val >= 0 else ''
            return '{}{}'.format(sign, val)
        return '{}i{}j{}k'.format(self.a, formatresult(self.b), formatresult(self.c))



if __name__ == '__main__':

    while True:
        try:
            print("Please enter the x(a), y(b), z(c) vectors")
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            vector = vecThreeD(a, b, c) #vector 1 initialized
            break #break out of the loop if no exception is raised
        except ValueError as e:
            print(f'{e}. Please try again\n')

    while True:
        print("\nWelcome! Please choose one of these options (We are group 16, option b)")
        print("a. Addition")
        print("b. Substraction")
        print("c. Product")
        print("d. Cross-Product")
        print("e. Magnitude-Comparison")
        print("q. Quit")
        op = input("Option = ")
        if(op == "b" or op == "B"):
            while True:
                try:
                    print("Please enter the x(d), y(e), z(f) values of the second vector (To be subtracted)")
                    d = float(input("d = "))
                    e = float(input("e = "))
                    f = float(input("f = "))
                    vector.updatev2(d, e, f) # Vector 2 initialized
                    break
                except ValueError as e:
                    print(f'{e}. Please try again\n')
            break
        elif(op == 'q' or op == 'Q'):
            print('Thank you for using the program. Goodbye!')
            exit()
        else:
            print("Please try again")

    resultvector = vector.sub()
    print('{} = {}'.format(vector, resultvector.result()))