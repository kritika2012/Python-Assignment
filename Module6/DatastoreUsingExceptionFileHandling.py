def four():
    while True:
        try:
            inp1=input("select the basic key you want to make change: ")
            if inp1 in datastore.keys():
                set(inp1)

            else:
                print("Inalid value Entered,Please enter the values again.")
        except:
                print("Inalid value Entered,Please enter the key again.")

def set(inp1):
    for key,val in datastore[inp1].items():
        print(key)
    try:
        while True:
            att=input("Enter the attribute you want to change in this:")
            if att=="medical":
                for i in range(len(datastore["office"][att])):
                    print(i,"  ",(datastore["office"]["medical"][i]))
                
                while True:
                    try:
                        index=int(input("select the index at which you want to change value"))
                        matt=input("select the attribute you want to make a change in")
                        nval=input("Enter the modified value")

                        print("Enter attributes from these option-",datastore["office"]["medical"][index].keys())
                        if matt in datastore["office"]["medical"][index].keys():
                            datastore[inp1][att][index][matt]=nval
                            print(datastore[inp1][att])
                            break
                        
                    except:
                        print("invalid data :",error.value)

            elif att=="parking":
                while True:
                        try:
                            print("Various fields in {} are".format(att))
                            print(datastore[inp1][att])
                            patt=input("select the attribute you want to make a change in")
                            pval=input("Enter the modified value")
                            datastore[inp1][att][patt]=pval
                            print(datastore[inp1][att])
                            break
                        except:
                            print("Inalid value Entered,Please enter the values again.")
            else:
                print("Inalid value Entered,Please enter the values again.")
    except:
        print("Inalid value Entered,Please enter the values again.")


def new():
    while True:
        try:
            attribute=input("enter the attriibute which you want to add")
            diy={input("enter the dictionary you want to add with the key")}
            datastore[attribute]=diy
            print(datastore)
            break
        except:
                print("Inalid value Entered,Please enter the values again. ")

       
datastore={"office":{"medical":[{"room number":100,"use":"reception","sq-ft":50,"price":75},
                     {"room number":101,"use":"waititng","sq-ft":250,"price":75},
                     {"room number":102,"use":"examination","sq-ft":125,"price":150},
                     {"room number":103,"use":"examination","sq-ft":125,"price":150},
                     {"room number":104,"use":"examination","sq-ft":150,"price":100},
                     ]
           ,"parking":{"location":"premium","style":"covered","price":750}}}

print("Hi there user!!! Select one of the given options to perform further actions")
while True:
    try:
        inpt=int(input("1 View Datastore \n2 View Keys of Office\n3 View Complete Keys Information of the office\n4 Make changes to the existing datastore Parts\n5 Add keys to office\n6 Add new key to Datastore\n7 Delete a key from Datastore\n8 Delete a key from office"))

        if inpt==1:
            print(datastore)
            break

        
        if inpt==2:
            for k,v in datastore["office"].items():
                print(k)
            break

            
        if inpt==3:
            print(datastore["office"])
            break
        
        if inpt==4:
            four()
            break

            
        if inpt==6:
            ans=input("Do you want to maually enter new data?")
            if ans=='yes':
                new()
            else:
                print("Thankyou for using our Application!!!")
            break

                
        if inpt==5:
            okey=input("Enter the key name")
            odit={input("Enter the new dictionary with the associated key")}
            datastore["office"][okey]=odit
            print(datastore["office"])
            break

        if inpt==7:
            print(datastore)
            dkey=input("Enter the key to be deleted from datastore")
            del datastore[dkey]
            print(datastore)
            break

        if input==8:
            for kk,vv in datastore["office"].items():
                print("Key(Office) -",kk)
            ofkey=input("Enter the key you want to delete from office")
            del datastore["office"][kk]
            print("Modified list of keys in office")
            for kkk,vvv in datastore["office"].items():
                print("Key(Office) -",kkk)
            break
        
        else:
            print("Inalid value Entered,Please enter the values again. ")
    except:
        print("Inalid value Entered,Please enter the values again. ")
        
    

    

    
    

    






                     
