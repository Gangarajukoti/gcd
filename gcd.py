def gcd(z,y):
    if(y==0):
        return z
    else:
        return gcd(y,z%y)
z=int(input("enter first number of z:"))
y=int(input("enter second number of y:"))
GCD=gcd(z,y)
print("GCD is: ")
print(GCD)
    
