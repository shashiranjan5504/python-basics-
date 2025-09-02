def fib(n):
    if n<0:
        print("inavlid input")
    else:
        a=0
        b=1
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(n-2):
                c=a+b
                print(c)
                a=b
                b=c


fib(int(input("enter the length of fibonacci series")))
