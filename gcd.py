def gcd(z,y):
    if(y==0):
        return z
    else:
        return gcd(y,z%y)
z=int(input("enter first number:"))
y=int(input("enter second number:"))
GCD=gcd(z,y)
print("GCD is: ")
print(GCD)
    
