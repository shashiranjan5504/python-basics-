a=5
b=5
try:
    print("resources open")
    print(a/b)
    value=int(input("enter a number "))
    print(value)
except ValueError as e:
    print("inavlid input")
except Exception as e:
    print("hey you cant divide a number by zero ",e)

finally:
    print("resources closed")
print("bye")