ind={}
ind["Player 1"]={"name":"Hardik","type":"All rounder","matches":100,"runs":156955,"average":548255,"Highest score":5000}
ind["Player 2"]={"name":"Dhoni","type":"Batsman","matches":1000,"runs":9992525,"average":24891,"Highest score":6223}
ind["Player 3"]={"name":"Rohit","type":"Batsman","matches":200,"runs":4851255,"average":54891,"Highest score":56922}
ind["Player 4"]={"name":"Rahul","type":"Batsman","matches":200,"runs":578514,"average":99155,"Highest score":25614}
ind["Player 5"]={"name":"Shami","type":"Bowler","matches":300,"runs":179628,"average":522,"Highest score":568}
ind["Player 6"]={"name":"Virat","type":"All Rounder","matches":500,"runs":4522589,"average":21561,"Highest score":2456}

print()
print()

for k,val in ind.items():
    print("keys: {}   {}".format(k,val),"\n")
print()


print("player- {} has successfully played {} matches and scored {} total runs with an average of {}".format(ind["Player 6"]["name"],ind["Player 6"]["matches"],ind["Player 6"]["runs"],ind["Player 6"]["average"]))
