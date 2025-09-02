def count(nums):
    even =0
    odd=0
    for i in nums:
        
        if i%2==0 :
            even+=1
        else:
            odd+=1
    return even,odd




nums=[]
count1=int(input("enter the number of values which has to be inserted in list"))
for i in range(count1):
    
    x=int(input("enter the next  number "))
    nums.insert(i,x)

print(nums)


even,odd=count(nums)
print("even : {} and odd : {}".format(even,odd))

