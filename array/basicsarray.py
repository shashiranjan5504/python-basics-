from array import *
vals=array('i',[5,6,-8,9,2])


# array ke values print karne ke tarike 
""" method 1
for i in range(len(vals)):
    print(vals[i]) """
""" method 2
for num in vals:
    print(num) """

"""method 3
 i=0
while (i<len(vals)):
    print(vals[i])
    i=i+1 """
#complete array ko print karana hai toh 
print(vals)
newarray=array(vals.typecode,(a for a in  vals))
for e in newarray:
    print(e)

