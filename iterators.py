""" nums=[7,8,9,5]

for i in nums:
    print(i)

it =iter(nums)

print(it.__next__())


print(next(it)) """


class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if  self.num<= 10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=TopTen()

print(next(values))#it prints 1

for  i in values:#it prints 2 to 10
    print(i)