pac=int(input("Enter the nmber of pacakges purchased"))
discount=0
if pac>=100:
    discount=0.4
elif pac>=50:
    discount=0.3
elif pac>=20:
    discount=0.2
else:
    if pac>=10:
      discount=0.1

tdiscount=pac*discount*99
print("AMOUNT OF DISCOUNT: {}".format(tdiscount))

total=(pac*99)-tdiscount
print("TOTAL AMOUNT OF PURCHASE AFTER DISCOUNT IS: {}".format(total))

    
