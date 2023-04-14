

def addition(number_1,number_2):
    return number_1+number_2
def subtraction(number_1,number_2):
    return number_1-number_2
def multiplication(number_1,number_2):
    return number_1*number_2
def division(number_1,number_2):
    return number_1/number_2

operations = {
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division
}

user_exit = "n"


print("Welcome to the calculator")


def calculator():
    first_number = float(input("Enter the first number: \n"))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operator = input ("What is the operation you want ot perform: ")
        second_number = float(input("Enter the second number: \n "))
        result = operations[operator](first_number,second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        if operator in ["/","*"] and (second_number== 0 or first_number == 0):
            print("These operations are forbidden, no multiplication or division by 0")
            calculator()
        if input("Do you want to continue with the calculated result? Y/N ").lower() == "y":
            first_number = result
        else:
            calculator()

calculator()

