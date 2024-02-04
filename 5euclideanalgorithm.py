# Euclidean algorithm for GCD(a,b)

a=int(input("Enter a: "))
b=int(input("Enter b: "))

r1=a
r2=b
while(r2>0):
    quo=r1//r2
    rem=r1%r2
    print(quo,r1,r2,rem)
    r1=r2
    r2=rem

print("The GCD of ",a, " and ",b," is ",r1)
