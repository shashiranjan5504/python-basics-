def search(list,n):
    global pos
    pos=0
    for i in list:
        pos=pos+1
        if i==n:
           return True
    return False
list=[5,8,4,6,9,2]
n=2
if search(list,n):
    print("Found at ",pos)
else:
    print("Not Found")
