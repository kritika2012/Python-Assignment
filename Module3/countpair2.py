def countPairs(n,list1,list2,sum):
    count1=0
    for i in list1:
        if sum-i in list2:
            count1+=1
    return count1



n=int(input("Enter the no of elements in first list"))
list1=[int(input()) for x in range(n)]
k=int(input("Enter the no of elements in first list"))
list2=[int(input()) for x in range(k)]
sum=int(input("Enter the sumto be searched"))
x=countPairs(n,list1,list2,sum)
print("No. of pairs in list1={}".format(x))
