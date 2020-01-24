import pickle

phone={"kritika":4444,"kaushiki":5555,"shachee":6666,"shree":7777}
outfile=open("phone.dat",'wb')
pickle.dump(phone,outfile)
outfile.close()

file1=open('phone.dat','rb')
pb=pickle.load(file1)
file1.close()
print(pb)
