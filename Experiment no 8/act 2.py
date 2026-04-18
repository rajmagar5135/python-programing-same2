To demonstrate exception handling by handling ZeroDivisionError exceptions
Created on Tue Mar 31 21:52:30 2026



@author : Raj Magar
try:
age = int(input("Enter your age: "))
if age <= 0:
print("Invalid age! Age must be positive.")



elif age < 18:



print("You are not eligible for registration.")
else:
print("Registration successful!")
except ValueError:

Type "copyright", "credits" or "license" for more information.

print("Invalid input! Please enter a valid number.")
