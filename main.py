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

def artists(): #lists
    #list format: name,genre
    exit==False
    while exit==False:
        artists_list=[["George","Metal"],["Henry","Metal"]]
        choice=int(input("""Press the number of what you want:
                     1. Add an artist
                     2. Remove an artist
                     3. Edit artists
                     4. See artists
                     5. Exit"""))
        if choice==1:#add
            artist=input("Artist Name")
            genre=input("Genre of the artist")
            artists_list.append([artist,genre])
        elif choice==2: #remove
            artist=input("Artist Name")
            genre=input("Genre of the artist")
            artists_list.remove([artist,genre])
        elif choice==3: #Edit Artists
            artist=input("Artist Name")
            genre=input("Genre of the artist")
            artists_list.remove([artist,genre])
            artist=input("Artist Name")
            genre=input("Genre of the artist")
            artists_list.append([artist,genre])
        elif choice==3: #See artists
            for x in artists_list:
                print(f"{x}: {artists_list[x]}")
        elif choice==4:
            print("invalid choice")
        elif choice==5:
            break
        else:
           print("Invalid choice")

artists()
'''
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
'''

'''
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
        art = input("What is the artists name?\n")
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
'''
