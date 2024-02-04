def gcd(a,b): 
    if (a==0): 
        return b; 
    return gcd(b%a,a); 
  
# Function to return members of group Zn* 
def groupMembers(n):
    arr=[]
    # 1 is always a generator and member
    for i in range(1, n): 
        # Checking relative prime nature
        if (gcd(i,n)==1): 
            arr.append(i)
    return arr

# Function to return the primitive roots modulo p (Zp*)
def PrimitiveRoots(p): 
    members=groupMembers(p)
    factors=[]
    print("Euler's toutient function value: ")
    print("Phi(p): ",len(members))
    for i in range(1,len(members)+1):
        if(len(members)%i==0):
            factors.append(i)
    c=[]
    for i in members:
        ar=[]
        for j in factors:
            if(pow(i,j)%p==1):
                ar.append(j)
        if(len(ar)==0):
            c.append(0)
        else:
            c.append(min(ar))        
    return(c)

p=int(input("Enter a large prime number: "))
members=groupMembers(p)
print("The members in the group  Zp* are: ",members)

# d to be a member of the Zp* 
d=int(input("Select a number from the array as d(private key): "))
if(d not in members or d>p-2):
    print("Entered wrong number")
    
else:
    primitives=[]
    powers=PrimitiveRoots(p)

    # finding primitives from powers
    # Used Legrange's theorem
    for i in powers:
        if(i==len(members)):
            primitives.append(members[powers.index(i)])
            powers[powers.index(i)]=0
            
    # e1 is primitive root in Zp*
    print("The list of primitive roots are: ",primitives)
    e1=int(input("Enter the primitive root of Zp*: "))
    if(e1 not in primitives):
        print("Entered wrong number")
        
    else:
        e2=pow(e1,d)%p
        print("Public key (e1,e2,p): ",e1," ",e2," ",p)
        print("Private key (d): ",d)

        # Encryption
        print("Enter an integer from Zp*: ", members)
        r=int(input())
        if(r not in members):
            print("Entered wrong number")
            
        else:
            C1=pow(e1,r)%p
            message=int(input("Enter the message in numbers: "))
            C2=(message*pow(e2,r))%p

            # Decryption:
            P=(pow(C1,p-d-1)*C2)%p

            print("Encrypted message (C1): ",C1)
            print("Encrypted message (C2): ",C2)
            print("Decrypted message is: ",P)