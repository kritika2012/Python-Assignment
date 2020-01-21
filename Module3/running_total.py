trees = int(input("enter number of trees: "))
seconds = int(input("enter number of seconds: "))
print("enter fruit number for each tree: ")
list =[int(input()) for i in range(0, trees)]
maxsum=0
for i in range(0, len(list)):
    sum =0
    for j in range(i, i+seconds):
        sum+=list[j%len(list)]
    if(sum>maxsum):
        maxsum=sum
print("maximum fruit value is: {}".format(maxsum))
