n=int(input("Enter the number of items"))
retail=0
i=0
while(i<=n):
    wholesale=int(input("Enter whole sale prize"))
    if wholesale>0:
         retail=(wholesale*0.5)
         print("retail is: ",retail)
    else:
        print("Negative Value Entered")
    i+=1
    
