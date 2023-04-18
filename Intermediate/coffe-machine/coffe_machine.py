MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 250,
    "milk": 200,
    "coffee": 100,
}

money_in_machine = 0


def print_report():
    print("Current resources left:")
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f'Money: {money_in_machine}')

def check_resources(kind_of_coffe:str):
    for resource,ingredient in zip(resources.items(),MENU[kind_of_coffe]["ingredients"].values()):
        if resource[1] < ingredient:
            return False, resource[0]
    return True, None

def use_resources(kind_of_coffe:str):
    global resources
    global money_in_machine
    for resource,ingredient in zip(resources.items(),MENU[kind_of_coffe]["ingredients"].items()):
        resources[ingredient[0]]=resource[1]-ingredient[1]
    money_in_machine += MENU[kind_of_coffe]["cost"]
    

def check_credits(kind_of_coffe:str,quarters:int=0,dimes:int=0,nickel:int=0,pennies:int=0,):
    coffe_price = MENU[kind_of_coffe]["cost"]
    provided_cash = 0.25*quarters+0.1*dimes+0.05*nickel+0.01*pennies
    if coffe_price < provided_cash:
        rest = provided_cash - coffe_price
        return True,round(rest,2)
    return False,round(provided_cash,2)

def request_money():
    try:
        quarters = int(input("Insert quarters: "))
        dimes = int(input("Insert dimes: "))
        nickels = int(input("Insert nickels: "))
        pennies = int(input("Insert pennies: "))
    except:
        print("Wrong inputs, please try again.")
        request_money()
    else:
        return [quarters,dimes,nickels,pennies]

def preapare_coffe(kind_of_coffe:str):
    resource_ok,resource = check_resources(kind_of_coffe)
    if not(resource_ok):
        return print(f"Insufficient resources. There is not enough {resource}")
    received_cash = request_money()
    money_ok, rest = check_credits(kind_of_coffe,received_cash[0],received_cash[1],received_cash[2],received_cash[3])
    if not(money_ok):
        return print(f"Insufficient amount of money, returning cash ${rest}")
    use_resources(kind_of_coffe)
    print(f"Here is your {kind_of_coffe} and change ${rest}. Enjoy!")

def coffe_machine():
    while True:
        user_request = input("What would you want to order today? (espresso/latte/cappuccino): ")
        if user_request == "off":
            return print("Turning off the machine")
        elif user_request =="report":
            print_report()
        elif user_request in ["espresso","latte","cappuccino"]:
            preapare_coffe(user_request)
        else:
            print("Wrong input, choose between espresso/latte/cappuccino.")

coffe_machine()