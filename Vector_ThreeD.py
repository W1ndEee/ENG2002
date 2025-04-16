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