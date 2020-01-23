dit={}
dit["Apple"]={"binomial name":"Malus Domestica","Major Producres":["China","US","Turkey"],"nutrition(in gms)":{"carbohydrates":13.18,"fat":0.17,"protien":0.26}}
dit["Mango"]={"binomial name":"Mangifera foetida","Major Producres":["India","Pakistan","Bangladesh"],"nutrition(in gms)":{"carbohydrates":220.3,"fat":0.33,"protien":0.56}}
dit["Cherry"]={"binomial name":"Prunus avium","Major Producres":["China","Dublin","Ireland"],"nutrition(in gms)":{"carbohydrates":21.00,"fat":0.23,"protien":0.99}}

for key,value in dit.items():
    print(key," - ",value)

list1=[]
list2=[]
for name,pro in dit.items():
    list1.append(name)
    list2.append(dit[name]["nutrition(in gms)"]["protien"])

print(list1)
print()
print(list2)

m=list2.index(max(list2))
print("Fruit {} has Highest protien of {}".format(list1[m],list2[m]))
hfruit=list1[m]

       
flist=[]
nlist=[]
for key1 in dit.keys():
    if "China" in dit[key1]["Major Producres"]:
        flist.append(key1)
        nlist.append(dit[key1]["nutrition(in gms)"]["protien"])
print(nlist," ",flist)
m=nlist.index(max(nlist))
print(flist[m])
        
