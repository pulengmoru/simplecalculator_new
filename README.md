# simplecalculator_new
# Calculator.py
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

# Test_calculator
from calculator import add


def test_add():
    results = add(1, 2)
    assert result == 3

from calculator import divide

def test_divide():
    results = divide(9, 3)
    assert result == 3


def test_divide_by_zero():
    results = divide(99, 0)
    assert type(result) == str

    from calculator import multiply


def test_multiply():
    results = multiply(6, 1)
    assert result == 6
    rint(result)

 from calculator import subtract


def test_subtract():
    result = subtract(5, 2)
    assert result == 3   