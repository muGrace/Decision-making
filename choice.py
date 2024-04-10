#choosing from a list
x=float(input("Enter a number :\n"))
y=float(input("Enter a second number :\n"))
print("1) add the two numbers ")
print("2) substract the two numbers ")
print("3) multiply the two numbers ")
print("4) divide the two numbers ")

choice=int(input("enter your choice:\n"))
print("The answer is: ",end="")
if choice == 1:
    print(x + y)
elif choice == 2:
    print( x-y)
elif choice == 3:
    print( x*y)
elif choice ==4:
    print(x/y)

else:
    print("invalid choice")
   
