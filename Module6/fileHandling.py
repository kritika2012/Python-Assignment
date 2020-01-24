def main():
    #For opening a file
    file1=open(r"F:\kritika\kritika.txt",'w+')

    #For Writing to a file
    file1.write("Hi there Kritika! \n")
    file1.write("How was your day? \n")
    file1.write("This file is open in write or w mode")
    file1.close()
   

    #For Performing The Reading Operation
    file1=open(r"F:\kritika\kritika.txt",'r')
    readfile1=file1.read()
    file1.close()
    print(readfile1)

def read():
    #For reading line by line we use readline()
    file2=open(r"F:\kritika\kritika2.txt",'r')
    readf=file2.readline()
    while readf!='':
        print(readf)
        readf=file2.readline()
    file2.close()

main()
read()
