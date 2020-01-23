people={"class":{1:"kritika",2:"kaushiki",3:"shachee",4:"shree"},"department":{"it":{"A":"big data","b":"cloud"}}}
print(people)

#Acessing the elements of the dictionaries
print(people["class"][1],"belongs to ",people["department"]["it"]["A"]," department")
print()

#Adding a new record
people["acd"]={}
people["acd"][4]=8.73
people["acd"]["avg"]=8.55
print(people)
print()

#Second way of adding elemts
people["state"]={1:"M.P",2:{"city":"Dewas","pin":455001}}
print(people)
print()

#deleting an element from dictionary or nested dictionary
del people["state"][2]["pin"]
print(people)
print()

#Iterating through dictionary
for k,val in people.items():
    print("keys: {}".format(k),"\n")
    print()
    for v in val:
        print(val," - ",val[v],"\n")
print()
