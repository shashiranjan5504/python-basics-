a=5
b=0
try:
    print("resources open")
    print(a/b)
    value=int(input("enter a number "))
    print(value)
except ValueError as e:
    print("inavlid input")
except ZeroDivisionError :
    print("a number cannot divide by zero")
except Exception as e:
    print("....something went wrong..... ")

finally:
    print("resources closed")
print("bye")