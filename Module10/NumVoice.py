import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
ones=["zero","one","two","three","four","five","six","seven","eight","nine"]
tens=["Ten","Eleven","Twelvth","Thirteen","Fourteen","Fifteen","Sisteen","Seventeen","Eighteen","Nineteen"]
tens1=["","Ten","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
hundred=["Hundred","Thousand","Lakh"]
n=input("ENter a number :")
s=int(n)
if(len(n)==1):
	speaker.Speak(ones[int(s)])
if(len(n)==2 and s<20):
	speaker.Speak(tens[int(s-10)])
if(len(n)==2 and s>=20):
	if(int(n[1])!=0):
		speaker.Speak((tens1[int(n[0])],ones[int(n[1])]))
	else:
		speaker.Speak(tens1[int(n[0])])
if(len(n)==3):
	if(int(n[2])!=0):
		if(int(n[1])==1):
			speaker.Speak((ones[int(n[0])],hundred[0],"and",tens[int(n[2])]))
		else:
			speaker.Speak((ones[int(n[0])],hundred[0],"and",tens1[int(n[1])],ones[int(n[2])]))
	else:
		speaker.Speak((ones[int(n[0])],hundred[0],tens1[int(n[1])]))
if(len(n)==4):


	
	if(int(n[1])!=0):
	
		if(int(n[2])!=0):

			if(int(n[3])!=0):

				if(int(n[2])!=1):
					speaker.Speak((ones[int(n[0])],hundred[1],ones[int(n[1])],hundred[0],"and",tens1[int(n[2])],ones[int(n[3])]))
				else:
					speaker.Speak((ones[int(n[0])],hundred[1],ones[int(n[1])],hundred[0],"and",tens[int(n[3])]))
			else:
				speaker.Speak((ones[int(n[0])],hundred[1],ones[int(n[1])],hundred[0],"and",tens1[int(n[2])]))
		else:	
			speaker.Speak((ones[int(n[0])],hundred[1],ones[int(n[1])],hundred[0],"and",ones[int(n[3])]))
	else:
		if(int(n[3])!=0):
			if(int(n[2])!=1):
				speaker.Speak((ones[int(n[0])],hundred[1],"and",tens1[int(n[2])],ones[int(n[3])]))
			else:
				speaker.Speak((ones[int(n[0])],hundred[1],tens[int(n[3])]))
		else:
			speaker.Speak((ones[int(n[0])],hundred[1],tens1[int(n[2])]))


			


