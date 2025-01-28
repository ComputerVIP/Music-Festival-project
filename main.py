# Eli Robison, Ticket Sales and Attendee Management

"""
Ticket Sales and Attendee Management
    Store and manage large numbers of ticket sales
    Track different ticket types (e.g., 1-day, 3-day, VIP)
    Store attendee information
"""

def ticket_attendee():
    price_one = 100
    price_three = 250
    price_vip = 450
    attendees = []
    while True:
        choice = input("""1. see ticket prices
                       2. buy a ticket
                       3. adjust ticket prices
                       4. attendee information
                       5. End
                       Enter the number of the thing you would like to do: """)
        if choice == "1":
            print("the price for a 1-day pass is $", price_one, ", the price for a 3-day pass is $", price_three, ", the price for a VIP pass is $", price_vip)
        elif choice == "2":
            amount = int(input("How many tickets do you want to buy: "))
            type = input("""1. 1-day pass
                         2. 3-day pass
                         3. VIP pass
                         Enter the number of the type of pass you would like to buy: """)
            if type == "1":
                cost = amount * price_one
            elif type == "2":
                cost = amount * price_three
            elif type == "3":
                cost = amount * price_vip
            else:
                print("That is not an option.")
            print("the cost will be", cost)
        elif choice == "3":
            
        elif choice == "4":
            
        elif choice == "5":
            break
        else:
            print("That is not an option.")