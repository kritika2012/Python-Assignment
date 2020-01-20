pnum=int(input("Enter the pocket number"))
if 0<=pnum<=36:
    if pnum==0:
        print("Pocket is GREEN")
    elif pnum<=10 :
        if pnum%2==0:
            print("Pocket are BLACK")
        else:
            print("Pocket are RED")
    elif pnum<=18:
        if pnum%2==0:
            print("Pocket are RED")
        else:
            print("Pocket are BLACK")
    elif pnum<=28:
        if pnum%2==0:
            print("Pocket are BLACK")
        else:
            print("Pocket are RED")
    elif pnum<=36:
        if pnum%2==0:
            print("Pocket are RED")
        else:
            print("Pocket are BLACK")
else:
    print("INVALID NUMBER ENTERED!!!")
        
