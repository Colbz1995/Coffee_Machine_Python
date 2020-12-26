from os import system
from time import sleep

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0
amount = 0.0


def clear():
    system("clear")  # Linux - OSX
    system("cls")  # Windows - OSX


def process_coins(q, d, n, p) -> float:
    """
    Count how much money there are based on the coins passed in and return that amount.
    """
    # penny = 0.01
    # nickel = 0.05
    # dime = 0.1
    # quarter = 0.25

    return (0.25 * q) + (0.1 * d) + (0.05 * n) + (0.01 * p)


def report():
    """
    Print out the resources and the amount of money in the register
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(coffee) -> bool:
    can_make = True
    for resource in MENU[coffee]["ingredients"]:
        if resources[resource] < MENU[coffee]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}.")
            can_make = False

    return can_make


def make_coffee(coffee):
    for resource in MENU[coffee]["ingredients"]:
        resources[resource] -= MENU[coffee]['ingredients'][resource]


def process_change(spending_money, coffee):
    change = spending_money - MENU[coffee]["cost"]
    return spending_money - change


while True:
    customer_response = input("What would you like? (espresso/latte/cappuccino/report): ").lower()

    if customer_response == "espresso" and check_resources(customer_response):
        quarter = int(input("Quarters: "))
        dime = int(input("Dimes: "))
        nickel = int(input("Nickel: "))
        penny = int(input("Penny: "))

        amount = process_coins(quarter, dime, nickel, penny)

        if amount >= MENU[customer_response]["cost"]:
            make_coffee(customer_response)
            money += process_change(amount, customer_response)
            print(f"Here is your {customer_response}. Enjoy!")
            sleep(5)
            clear()
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif customer_response == "latte" and check_resources(customer_response):
        quarter = int(input("Quarters: "))
        dime = int(input("Dimes: "))
        nickel = int(input("Nickel: "))
        penny = int(input("Penny: "))

        amount = process_coins(quarter, dime, nickel, penny)

        if amount >= MENU[customer_response]["cost"]:
            make_coffee(customer_response)
            money += process_change(amount, customer_response)
            print(f"Here is your {customer_response}. Enjoy!")
            sleep(5)
            clear()
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif customer_response == "cappuccino" and check_resources(customer_response):
        quarter = int(input("Quarters: "))
        dime = int(input("Dimes: "))
        nickel = int(input("Nickel: "))
        penny = int(input("Penny: "))

        amount = process_coins(quarter, dime, nickel, penny)

        if amount >= MENU[customer_response]["cost"]:
            make_coffee(customer_response)
            money += process_change(amount, customer_response)
            print(f"Here is your {customer_response}. Enjoy!")
            sleep(5)
            clear()
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif customer_response == "report":
        report()
        sleep(5)
        clear()
    elif customer_response == "off":
        break
    else:
        sleep(5)
        clear()
        continue
