#name=input("enter your name: ")

#print(name)
""" x=int(input("enter the first number "))
y=float(input("enter the value of pi"))
z=x+y
print(z) """

"""
use of  index in order to get character 

 ch=input("enter a character")[5]
print(ch) """

"""
 result=eval(input("enter an expresssion" ))
ismein hmein int typecast krne ki jarurat nhi hain

print(result) 
print(type(result)) 
"""



import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=x+y
print(z)

""" 
#1 How to get user input
-- Getting user input in Python is straightforward. You can use the input() function 
to get input from the user. The input function takes a single argument, which is the 
prompt message displayed to the user.

e.g
name = input("Please enter your name: ")
x=input("Enter first number: ");
y=input("Enter second number: ");
z=x+y;
print(z);


#2 input function 
-- In Python, the input() function is used to accept user input from the command line or console.
name=input("Enter your name:");
print(name);
-- In this example, the input() function prompts the user to enter their name. Whatever the user types 
in response is stored in the name variable.
-- Note that the input() function always returns a string, so if we want to use the user's input as a number, 
we'll need to convert it using the appropriate type-casting function (e.g., int() for integers or float() for 
floating-point numbers).

#3 Types of input data
-- The input() function always returns a string, regardless of what the user enters. 
we may need to convert the input to a different data type if you want to perform calculations or other operations on it.

e.g
x=input("Enter first number: ");
a=int(x);
the input entered by the user is converted to an integer using the int() function in this example.

#4 when to use index value 
-- If you want to get a single character from the user, we can use the input() function and index the result.
e.g
ch=input('enter a character: ');
print(ch[0])

ch=input('enter a character: ')[0];
print(ch);

#5 eval function
eval function
-- The eval() function in Python is used to evaluate an expression entered by the user as a string. 
The eval() function returns the result of the expression as a value.

e.g
x=eval(input("Enter an expression: "));
typeOf = type(x);
print(typeOf);

#6
Passing values from command line
-- sys module provides access to any command-line arguments via the sys.argv list. 
we can pass arguments to a Python script from the command line using the sys.argv list. 
The first argument in the list is always the name of the script itself.

suppose we have a file named Mycode.py
in file we have written code
import sys  # without this line you will get error
x=sys.argv[1];
y=sys.argv[2];
z=x+y;
print(z);

in command line we have to run this file
#python3 Mycode.py 9 5
            0      1 2

Note: Mycode is count as 0th argument
      9 is count as 1st argument
      5 is count as 2nd argument """