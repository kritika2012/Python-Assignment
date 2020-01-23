def frq(list1, size):
    answer_list = []
    freq = dict()
    for i in list1:
        if i in freq.keys():
             freq[i]+=1
        else:
            freq[i]=1
    freq = list(freq.items())
    for i in range(0, len(freq)-1):
        for j in range(i+1,len(freq)):
            if((freq[i][1] < freq[j][1]) or ((freq[i][1] == freq[j][1]) and freq[i][0]>freq[j][0])):
                freq[i],freq[j]=freq[j],freq[i]
        print(str(freq[i][0])*freq[i][1],end="")
        if(i==len(freq)-2):
            print(str(freq[i+1][0])*freq[i+1][1],end="")


size = int(input("enter size of elements"))
list1 = [int(input()) for i in range(0,size)]
fre(list1, size)
