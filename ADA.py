class vecThreeD:
    """A 3D vector"""
    def __init__(self, a, b, c):
        if a == 0 and b == 0 and c == 0: # Check if all values are zero
            raise ValueError("a,b,c values cannot all be zero") # Raise an error if all values are zero
        self.a, self.b, self.c, self.d, self.e, self.f = a, b, c # Values are not all zero, safe to assign
        self.d, self.e, self.f = 1, 1, 1 # Initialize second vector to 1 for the time being

    def __str__(self): #Maybe remove | Nah you're good
        return '{:.2f}i + {:2f}j + {:.2f}k'.format(self.x, self.y, self.z)
    def __repr__(self):
        return repr((self.x, self.y, self.z))
    def __sub__(self, other):
        return vecThreeD(self.x - other.x, self.y - other.y, self.z - other.z)
    
if __name__ == '__main__':
    while True:
        try:
            print("Please enter the x(a), y(b), z(c) vectors")
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            v1 = vecThreeD(a, b, c) #vector 1 initialized
            break #break out of the loop if no exception is raised
        except ValueError as e:
            print(f'{e}. Please try again\n')

    while True:
        print("Please choose one of these options(We are group 16, option b)")
        print("a. Addition")
        print("b. Substraction")
        print("c. Product")
        print("d. Cross-Product")
        print("e. Magnitude-Comparison")
        op = input("Option = ")
        if(op == "b"):
            break
        else:
            print("Please try again")
    
    v2 = vecThreeD(5, 7, 9)
    print('v1 = ', v1)
    print('str(v1) = ', str(v1))
    print('repr(v2) = ', repr(v2))
    print('v1 - v2 = ', v1 - v2)