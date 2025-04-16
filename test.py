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

class vecAzm(vecThreeD):
    """A 3D vector with azimuthal angle"""
    def arctan(z, t):
        #z = self.b / self.a
        #if z < -1 or z > 1:
            #raise AssertionError('The input argument for the method is out of the valid range (b/a must be between -1 and 1)')
        
        if t >= 1:
            result = z - (z**3) / 3
            num = 5
            for i in range(t-1):
                if i % 2 == 0:
                    result = result + (z**num) / num
                elif i % 2 == 1:
                    result = result - (z**num) / num
                num += 2
        else:
            raise AssertionError('Your number of terms should not be 0 or less than 0')
        return result
    
    def findAzm(self, terms):
        z = self.b / self.a
        if z < -1 or z > 1:
            raise AssertionError('The input argument for the method is out of the valid range (b/a must be between -1 and 1)')
        elif terms <= 0:
            raise AssertionError('Your number of terms should not be 0 or less than 0')
        else:
            return 'Azimuth: {.3f}'.format(self.arctan(z, terms))
        

if __name__ == "__main__":
    vector = vecThreeD(3, 2, 4)

    print(vector.findAzm(100))