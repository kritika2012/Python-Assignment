st=input("Enter the data")
list=[]
nlist=["0","1","2","3","4","5","6","7","8","9"]
for i in range(len(st)-1):
    if st[i] in nlist and st[i+1] in nlist:
        list.append(int(st[i]+st[i+1]))
    elif st[i] in nlist:
        list.append(int(st[i]))
    else:
        pass
print(list)
print("sum={0} and average={1} ".format(sum(list),sum(list)/(len(list))))
