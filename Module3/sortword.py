st=input("enter the input here ")
st=st.split(" ")
st.sort()
lst=[]
for i in range(len(st)):
    if st[i] not in lst:
        lst.append(st[i])
for j in lst:
    print(j,end=" ")
