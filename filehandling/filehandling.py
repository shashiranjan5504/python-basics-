#for reading the whole data of mydata file 
f=open("mydata.txt","r")
print(f)
print(f.read())
#writing something in another file
f1=open("abc",'w')
f1.write("my name is shashi ranjan")
#appending something
f1=open("abc",'a')
f1.write("i just love  things")

# for printing below statement we have to open it and also decalring it what to do 
f=open("mydata.txt","r")
print(f.readline(),end="")#this staement is used for writing specific lines of the whole data
print(f.readline(),end="")
print(f.readline(4),end="")

# copy text from data and  paste  it into abc file

f1=open("abc",'a')

for  data in f:
    f1.write(data)
 