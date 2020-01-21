n=int(input("Enter the number of elements in list"))
print("Enter the elements of the first list")
list1=[int(input()) for x in range(n)]
print("Enter the elements of the second list")
list2=[int(input()) for x  in range(n-1)]
print("The missing element is {}".format(sum(list1)-sum(list2)))

