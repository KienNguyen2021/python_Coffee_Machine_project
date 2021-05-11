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

profit =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """ Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients :
        if order_ingredients[item] >= resources[item]:
            print(f" Sorry ! there is not enough {item}.")

            return False

    return True

def process_coins():
    """ Return the total calculation from coins inserted."""
    print("Please insert coins :")
    total = int(input ("How many quarters ? : "))* 0.25
    total += int(input("How many dimes ? : ")) * 0.10
    total += int(input("How many nickles ? : ")) * 0.05
    total += int(input("How many pennies ? : ")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    # this function takes 2 input : money received and cost
    """ Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost :
        change = round(money_received - drink_cost, 2)  # takes 2 decimal number
        print(f" Here is ${change} ub change")
        global profit
        profit += drink_cost
        return True
    else :
        print("Sorry, that is not enough money . Money refunded.")
        return False


def make_coffee (drink_name, order_indredients) :
    """ Deduct the required ingredients from the resources."""
    for item in order_indredients :
        resources[item] -= order_indredients[item]
    print(f" Here is your {drink_name}🍔 Enjoy !")



is_on = True
while is_on :
    choice = input("what would you like (espressro/latte/cappuccino):? ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water :{resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}ml")
        print(f"Money : ${profit}")
    else :
        drink = MENU[choice]
          #print(drink) or :

        if is_resource_sufficient(drink["ingredients"]):   # Call the function is_resource_sufficient to pass ingredient

            payment = process_coins()       # function calling process_coin

            if is_transaction_successful(payment,drink["cost"]) :
            # Call the function successful, pass the payment and drink cost

                make_coffee(choice, drink["ingredients"])
