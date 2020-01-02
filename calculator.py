1. add
2. subtract
3. multiply
4. divide

print("Select an peration to perform")
print("1. add")
print("2. subtract")
print("3. multipy")
print("4. divide")

operation = input()

if operation == "1":
    num1 = input("enter first number")
    num2 = input("enter second number")
    print("the sum is" + str(int(num1) + int(num2)))
    #addition
elif operation == "2":
    num1 = input("enter first number")
    num2 = input("enter second number")
    print("the sum is" + str(int(num1) - int(num2)))
    #subtract
elif operation == "3":
    num1 = input("enter first number")
    num2 = input("enter second number")
    print("the sum is" + str(int(num1) * int(num2)))
    #multiply
elif operation == "4":
    num1 = input("enter first number")
    num2 = input("enter second number")
    print("the sum is" + str(int(num1) / int(num2)))
    #divide
else:
    print("invalid entry")


