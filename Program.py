done = False
milkshake_menu = ["Chocolate", "Vanilla", "Strawberry"]
ice_cream_flavors_menu = ["Chocolate", "Vanilla", "Strawberry", "Rocky Road"]
sundaes_menu = ["Classic", "Banana Split"]

def ice_cream_flavor_menu():
    sizes = {"Small": 4.00, "Medium": 5.50, "Large": 6.25}
    print()
    print("====Ice Cream Menu====")
    for x in sizes:
        print("-",x.title(),sizes[x])
        choice = input("Choice >>  ").lower()
        def items():
            def cost():
                    if choice in sizes:
                            items.append(choice)
                            cost.append(sizes[choice])
                    print("You've got it!")

    else:
            toppings_menu = ["Sprinkles", "Fudge", "Cherry"]
            print("Invalid Choice")
            toppings = input("Do you want some toppings?(Yes/No)>> ").lower()
            if toppings == "yes":
                toppings_menu()
            else:
                        print("Okay got you!")
def checkout():
    def cost():
        print("==== Check Out ====")
    subtotal = sum(cost)
    print("Subtotal:", subtotal)
    def coupon():
        choice = input("Do you have any coupons? (Yes/No)>> ")
        if choice == "Yes":
            coupon(subtotal)
        def tax():
            final = tax(subtotal)
            print(">> Final Bill:")
            def items():
                for i in items:
                    print("-",i)
                    print("-------------------")
                    print("Final Price ${:.2f}".format(final))
                    print("Thank you for coming to Scoops of Joy!")
                    print("Have a good day!")





print("Welcome to Scoops of Joy")


while not done:
    item_x = 0
    item_choice = -1

    print()
    print("Our Menu")
    print("What would you like?")
    print("M - Milkshakes")
    print("I - Ice cream flavors")
    print("S - Sundaes")
    print("C - Checkout")
    choice = input("Choice >> ")
    print()

    if choice.upper().strip() == "M":
        for item in milkshake_menu:
            item_x += 1
            print(f"{item_x}: {item}")

    if choice.upper().strip() == "I":
        for item in ice_cream_flavors_menu:
            item_x += 2
            print(f"{item_x}: {item}")

        if choice.upper().strip() == "S":
            for item in sundaes_menu:
                item_x += 3
                print(f"{item_x}: {item}")

        item_choice = int(input("Which would you like?: "))

    elif choice == "C":
        checkout()
        done = True
