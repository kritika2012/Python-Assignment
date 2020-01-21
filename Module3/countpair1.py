n=int(input("Enter the no of elements in the array"))
list=[int(input()) for x in range(n)]
print(list)
sum=int(input("Enter the sumto be searched"))
f=False
for i in list:
    if sum-i in list:
        f=True
if f==False:
    print("No pair present")
else:
    print("Yes pair present")
