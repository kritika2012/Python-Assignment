print("Pattern1")
print()
print()
k=5
for i in range(5):
    for j in range(k):
        print("*",end="")
    k-=1
    print()
k=1
for i in range(5):
    for j in range(k):
        print("*",end="")
    k+=1
    print()
print()
print()
print("Pattern 2       ")
print()
print()
k=5
for i in range(k):
    for j in range(k):
        print(" ",end="")
    print("*")
for l in range(0,11):
    print("*",end="")
k=5
print()
for i in range(k):
    for j in range(k):
        print(" ",end="")
    print("*")
    

print()
print()
print(" Pattern 3       ")
print()
print()
k=5
l=1
for i in range(7):
    l+=1
    for j in range(k+1):
        print(" ",end="")
    for m in range(i+1):
        if (i+1)%2!=0:
            print("* ",end="")
    k-=1
    print()
print()

k=5
l=1
for i in range(7):
    for m in range(i+1):
        print(" ",end="")
    for j in range(k):
        if (i+1)%2!=0:
            print(" *",end="")
    k-=1
    l+=1
    print()
    

    
print()
print()
print(" Pattern 4       ")
print()
print()
k=6
for i in range(7):
    for j in range(k):
        print(" ",end="")
    print("* ",end="")
    k-=1
    m=2*i
    for p in range(m-2):
        if m!=12:
            print(" ",end='')
    if i!=0:
        print("*",end="")
    if m==12:
             print(" * * * * * ",end='')
    print()




