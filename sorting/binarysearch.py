#pos=-1
def search(list,n):
    start=0
    end=len(list)-1
    while start<=end:
        mid=(start+end)//2
        if list[mid]==n:
            # globals()['pos']=mid
            global pos
            pos=mid
            return True
        elif list[mid]<n:
            start=mid+1
        else:
            end=mid-1
    return False

        



list=[4,7,8,12,45,99]
n=45
if search(list,n):
    print("found at ",pos+1)
else:
    print("not found")