
def sequence(n):
    arr=[]
    i=0
    # creating the sequence required for
    # implementing railfence cipher
    # the sequence is stored in array
    while(i<n-1):
        arr.append(i)
        i+=1
    while(i>0):
        arr.append(i)
        i-=1
    return(arr)

# this is to implement the logic
def railfence(s,n):
    # converting into lower cases
    s=s.lower()

    # If you want to remove spaces,
    # you can uncomment this
    # s=s.replace(" ","")

    # returning the sequence here
    L=sequence(n)
    print("The raw sequence of indices: ",L)
    print("Transformed message for encryption: ",s)

    # converting into cipher text
    num=0
    cipher_text=""
    while(num<n):
        for i in range(L.count(num)):
            # adding characters according to
            # indices to get cipher text
            cipher_text=cipher_text+s[L.index(num)]
            L[L.index(num)]=n
        num+=1
    print("The cipher text is: ",cipher_text)
   
plain_text=input("Enter the string to be encrypted: ")
n=int(input("Enter the number of rails: "))
railfence(plain_text,n)
