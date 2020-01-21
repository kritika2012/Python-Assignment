import math
st=input("Enter the deatils of the student")
st=st.split(",")
nlist=[int(x) for x in st[1:]]
print(nlist)

per=(sum(nlist)/590)*100
print('{0} obtained {1} marks out of {2} in theory and {3} marks out of {4} in practical and successfully passed the exam with {5} in aggreate'.format(st[0],sum(nlist[0:5]),500,sum(nlist[5:8]),90,per))
