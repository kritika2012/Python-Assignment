pac=int(input("Enter the nmber of pacakges purchased"))
discount=0
if 10<=pac<=19:
    discount=0.1
elif 20<=pac<=49:
    discount=0.2
elif 50<=pac<=99:
    discount=0.3
else:
    if pac>=100:
      discount=0.4

tdiscount=pac*discount*99
print("AMOUNT OF DISCOUNT: {}".format(tdiscount))

total=(pac*99)-tdiscount
print("TOTAL AMOUNT OF PURCHASE AFTER DISCOUNT IS: {}".format(total))

    
