#This is he actual program, use this one
#use sets
#TIP!!!!!
#If you right-click the Pseudocode file > Open to the side, it will show both this and the Pseudocode file at the same time!

#Variable for repeats
rept = 1


import random
#Schedule variables
tmes = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00"]
ven1 = ""
ven2 = ""
ven3 = ""
ven4 = ""

# function to manaage tickets and attendees
def ticket_attendee():
    price_one = 100
    price_three = 250
    price_vip = 450
    attendees = []
    while True:
        choice = input("""1. see ticket prices
2. adjust ticket prices
3. add attendee information
4. see attendee information
5. End
Enter the number of the thing you would like to do: """)
        if choice == "1":
            print("the price for a 1-day pass is $", price_one, ", the price for a 3-day pass is $", price_three, ", the price for a VIP pass is $", price_vip)
        elif choice == "2":
            price_one = float(input("what should the 1-day pass cost: "))
            price_three = float(input("what should the 3-day pass cost: "))
            price_vip = float(input("what should the VIP pass cost: "))
        elif choice == "3":
            name = input("enter the name of the attendee: ")
            age = input("enter the age of the attendee: ")
            ticket_type = input("""1. 1-day pass
2. 3-day pass
3. VIP pass
Enter the number of the type of ticket the attendee bought: """)
            if ticket_type == "1":
                ticket_type = "1-day pass"
            elif ticket_type == "2":
                ticket_type = "3-day pass"
            elif ticket_type == "3":
                ticket_type = "VIP pass"
            else:
                print("That is not an option.")
                continue
            attendee = (name, age, ticket_type)
            attendees.append(attendee)
        elif choice == "4":
            for p in range(len(attendees)):
                print(attendees[p])
        elif choice == "5":
            break
        else:
            print("That is not an option.")
            continue


def artists(rept, artist_list): #lists
    #list format: name,genre
    try:
        choice=int(input("""Press the number of what you want:
        1. Add an artist
        2. Remove an artist
        3. Edit artists
        4. See artists
        5. Exit
"""))
        if choice==1:#add
            artist=input("Artist Name?\n    ")
            genre=input("Genre of the artist?\n    ")
            ven=input("Venu performing at?\n    ")
            artist_list.append([artist,genre, ven])
            rept = 1
            return rept, artist_list
            
        elif choice==2: #remove
            try:
                index=int(input("""     1. Use the number of the artist in the list
        2. Use the name and genre\n    """))
                if index==1: #index remove
                    try:
                        index=int(input("What is the number of the artist?\n    "))
                        if index<len(artist_list):
                            artist_list.remove(artist_list[index-1])
                            rept = 1
                            return rept, artist_list
                        else:
                            rept = 1
                            return rept, artist_list
                    except:
                        rept = 1
                        return rept, artist_list
                elif index==2: #name remove
                    artist=input("Artist Name?\n    ")
                    genre=input("Genre of the artist\n    ")
                    if [artist,genre] in artist_list:
                        artist_list.remove([artist,genre])
                        rept = 1
                        return rept, artist_list
                    else:
                        rept = 1
                        return rept, artist_list
                else:
                    rept = 1
                    return rept, artist_list
            except:
                rept = 1
                return rept, artist_list
    
        elif choice==3: #Edit Artists
            try:
                index=int(input("""     1. Use the number of the artist in the list
        2. Use the name and genre\n    """))
                if index==1: #index remove
                    try:
                        index=int(input("What is the number of the artist?\n    "))
                        if index<len(artist_list):
                            artist_list.remove(artist_list[index-1])
                        else:
                            rept = 1
                            return rept, artist_list
                    except:
                        rept = 1
                        return rept, artist_list
                elif index==2: #name remove
                    artist=input("Artist Name?\n    ")
                    genre=input("Genre of the artist?\n    ")
                    index=artist_list.index([artist,genre])
                    if [artist,genre] in artist_list:
                        artist_list.remove([artist,genre])
                        rept = 1
                        return rept, artist_list
                    else:
                        rept = 1
                        return rept, artist_list
            except:
                rept = 1
                return rept, artist_list
            #new artist
            artist=input("New artist name?\n    ")
            genre=input("Genre of the New artist?\n    ")
            artist_list.insert(index,[artist,genre])
            rept = 1
            return rept, artist_list
            
        elif choice==4: #See artists
            for x in artist_list:
                print(f"{artist_list.index(x)}: {x[0]}, {x[1]}")
                rept = 1
                return rept, artist_list
        
        elif choice==5: #Exit
            rept = 1
            return rept, artist_list
    
    except:
        rept = 1
        return rept, artist_list



#The randomised still broken
def schedule(tmes, ven1, ven2, ven3, ven4, rept, artist_list):
    ans = int(input('''What would you like to do?
        1 Randomise scehdule
        2 Remove artist from schedule
        3 Add artist to empty slot
        4 For end
'''))
    if ans == 1:
        #This will add times and sechdule timing to a venu slot
        lst = []
        lst1 = []
        ans = input("What venu would you like to make the schedule for?\n   ")
        count = 0
        countlst = len(tmes)
        for x in artist_list:
            if ans in x:
                lst.append(x)
                count += 1
            else:
                pass
        if count > countlst:
            return ven1, ven2, ven3, ven4, rept, ("The amount of artists is too much for the amount of time slots")
        else:
            lst3 = lst[:]
            random.shuffle(lst3)
            lst = lst3
            for x in lst:
                for i in tmes:
                    lst1 = lst1.append(i + x)
            print(f"Venu #1:\n{ven1}\nVenu #2:\n{ven2}\nVenu #3:\n{ven3}\nVenu #4:\n{ven4}\n")
            ans = int(input("Which venu SLOT do you want to save this schedule to? (5 for none)\n    "))
            if ans == 1:
                ven1 = tuple(lst1)
            elif ans == 2:
                ven2 = tuple(lst1)
            elif ans == 3:
                ven3 = tuple(lst1)
            elif ans == 4:
                ven4 = tuple(lst1)
            else:
                print("Not saved to a slot")
            return ven1, ven2, ven3, ven4, rept
    elif ans == 2:
        #This is to delete a time slot, need to work on making the times back into the list
        #Fix is the list that will be saved to the venu
        ask = int(input("What venu slot would you like to access? (1-4)\n   "))
        if ask == 1:
            fix = list(ven1)
            print(fix)
            ans = input("What item would you like to remove? (Don't do times, only the artist)\n  ")
            if ans in fix:
                fix = fix.remove(ans)
                pass
            else:
                print("Error removing")
                pass
            ven1 = tuple(fix)
            pass
        elif ask == 2:
            fix = list(ven2)
            print(fix)
            ans = input("What item would you like to remove? (Don't do times, only the artist)\n  ")
            if ans in fix:
                fix = fix.remove(ans)
                pass
            else:
                print("Error removing")
                pass
            ven2 = tuple(fix)
            pass
        elif ask == 3:
            fix = list(ven3)
            print(fix)
            ans = input("What item would you like to remove? (Don't do times, only the artist)\n    ")
            if ans in fix:
                fix = fix.remove(ans)
                pass
            else:
                print("Error removing")
                pass
            ven3 = tuple(fix)
            pass
        elif ask == 4:
            fix = list(ven4)
            print(fix)
            ans = input("What item would you like to remove? (Don't do times, only the artist)\n    ")
            if ans in fix:
                fix = fix.remove(ans)
                pass
            else:
                print("Error removing")
                pass
            ven4 = tuple(fix)
            pass
        else:
            print("Not an available slot")
        return ven1, ven2, ven3, ven4, rept
    #This is the adding function, need to fix the slot they need to add to
    elif ans == 3:
        ask = int(input("What venu slot would you like to access? (1-4)\n   "))
        if ask == 1:
            fix = list(ven1)
            print(fix)
            ask = input("What time would you like to add this to?\n    ")
            ans = input("What would you like to add?\n    ")
            for x in fix:
                if ask in fix[x]:
                    fix = fix[x].append(ans)
                    pass
            ven1 = tuple(fix)
            return ven1, ven2, ven3, ven4, rept
        elif ask == 2:
            fix = list(ven2)
            print(fix)
            ask = input("What time would you like to add this to?\n    ")
            ans = input("What would you like to add?\n    ")
            for x in fix:
                if ask in fix[x]:
                    fix = fix[x].append(ans)
                    pass
            ven2 = tuple(fix)
            return ven1, ven2, ven3, ven4, rept
        elif ask == 3:
            fix = list(ven3)
            print(fix)
            ask = input("What time would you like to add this to?\n    ")
            ans = input("What would you like to add?\n    ")
            for x in fix:
                if ask in fix[x]:
                    fix = fix[x].append(ans)
                    pass
            ven3 = tuple(fix)
            return ven1, ven2, ven3, ven4, rept
        elif ask == 4:
            fix = list(ven4)
            print(fix)
            ask = input("What time would you like to add this to?\n    ")
            ans = input("What would you like to add?\n    ")
            for x in fix:
                if ask in fix[x]:
                    fix = fix[x].append(ans)
                    pass
            ven4 = tuple(fix)
            return ven1, ven2, ven3, ven4, rept
        else:
            return ven1, ven2, ven3, ven4, rept, ("Invalid input!")


def search(rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus):
    ans = int(input('''What would you like to do?
        1 for attendees
        2 for venu
        3 for artists
        4 for schedule
        5 for end
'''))
    #Searches for attendee by name
    if ans == 1:
        atnd = input("What is the attendee name?\n")
        if atnd in attendees:
            print(f"{atnd} is in the list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
        else:
            print(f"{atnd} not in the list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
    #Searches for venu by name of venu
    elif ans == 2:
        ven = input("What is the name of the venu?\n")
        if ven in venus:
            print(f"{ven} in the list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
        else:
            print(f"{ven} not in the list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
    #Searches for artist by name
    elif ans == 3:
        art = input("What is the artist's name?\n")
        if art in artist_list:
            print(f"{art} in the list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
        else:
            print(f"{art} not in list!")
            rept = 1
            return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
    #Prints the schedule
    elif ans == 4:
        ans = int(input("What slot of venu schedule would you like to access? (1-4)\n    "))
        if ans == 1:
            print(ven1)
            pass
        elif ans == 2:
            print(ven2)
            pass
        elif ans == 3:
            print(ven3)
            pass
        elif ans == 4:
            print(ven4)
            pass
        else:
            print("Invalid input!")
            pass
        rept = 1
        return rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus
    #Ends the function and returns to menu
    else:
        rept = 1
        return rept



def main(rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus, price_one, price_three, price_vip, tmes):
    while rept > 0:
        choice = input("""        1. Artist Management
        2. Schedule Management
        3. Venue Management
        4. Ticket Sales and Attendee Management
        5. Search
        6. End
        Enter the number of the thing you would like to do:
""")
        if choice == "1":
            rept, artist_list = artists(rept, artist_list)
        elif choice == "2":
            tmes, ven1, ven2, ven3, ven4, rept, artist_list = schedule(tmes, ven1, ven2, ven3, ven4, rept, artist_list)
        elif choice == "3":
            rept, venus = venu((int(input("How many venus would you like to make?\n    "))), venus, rept)
        elif choice == "4":
            attendees, rept, price_one, price_vip, price_three = ticket_attendee(attendees, rept, price_one, price_vip, price_three)
        elif choice == "5":
            rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus = search(rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus)
        else:
            rept = 0
    return rept

# loop that makes sure the program continues until the user is done
while rept > 0:
    print("Music Festival Manager")
    rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus, price_one, price_three, price_vip = main(rept, artist_list, ven1, ven2, ven3, ven4, attendees, venus, price_one, price_three, price_vip, tmes)
print("Thank you for using this program.")