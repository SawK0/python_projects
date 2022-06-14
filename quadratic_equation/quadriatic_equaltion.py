import math

# quadratic equation -> x = (-b +|- sqrt(b**2 - 4ac))/2a
def quadratic(a=1, b=0, c=0):
    if a == 0:
        return "(NA, NA) \nERROR: 'a' value shouldn't be zero"
    d = abs((b**2) - 4*a*c)
    s1 = (-b + math.sqrt(d))/(2*a)
    s2 = (-b - math.sqrt(d))/(2*a)
    
    return s1, s2


print(quadratic(0, 4, 4))
