from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# work with the given documentation and don't change any other module

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    coffee_choice = input("What would you like? " + menu.get_items() + "\n")

    if coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    elif coffee_choice == "off":
        break

    menu_item = menu.find_drink(coffee_choice)

    if menu_item is not None:
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
                print("\n----------------------------------------------------\n")
