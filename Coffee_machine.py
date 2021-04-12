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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

userinput = input("What would you like? (espresso/latte/cappuccino) ").lower()

if userinput == "report":
    for i in resources:
        print (i, resources[i])

elif userinput == "espresso":

    if MENU['espresso']['ingredients']['water'] > resources['water']:
        print("Sorry, but there is not enough water to make this.")
    elif MENU['espresso']['ingredients']['coffee'] > resources['coffee']:
        print("Sorry, but there is not enough coffee to make this.")
    elif MENU['espresso']['ingredients']['water'] < resources['water'] and MENU['espresso']['ingredients']['coffee'] < resources['coffee']:
        print(f"Espresso cost is ${MENU['espresso']['cost']}, please insert coins to pay | quarters, dimes, nickels, pennies. ")
        q = int(input("How many quarters? ")) * .25
        d = int(input("How many dimes? ")) * .1
        n = int(input("How many nickels? ")) * .05
        p = int(input("How many pennies? ")) * .01
        total_coins = q + d + n + p 
        if MENU['espresso']['cost'] > total_coins:
            print("Sorry, this is not enough money. Your money has been refunded")
        else:
            change = total_coins - MENU['espresso']['cost']
            resources['money'] = resources['money'] + MENU['espresso']['cost']
            print(f"Thank you for your purchase! your change is ${round(change, 2)}.")
        resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
        print(f"Your {userinput} is dispensing now!")
        print(f"Remaining resources: {resources}.")

elif userinput == "latte":

    if MENU['latte']['ingredients']['water'] > resources['water']:
        print("Sorry, but there is not enough water to make this.")
    elif MENU['latte']['ingredients']['coffee'] > resources['coffee']:
        print("Sorry, but there is not enough coffee to make this.")
    elif MENU['latte']['ingredients']['milk'] > resources['milk']:
        print("Sorry, but there is not enough milk to make this.")
    elif MENU['latte']['ingredients']['water'] < resources['water'] and MENU['latte']['ingredients']['coffee'] < resources['coffee'] and MENU['latte']['ingredients']['milk'] < resources['milk']:
        print(f"Latte cost is ${MENU['latte']['cost']}, please insert coins to pay | quarters, dimes, nickels, pennies. ")
        q = int(input("How many quarters? ")) * .25
        d = int(input("How many dimes? ")) * .1
        n = int(input("How many nickels? ")) * .05
        p = int(input("How many pennies? ")) * .01
        total_coins = q + d + n + p 
        if MENU['latte']['cost'] > total_coins:
            print("Sorry, this is not enough money. Your money has been refunded")
       
        elif MENU['latte']['cost'] < total_coins:
            change = total_coins - MENU['latte']['cost']
            resources['money'] = resources['money'] + MENU['latte']['cost']
            print(f"Thank you for your purchase! your change is ${round(change, 2)}.")
            resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
            resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
            resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
            print(f"Your {userinput} is dispensing now!")
            print(f"Remaining resources: {resources}.")

elif userinput == "cappuccino":

    if MENU['cappuccino']['ingredients']['water'] > resources['water']:
        print("Sorry, but there is not enough water to make this.")
    elif MENU['cappuccino']['ingredients']['coffee'] > resources['coffee']:
        print("Sorry, but there is not enough coffee to make this.")
    elif MENU['cappuccino']['ingredients']['milk'] > resources['milk']:
        print("Sorry, but there is not enough milk to make this.")
    elif MENU['cappuccino']['ingredients']['water'] < resources['water'] and MENU['cappuccino']['ingredients']['coffee'] < resources['coffee'] and MENU['cappuccino']['ingredients']['milk'] < resources['milk']:
        print(f"cappuccino cost is ${MENU['cappuccino']['cost']}, please insert coins to pay | quarters, dimes, nickels, pennies. ")
        q = int(input("How many quarters? ")) * .25
        d = int(input("How many dimes? ")) * .1
        n = int(input("How many nickels? ")) * .05
        p = int(input("How many pennies? ")) * .01
        total_coins = q + d + n + p 
        if MENU['cappuccino']['cost'] > total_coins:
            print("Sorry, this is not enough money. Your money has been refunded")
       
        elif MENU['cappuccino']['cost'] < total_coins:
            change = total_coins - MENU['cappuccino']['cost']
            resources['money'] = resources['money'] + MENU['cappuccino']['cost']
            print(f"Thank you for your purchase! your change is ${round(change, 2)}.")
            resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
            resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
            resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
            print(f"Your {userinput} is dispensing now!")
            print(f"Remaining resources: {resources}.")

elif userinput == "off":
    print("Thank you, goodbye.")
        
        

    