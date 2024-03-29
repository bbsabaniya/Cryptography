import string
main=string.ascii_lowercase
def generate_key(n,s):
    s=s.replace(" ","")
    s=s.lower()   
    key_matrix=['' for i in range(n)]
    i=0;j=0
    for c in s:
        if c in main:
            key_matrix[i]+=c
            j+=1
            if(j>n-1):
                i+=1
                j=0
    print("The key matrix "+"("+str(n)+'x'+str(n)+") is:")
    print(key_matrix)   
    key_num_matrix=[]
    for i in key_matrix:
        sub_array=[]
        for j in range(n):
            sub_array.append(ord(i[j])-ord('a'))
        key_num_matrix.append(sub_array)  
    for i in key_num_matrix:
        print(i)
    return(key_num_matrix)
def message_matrix(s,n):
    s=s.replace(" ","")
    s=s.lower()
    final_matrix=[]
    if(len(s)%n!=0):
        while(len(s)%n!=0):
            s=s+'z'
    print("Converted plain_text for encryption: ",s)
    for k in range(len(s)//n):
        message_matrix=[]
        for i in range(n):
            sub=[]
            for j in range(1):
                sub.append(ord(s[i+(n*k)])-ord('a'))
            message_matrix.append(sub)
        final_matrix.append(message_matrix)
    print("The column matrices of plain text in numbers are:  ")
    for i in final_matrix:
        print(i)
    return(final_matrix)
def getCofactor(mat, temp, p, q, n): 
    i = 0
    j = 0
    for row in range(n):  
        for col in range(n): 
            if (row != p and col != q) : 
                temp[i][j] = mat[row][col] 
                j += 1
                if (j == n - 1): 
                    j = 0
                    i += 1
def determinantOfMatrix(mat, n): 
    D = 0 # Initialize result 
    if (n == 1): 
        return mat[0][0]  
    temp = [[0 for x in range(n)]  
               for y in range(n)]  
    sign = 1 # To store sign multiplier 
    for f in range(n):  
        getCofactor(mat, temp, 0, f, n) 
        D += (sign * mat[0][f] *
              determinantOfMatrix(temp, n - 1))  
        sign = -sign 
    return D  
def multiply_and_convert(key,message):
    res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))] 
    for i in range(len(key)): 
        for j in range(len(message[0])):
            for k in range(len(message)): 
                res_num[i][j]+=key[i][k] * message[k][j]
    res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
    for i in range(len(key)):
        for j in range(len(message[0])):
            res_alpha[i][j]+=chr((res_num[i][j]%26)+97)         
    return(res_alpha)
n=int(input("What will be the order of square matrix: "))
s=input("Enter the key: ")
key=generate_key(n,s)
    
plain_text=input("Enter the message: ")
message=message_matrix(plain_text,n)
final_message=''
for i in message:
    sub=multiply_and_convert(key,i)
    for j in sub:
        for k in j:
            final_message+=k
print("plain message: ",plain_text)
print("final encrypted message: ",final_message)