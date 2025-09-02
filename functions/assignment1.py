#take 10 name from user then count and dispalythe numbr of users who have length more than 5 letters 




#funnction declaration 
def count(names):
    count1=0
    final_names=[]
    for e in names:
        if len(e)>5:
            count1+=1
            final_names.append(e)
        else:
            pass
    return count1,final_names  



names=[]
length=int(input("number of names which has to be inserted"))
for  i in range(length):
    x=input("enter the next name ")
    names.append(x)
print(names)
count1,final_names=count(names)

print("number of names larger than 5 letters",count1)
print(final_names)
