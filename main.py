#This is he actual program, use this one

#TIP!!!!!
#If you right-click the Pseudocode file > Open to the side, it will show both this and the Pseudocode file at the same time!



def search():
    ans = int(input("What would you like to do?\n 1 for attendees\n 2 for venu\n 3 for artists\n 4 for schedule\n 5 for end\n"))
    if ans == 1:
        atnd = input("What is the attendee name?\n")
        if atnd in "insert attendee list":
            print(f"{atnd} is in the list!")
            return "insert variables here"
        else:
            print(f"{atnd} not in the list!")
            return "insert variables here"
    elif ans == 2:
        ven = input("What is the name of the venu?\n")
        if ven in "insert venu list":
            print( "venu info" )
            return "insert variables here"
        else:
            print(f"{ven} not in the list!")
            return "insert variables here"
    elif ans == 3:
        art = input("What is the artist's name?\n")
        if art in "insert artist list here":
            print(f"{art} in the list!")
            return "insert variables here"
        else:
            print(f"{art} not in list!")
            return "insert variables here"
    elif ans == 4:
        print( "insert schedule name here" )
        return "insert variables here"
    else:
        return "insert variables here"

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
    end = main()
    if end == "end":
        print("Thank you for using this program.")
        break