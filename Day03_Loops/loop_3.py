# Program to take a number from the user and display its multiplication table using a loop

num=int(input("Enter the number: "))
for i in range (1, 11):
    print(num, "x", i, "=", num*i )
