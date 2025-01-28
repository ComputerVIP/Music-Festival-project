# function with the main user interface
def main():
    choice = input("""1. Artist Management
    2. Schedule Management
    3. Venue Management
    4. Ticket Sales and Attendee Management
    5. Search
    6. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        artists()
    elif choice == "2":
        schedule()
    elif choice == "3":
        venue()
    elif choice == "4":
        ticket_&_attende()
    elif choice == "5":
        search()
    elif choice == "6":
        return "end"
    else:
        print("That is not an option.")

# loop that makes sure the program continues until the user is done
while True:
    print("Music Festival Manager")
    end = main()
    if end == "end":
        print("Thank you for using this program.")
        break