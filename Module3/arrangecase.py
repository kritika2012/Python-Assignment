import string
st=input("Enter a string, dont enter a space in string")
l=[]
u=[]

l=[x for  x in st if x in string.ascii_lowercase]
u=[x for  x in st if x in string.ascii_uppercase]

print("".join(l+u))

