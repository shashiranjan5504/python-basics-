def is_even(n):
     return n%2==0


nums=[3,2,6,8,4,6,2,9]


#evens=list(filter(is_even,nums))  
""" instead of this we can write direct without the function declration """
evens=list(filter(lambda n:n%2==0,nums))


print(evens)