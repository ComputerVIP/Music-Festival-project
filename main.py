#This is he actual program, use this one

#TIP!!!!!
#If you right-click the Pseudocode file > Open to the side, it will show both this and the Pseudocode file at the same time!

import random

#Schedule variables
tmes = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00"]
ven1 = ""
ven2 = ""
ven3 = ""
ven4 = ""

def ticket_attendee():
    price_one = 100
    price_three = 250
    price_vip = 450
    attendees = []
    while True:
        choice = input("""1. see ticket prices
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
                continue
            print("the cost will be", cost)
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            print("That is not an option.")

def schedule(tmes, ven1, ven2, ven3, ven4, *insert variables here* ):
    ans = int(input("What would you like to do?\n1 Randomise scehdule\n2 Remove artist from schedule\n3 Add artist to empty slot\n4 For end\n    "))
    if ans == 1:
        lst = []
        lst1 = []
        cnt = 0
        ans = input("What venu would you like to make the schedule for?\n   ")
        for x in *list of artists*:
            if *list of artists*[cnt] contains ans:
                lst.append(*list of artists*[cnt])
                cnt += 1
                count = len( *artist list of that venu* )
                countlst = len(tmes)
            else:
                pass
        cnt = 0
        if count > countlst:
            return *insert variables here*, ("The amount of artists is too much for the amount of time slots")
        else:
            for x in lst:
                lst1 = lst1.append(tmes[random.randint(0,(len(tmes)-1))] + lst[random.randint(0,(len(lst)-1))])
            print(f"Venu #1:\n{ven1}\nVenu #2:\n{ven2}\nVenu #3:\n{ven3}\nVenu #4:\n{ven4}\n")
            ans = int(input("Which venu SLOT do you want to save this schedule to? (5 for none)\n    "))
            if ans == 1:
                ven1 = tuple(lst1)
                return ven1, ven2, ven3, ven4, *insert variables here*
            elif ans == 2:
                ven2 = tuple(lst1)
                return ven1, ven2, ven3, ven4, *insert variables here*
            elif ans == 3:
                ven3 = tuple(lst1)
                return ven1, ven2, ven3, ven4, *insert variables here*
            elif ans == 4:
                ven4 = tuple(lst1)
                return ven1, ven2, ven3, ven4, *insert variables here*
            else:
                return ven1, ven2, ven3, ven4, *insert variables here*





def search( *insert variables here* ):
    ans = int(input("What would you like to do?\n 1 for attendees\n 2 for venu\n 3 for artists\n 4 for schedule\n 5 for end\n   "))
    #Searches for attendee by name
    if ans == 1:
        atnd = input("What is the attendee name?\n")
        if atnd in *insert attendee list*:
            print(f"{atnd} is in the list!")
            return *insert variables here*
        else:
            print(f"{atnd} not in the list!")
            return *insert variables here*
    #Searches for venu by name of venu
    elif ans == 2:
        ven = input("What is the name of the venu?\n")
        if ven in *insert venu list*:
            print( *venu info* )
            return *insert variables here*
        else:
            print(f"{ven} not in the list!")
            return *insert variables here*
    #Searches for artist by name
    elif ans == 3:
        art = input("What is the artist's name?\n")
        if art in *insert artist list here*:
            print(f"{art} in the list!")
            return *insert variables here*
        else:
            print(f"{art} not in list!")
            return *insert variables here*
    #Prints the schedule
    elif ans == 4:
        print( *insert schedule name here* )
        return *insert variables here*
    #Ends the function and returns to menu
    else:
        return *insert variables here*