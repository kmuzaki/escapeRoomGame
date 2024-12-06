import time #Importing the time library for text delays
import colorama #Importing colorama library. **Need to install first by type in "pip install colorama" command in the terminal
from colorama import Fore, Back, Style #Importing specific functions from said colorama library
colorama.init(autoreset=True) #Initialise the colorama library with Autoreset colour style enabled
import pprint #Importing pprint library to be able to print each items in the inventory 

class inventory:
    items = {}
    def checkItems():
        if len(inventory.items) != 0:
            print(Fore.LIGHTGREEN_EX + "\nHere are your current items:")
            pprint.pprint(inventory.items)
            print("\n")
            time.sleep(1)
        else:
            print(Fore.LIGHTGREEN_EX + "You currently don't have any items\n")
            time.sleep(1)


class prologue:
    escape = False
    def table():
        print("\nYou walked to the table and you see a 'picture' frame, a 'paper bag', and a 'note'. Which do you want to investigate?")
        while True:
            try:
                cTable = str(input("Enter selection. Type 'back' if you're done investigating: "))
            except ValueError:
                print("Wrong Input! Try Again\n")
                continue
            
            #Choice conditions
            cTable = str.lower(cTable)
            if cTable == "picture":
                print("It's a picture of a young girl with her two parents behind her. The girl appeared to be 7 to 9 years old.\n")
                time.sleep(1)
            elif cTable == "paper bag":
                print("You look into the bag, and it's empty. Welp.\n")
                time.sleep(1)
            elif cTable == "note":
                tNote = "I didn't know how it got worse from here. I thought we could get out of this place, but I failed you. I failed all of us. I'm sorry, Lisa."
                print(f"The note yreads:"+ "\n\x1B[3m" + Fore.YELLOW + tNote + "\x1B[0m\n")
            elif cTable == "back":
                print("You go back explore other parts of the room\n")
                time.sleep(1)
                break
            else:
                print("Wrong Input! Try Again\n")
            
        
    def intro(): #A prologue to thge story of the game
        print("You look around and you appears to be in a dimly lit room surrounded with gloomy walls that looks to be cracked at some points. You also hear some water dripping from the roof,\nand some water dips onto your head. You see an iron key that is slightly rusty around the edges.")
        print("You also see a note on the floor. The note reads: \n")
        time.sleep(1) #For every 'time.sleep' line, the text will delay
        note = "Hello. I realise that this may not be the most convenient position for you. You are choosen to be a part of my little game! Isn't it fun? There are 3 rooms you need to escape from. \nFind the key in each rooms and then you'll win! Of course, it would be child's play if there aren't any 'challenges'. Pick up the key in front of you and start escaping. Good luck."
        print(f"\x1B[3m" + Fore.YELLOW + note + "\x1B[0m\n") #Printing the variable "note" in italic

    def startGameChoice(): #Basically the start button for the game
        while True:
            #Try and except for error handling
            try:
                start = str(input("Pick up the key? (Y/N)"))
            except ValueError:
                print("Wrong Input! Try Again\n")
                continue
            
            #Choice conditions
            start = str.lower(start)
            if start == "n":
                print(f"You decided not to pick up the key, thinking that everything is all a dream")
                time.sleep(1)
                print("You decided to wait and closed your eyes until you wake up...")
                time.sleep(1)
                print("You thought to yourself that it will be over soon. Aaaand....")
                time.sleep(2)
                print("You opened your eyes-")
                print(Fore.CYAN + "GAME ENDED")
                print(Fore.CYAN +"----------")
                {time.sleep(1)}
                print(Fore.CYAN +"**You got 'The Coward Ending'.**")
                quit()
            
            elif start == "y":
                print("Filled with determination, you picked up the key.")
                inventory.items["rusty key"] = "A Rusty key. Feels rough but still sturdy" #Add the key to inventory
                print(Fore.LIGHTGREEN_EX +"**YOU GOT A 'rusty key'!**")
                time.sleep(1)
                print("You stand up and can now look around\n")
                break

            else:
                print("Wrong Input! Try Again\n")
    
    def room0Menu():
        print(Fore.CYAN +"**To interact in this game. You need to type the key words that are in a apostrophe marks (or '') to interact with certain objects.**")
        time.sleep(1)
        print(Fore.CYAN +"**For example, you want to investigate 'note'. Notice the word note are in apostrophe marks. Hence you need to type 'note' to interact said object.**\n")
        time.sleep(3)
        while True:
            print("You look around you, and you see a spruce planks 'door' and a 'wooden table' with some things on it. Which would you like to interact first?")
            time.sleep(1)
            try:
                choice = str(input("Enter selection. Type 'inventory' to see what items you have at your disposal: "))
            except ValueError:
                print("Wrong Input! Try Again\n")
                continue
                
            #Choice conditions
            choice = str.lower(choice)
            if choice == "wooden table" or choice == "table":
                prologue.table()
                
            elif choice == "door":
                print("You walk to the door, and then you insert the rusty key")
                time.sleep(1)
                print(Fore.YELLOW +"*Click!*")
                inventory.items.pop('rusty key')
                time.sleep(1.5)
                print("The key fits! You opened the door and walked in. A bright light flashed upon you.\n")
                time.sleep(3)
                prologue.escape = True
                break
            
            elif choice == "inventory":
                inventory.checkItems()

            else:
                print("Wrong Input! Try Again\n")


class room1:
    escape = False
    bShelf = False
    vaultStatus = False
    tableLampShelf = False

    def comfyRedSofa():
        print("It's a comfortable red sofa. You tried to sit on it.")
        time.sleep(1)
        print("It's comfortable alright. So much so that you relaxed for a moment, and almost wanted to sleep.")
        time.sleep(1)
        print("Apart from that, there's nothing of interest to check on the sofa. There's nothing under the sofa either. So you go back explore other parts of the room\n")
        time.sleep(0.5)

    def gramophone():
        print("It's a vintage gramophone. Reminded you of the good ol' days. There appears to be something inside the gramophone.")
        while True:
            #Try and except for error handling
            try:
                cGramo = str(input("Take a look inside? (Y/N)"))
            except ValueError:
                print("Wrong Input! Try Again\n")
                continue
            
            cGramo = str.lower(cGramo)
            if cGramo == "y":
                print("You take a look inside...")
                time.sleep(1)
                print("It's just some dust bunnies.")
                time.sleep(1.5)
                print("You go back explore other parts of the room\n")
                break

            elif cGramo == "n":
                print("You go back explore other parts of the room\n")
                break

            else:
                print("Wrong Input! Try Again\n")

    def bookshelf():
        bShelfFalse = "It's a wooden bookshelf. Filled with numerous books regarding a variety of topics. There appears to be something in-between some of the books..."
        bShelfTrue = "It's a wooden bookshelf. Filled with numerous books regarding a variety of topics. There's nothing of interest anymore."
        if room1.bShelf == True:
            print(bShelfTrue)
            time.sleep(1)
            print("So you go back explore other parts of the room\n")
        else:
            print(bShelfFalse)
            while True:
                #Try and except for error handling
                try:
                    cBShelf = str(input("Check between the books? (Y/N)"))
                except ValueError:
                    print("Wrong Input! Try Again\n")
                    continue
                
                cBShelf = str.lower(cBShelf)
                if cBShelf == "y":
                    print("You take a look inside...")
                    time.sleep(1)
                    print("You find a flathead screwdriver")
                    inventory.items["flathead screwdriver"] = "It has a smooth wooden handle on it. Feels high quality when you hold it." #Add the key to inventory
                    print(Fore.LIGHTGREEN_EX +"**YOU GOT A 'flathead screwdriver'!**")
                    time.sleep(1.5)
                    print("You go back explore other parts of the room\n")
                    room1.bShelf = True
                    break

                elif cBShelf == "n":
                    print("You go back explore other parts of the room\n")
                    break

                else:
                    print("Wrong Input! Try Again\n")

    def vault():
        vaultFalse = "It's a stainless steel vault. It appears to be locked behind a grate. You might need to use something to open the screws."
        vaultTrue = "It's a stainless steel vault. It's already opened though. So there's nothing of interest anymore."
        if room1.vaultStatus == True:
            print(vaultTrue)
            time.sleep(1)
            print("So you go back explore other parts of the room\n")
        else:
            print(vaultFalse)
            time.sleep(1)
            if 'flathead screwdriver' in inventory.items:
                print("You have the right tool for the job!")
                print(Fore.LIGHTGREEN_EX +"**Used the 'flathead screwdriver**")
                time.sleep(2)
                room1.vaultStatus = True
                print("You take the grate off, and then you turn the valve to open the vault...")
                time.sleep(1)
                print(Fore.LIGHTGREEN_EX +"**YOU GOT A 'shelf handle**")
                inventory.items["shelf handle"] = "Just a gold-plated handle for a shelf. Looks like you could attach it to something"
                print("You go back explore other parts of the room\n")

            else:
                print("It appears you don't have anything to open the screws.")
                time.sleep(1)
                print("So go back explore other parts of the room\n")

    def tableLamp():
        tLampFalse = "It's a table lamp. Though... it has a shelf under it, but there doesn't seem to be any handle to open it."
        tLampTrue = "It's a table lamp. Nothing of interest anymore"
        if room1.tableLampShelf == True:
            print(tLampTrue)
            time.sleep(1)
            print("So you go back explore other parts of the room\n")
        else:
            print(f"{tLampFalse}\n")
            time.sleep(1)
            if 'shelf handle' in inventory.items:
                print("Looks like you have the correct handle. You try to attach the handle...")
                print(Fore.LIGHTGREEN_EX +"**Used the 'shelf handle'**")
                inventory.items.pop('shelf handle')
                time.sleep(2)
                room1.tableLampShelf = True
                print("It fits!")
                time.sleep(1)
                print("You open the shelf and...")
                print(Fore.LIGHTGREEN_EX +"**YOU GOT A 'room 1 key'**")
                time.sleep(2)
                inventory.items["room 1 key"] = "A gold-plated key. It has the number 1 engraved on it. Fancy!"
                print("You go back explore other parts of the room\n")

    def intro():
        print("Suddenly. You end up in what appears to be a lounge room. A cozy one that is surrounded with walls covered in classical red wallpaper, and the floor is made out of dark brown wood.\nYou also see a sign that says number 1 above the door infront of you")
        time.sleep(1)
        print("That 'door' is locked, so you need to find that key first\n")
        time.sleep(2)

    def room1Menu():
        while True:
            print("You look around the room, and you see a comfy red 'sofa', a wooden 'bookshelf', a 'gramophone' on a small table next to the 'sofa', a 'table lamp' near the 'door', and a 'vault'.\nWhich would you like to interact first?")
            try:
                choice = str(input("Enter selection. Type 'inventory' to see what items you have at your disposal: "))
            except ValueError:
                print("Wrong Input! Try Again\n")
                continue
                
            #Choice conditions
            choice = str.lower(choice)
            if choice == "sofa":
                room1.comfyRedSofa()
            
            elif choice == "gramophone":
                room1.gramophone()
            
            elif choice == "bookshelf":
                room1.bookshelf()

            elif choice == "vault":
                room1.vault()

            elif choice == "table lamp":
                room1.tableLamp()
                
            elif choice == "door":
                print("It's a red wooden door that is locked.")
                time.sleep(1)
                if 'room 1 key' in inventory.items:
                    print("Looks like you have the key for it!")
                    time.sleep(1)
                    print("You walk to the door, and then you insert the key")
                    time.sleep(1)
                    print(Fore.YELLOW +"*Click!*")
                    inventory.items.pop('room 1 key')
                    time.sleep(1.5)
                    print("The key fits! You opened the door and walked in. A bright light flashed upon you.\n")
                    room1.escape = True
                    break

                else:
                    print("Seems like you don't have the right key for it.\n")
                    time.sleep(2)
            
            elif choice == "inventory":
                inventory.checkItems()

            else:
                print("Wrong Input! Try Again\n")  

    
class room2:
    escape = False
    gShelf = False
    gShelfOpen = False
    suitCase = False

    def glassShelf():
        gShelfFalse = "The buttons appear to be not working as of now. So you go back explore other parts of the room\n"
        gShelfOpen = "It's already opened and there's nothing of interest anymore."
        
        print("\nIt's a glass shelf that is attached to the wall.")
        time.sleep(1)
        if room2.gShelfOpen == True:
            print(gShelfOpen)
            time.sleep(1)
            print("So you go back explore other parts of the room\n")
        else:
            print("It's locked and there's a set of 4 buttons and a USB slot on it")
            time.sleep(1)
            print(f"The buttons are as follows: " + Fore.BLUE + "1. Water, " + Fore.RED + "2. Fire, " + Fore.GREEN + "3. Earth, " + Fore.RESET + "and " + Fore.YELLOW + "4. Wind.")
            time.sleep(1)

            if 'flashdisk' in inventory.items:
                print(Fore.LIGHTGREEN_EX +"**Used the 'flashdisk**")
                inventory.items.pop('flashdisk')
                room2.gShelf = True
                print("You inserted the flashdisk...")
                time.sleep(2)
                print("Suddenly, the buttons light up for a second.")
                time.sleep(1)

            if room2.gShelf == False:
                print(gShelfFalse)
                time.sleep(2)
            else:
                print("The buttons appear to be working now and it seems like you have to push one.")
                while True:
                    try: 
                        cGShelf = str(input("Which one is it? Just type the button number. Type 'inventory' if you need a hint: "))
                    except ValueError:
                        print("Wrong Input! Try Again\n")
                        continue
                    
                    if cGShelf == "inventory":
                        inventory.checkItems()

                    if cGShelf == "1":
                        print("That's not it.\n")

                    elif cGShelf == "2":
                        print("Correct!\n")
                        room2.gShelfOpen = True
                        inventory.items['room 2 key'] = 'A simple yet artistic looking key. It has the number 2 engraved on it'
                        print(Fore.LIGHTGREEN_EX +"**YOU GOT 'room 2 key'!**")
                        time.sleep(2)
                        print("You go back explore other parts of the room\n")
                        break

                    elif cGShelf == "3":
                        print("That's not it.\n")

                    elif cGShelf == "4":
                        print("That's not it.\n")

                    else:
                        print("Wrong Input! Try Again\n")

    def suitcase():
        sOpen = "It's already opened and there's nothing of interest anymore."
        sClosed = "It appears to be locked by a set of 4-number combination."

        print("\nIt's a black suitcase made out of leather material on the outside.")
        time.sleep(1)

        if room2.suitCase == True:
            print(sOpen)
            time.sleep(1)
            print("So you go back to explore other parts of the room.\n")
            return  # Exit the function once it's already opened.

        else:
            print(sClosed)
            while True:
                try: 
                    scChoice = input("Try to open the lock? (Y/N): ").strip().lower()
                except ValueError:
                    print("Invalid input. Please enter 'Y' or 'N'.")
                    continue

                if scChoice == "n":
                    print("You go back to explore other parts of the room.\n")
                    time.sleep(2)
                    return  # Exit if the user doesn't want to try opening the lock.

                elif scChoice == "y":
                    print("Enter the 4-digit code one number at a time. Type 'back' to stop trying.")
                    numLockCorrectCombo = ['2', '8', '4', '5']
                    numLockCombo = []  # Stores user input for the combination.

                    for i in range(4):
                        while True:
                            numLock = input(f"Enter number for slot {i + 1}: ").strip()

                            if numLock.lower() == "back":
                                print("You go back to explore other parts of the room.\n")
                                time.sleep(2)
                                return  # Exit both loops if the user decides to go back.

                            if numLock.isdigit() and len(numLock) == 1:
                                numLockCombo.append(numLock)
                                break  # Proceed to the next slot.
                            else:
                                print("Invalid input. Please enter a single-digit number.")

                    # Check if the entered combination is correct.
                    if numLockCombo == numLockCorrectCombo:
                        print(Fore.YELLOW +"*Click!*")
                        room2.suitCase = True
                        time.sleep(1)
                        print("The suitcase has opened! You take a look inside...")
                        time.sleep(1)
                        print("There is a pencil, a flashdisk, and a paper slip inside.")
                        time.sleep(1)
                        print("You take the flashdisk and the paper slip.")
                        print(Fore.LIGHTGREEN_EX +"**YOU GOT 'flashdisk' AND 'paper slip'!**")
                        inventory.items['flashdisk'] = 'A red flashdisk with a familiar logo. Seems like you could plug that into something.'
                        inventory.items['paper slip'] = 'A torn apart paper. There appears to be a riddle: Feed me and I shall survive. Give me drink and I shall die.'
                        time.sleep(2)
                        return  # Exit the function after success.

                    else:
                        print("The code doesn't seem to match. You decide to try again later.")
                        time.sleep(2)
                        return  # Exit if the combination is wrong.

                else:
                    print("Invalid input. Please type 'Y' or 'N'.")
   
    def intro():
        print("Suddenly, you end up in what appears to be a study room.\nYou also see a sign that says number 2 above the door infront of you")
        time.sleep(1)
        print("That 'door' is locked, so you need to find that key first\n")
        time.sleep(2)

    def room2Menu():
        while True:
            print("You look around the room, and you see a 'desk' with some things on it, a 'suitcase' on the floor, a 'bookshelf', a 'painting', and a 'glass shelf' on a wall.\n Which would you like to interact first?")
            try:
                choice = str(input("Enter selection. Type 'inventory' to see what items you have at your disposal: "))
            except ValueError:
                continue
                
            #Choice conditions
            choice = str.lower(choice)
            if choice == "desk":
                print("\nIt's a simple desk. There appears to be some stuff like a notebook, a glass of water, a laptop, a small plant, and others.")
                time.sleep(1)
                print("Perhaps whoever was here was 'cooking' something with his knowledge?")
                time.sleep(1)
                print("Apart from that, there isn't anything interesting on this desk..")
                time.sleep(1)
                print("So you go back explore other parts of the room.\n")
                time.sleep(2)

            if choice == "bookshelf":
                print("\nIt's a bookshelf just like in the previous room. Though, ironically there are less books in this shelf this time")
                time.sleep(1)
                print(f"Interestingly, you do noticed that one of the books' spine has the number " + Fore.YELLOW + "2845 " + Fore.RESET + "being underlined.")
                time.sleep(1.5)
                print("You go back explore other parts of the room.\n")
                time.sleep(2)
            
            elif choice == "painting":
                him = "Walter White"
                print("\nIt's a fine painting of a fine gentleman wearing a white suit, a blue shirt, and a hat on.")
                time.sleep(1)
                print(f"There's sign that says "+ Fore.YELLOW +"\x1B[3m" + him + "\x1B[0m"+ Fore.RESET +" under the painting. So you assumed that it's his name.")
                time.sleep(1)
                print("Apart from that. There's nothing of interest of this painting.")
                print("So you go back explore other parts of the room.\n")
                time.sleep(3)
            
            elif choice == "glass shelf":
                room2.glassShelf()

            elif choice == "suitcase":
                room2.suitcase()
                
            elif choice == "door":
                print("It's a birch door that is locked.")
                time.sleep(1)
                if 'room 2 key' in inventory.items:
                    print("Looks like you have the key for it!")
                    time.sleep(1)
                    print("You walk to the door, and then you insert the key")
                    time.sleep(1)
                    print(Fore.YELLOW +"*Click!*")
                    inventory.items.pop('room 2 key')
                    time.sleep(1.5)
                    print("The key fits! You opened the door and walked in. A bright light flashed upon you.\n")
                    room2.escape = True
                    break

                else:
                    print("Seems like you don't have the right key for it.\n")
                    time.sleep(2)
            
            elif choice == "inventory":
                inventory.checkItems()

            else:
                print("Wrong Input! Try Again\n")


class room3:
    escape = False
    chestStatus = False

    def chest():
        print("\nIt's a regular wooden chest")
        time.sleep(1)

        if room3.chestStatus == True:
            print("It's already opened and there's nothing of interest anymore.")
            time.sleep(1)
            print("So you go back explore other parts of the room.\n")
            time.sleep(2)

        else:
            print("It appears to be locked by a 3-number combination")
            while True:
                try: 
                    scChoice = input("Try to open the lock? (Y/N): ").strip().lower()
                except ValueError:
                    print("Invalid input. Please enter 'Y' or 'N'.")
                    continue

                if scChoice == "n":
                    print("You go back to explore other parts of the room.\n")
                    time.sleep(2)
                    return  # Exit if the user doesn't want to try opening the lock.

                elif scChoice == "y":
                    print("Enter the 3-digit code one number at a time. Type 'back' to stop trying.")
                    numLockCorrectCombo = ['3', '5', '6']
                    numLockCombo = []  # Stores user input for the combination.

                    for i in range(3):
                        while True:
                            numLock = input(f"Enter number for slot {i + 1}: ").strip()

                            if numLock.lower() == "back":
                                print("You go back to explore other parts of the room.\n")
                                time.sleep(2)
                                return  # Exit both loops if the user decides to go back.

                            if numLock.isdigit() and len(numLock) == 1:
                                numLockCombo.append(numLock)
                                break  # Proceed to the next slot.
                            else:
                                print("Invalid input. Please enter a single-digit number.")

                    # Check if the entered combination is correct.
                    if numLockCombo == numLockCorrectCombo:
                        print(Fore.YELLOW +"*Click!*")
                        room3.chestStatus = True
                        time.sleep(1)
                        print("The chest has opened! You take a look inside...")
                        time.sleep(1)
                        print("There is a letter, and the room key inside!.")
                        time.sleep(1)
                        print("You take the letter and the room key.")
                        print(Fore.LIGHTGREEN_EX +"**YOU GOT 'letter' AND 'room 3 key'!**")
                        inventory.items['letter'] = 'Well done, my friend! It seems like you have solved the last room. I must say that it was quite exciting to see you go through those rooms. This is our goodbye, I am afraid. Now I am gonna go back to how things were. You escaped and I live alone again...'
                        inventory.items['room 3 key'] = 'A silver key with the number 3 engraved on it.'
                        time.sleep(2)
                        return  # Exit the function after success.

                    else:
                        print("The code doesn't seem to match. You decide to try again later.")
                        time.sleep(2)
                        return  # Exit if the combination is wrong.

                else:
                    print("Invalid input. Please type 'Y' or 'N'.")

    def bed():
        print("It's a comfortable bed. You tried to sit on it.")
        time.sleep(1)
        print("It's comfortable alright. So much so that you relaxed for a moment. This is even better than the sofar in the first room!")
        time.sleep(1)
        print("Wait a minute...")
        time.sleep(2)
        print("There's a vinyl under the blankets!?")
        time.sleep(1)
        print("The vinyl is called " + Fore.YELLOW + "'Soul & Mind' by E's Jammy Jam. " + Fore.RESET + "Why does that song title ring a bell?")
        time.sleep(1)
        print("Apart from that, there's nothing else interesting from the bed. So you go back explore other parts of the room.\n")
        time.sleep(2)

    def desk():
        print("\nYou walked to the desk and you see a 'notebook', a 'flower pot', and a 'picture'. Which do you want to investigate?")
        while True:
            try:
                cDesk = str(input("Enter selection. Type 'back' if you're done investigating: "))
            except ValueError:
                print("Wrong Input! Try Again\n")
                continue
            
            #Choice conditions
            cDesk = str.lower(cDesk)
            message = "Please remind me to look at your pictures from a 'different' lens if I forget the code to open my chest."
            if cDesk == "notebook":
                print(f"\nIt's a small notebook. There's something written on it. \n")
                print(f"\x1B[3m" + Fore.YELLOW + message + "\x1B[0m")
                time.sleep(2)
            elif cDesk == "flower pot":
                print("\nIt's a pretty little red flower. How cute.\n")
                time.sleep(1)
            elif cDesk == "picture":
                print("\nIt's a picture of a beautiful young woman. She appeared to wear a set clothing from a royal family. Looks fancy!\n")
                time.sleep(1)
            elif cDesk == "back":
                print("You go back explore other parts of the room\n")
                time.sleep(1)
                break
            else:
                print("Wrong Input! Try Again\n")

    def intro():
        print("Suddenly, you end up in what appears to be a bedroom?\nThe room itself is surrounded with cyan wallpaper and the floor is covered with dark blue carpet.\nYou also see a sign that says number 3 above the door infront of you")
        time.sleep(1)
        print("That 'door' is locked, so you need to find that key first\n")
        time.sleep(2)

    def room3Menu():
        while True:
            print("You look around the room, and you see a 'bed', a set of 'picture' frames on the wall, a 'chest' on the floor, and a 'desk' with some things on it.\n Which would you like to interact first?")
            try:
                choice = str(input("Enter selection. Type 'inventory' to see what items you have at your disposal: "))
            except ValueError:
                continue
                
            #Choice conditions
            choice = str.lower(choice)
            if choice == "desk":
                room3.desk()

            if choice == "picture":
                print("It's a set of 3 picture frames with only some text written on it.")
                time.sleep(1)
                print("-------------------------------------------")
                print("TTEEEEEEETT     TTEEEEEEETT     TTEEEEEEETT")
                print("TTTTTTTEETT     TTEETTTTTTT     TTEETTTTTTT")
                print("TTTTTTTEETT     TTEETTTTTTT     TTEETTTTTTT")
                print("TTEEEEEEETT     TTEEEEEEETT     TTEEEEEEETT")
                print("TTEEEEEEETT     TTEEEEEEETT     TTEETTTEETT")
                print("TTTTTTTEETT     TTTTTTTEETT     TTEETTTEETT")
                print("TTTTTTTEETT     TTTTTTTEETT     TTEETTTEETT")
                print("TTEEEEEEETT     TTEEEEEEETT     TTEEEEEEETT")
                print("-------------------------------------------")
                time.sleep(5)
            
            elif choice == "bed":
                room3.bed()
            
            elif choice == "chest":
                room3.chest()
                
            elif choice == "door":
                print("It's an oak planks door that is locked.")
                time.sleep(1)
                if 'room 3 key' in inventory.items:
                    print("Looks like you have the key for it!")
                    time.sleep(1)
                    print("You walk to the door, and then you insert the key")
                    time.sleep(1)
                    print(Fore.YELLOW +"*Click!*")
                    inventory.items.pop('room 3 key')
                    time.sleep(1.5)
                    print("The key fits! You opened the door and walked in. A bright light flashed upon you.\n")
                    room3.escape = True
                    break

                else:
                    print("Seems like you don't have the right key for it.\n")
                    time.sleep(2)
            
            elif choice == "inventory":
                inventory.checkItems()

            else:
                print("Wrong Input! Try Again\n")


#Room 4 and 5 were planned but unfortunately cannot be made due to time contraints because of a hectic assignment for Computer Architecture subject
class room4:
    pass

class room5:
    pass


#The game's intro
print(Fore.CYAN +"THE ESCAPE ROOM")
print(Fore.CYAN +"----------------")
print(Fore.CYAN +"**The game will start in 3 seconds**")
time.sleep(3)
print("You wake up. Your head feels dizzy. You look around and you realise that you're trapped in a room with")
time.sleep(1)
print("little to no knowlodge on how you got here. You only have one objective in your mind. To escape the room... or rooms.")
time.sleep(1)

# # #Executing the game's progression
# The Prologue stage
prologue.intro()
prologue.startGameChoice()
while prologue.escape == False:
    prologue.room0Menu()

# #Room 1
room1.intro()
while room1.escape == False:
    room1.room1Menu()

# #Room 2
room2.intro()
while room2.escape == False:
    room2.room2Menu()

# Room 3
room3.intro()
while room3.escape == False:
    room3.room3Menu()

#Congrats message
print(Fore.CYAN +"GAME ENDED")
print(Fore.CYAN +"----------")
print(Fore.CYAN +"**Congratulations player! You have finally escaped to your freedom! You looked around and you see a familiar campus infront of you**")
time.sleep(1)
print(Fore.CYAN +"**A friend come up to you and asked where have you been.**")
time.sleep(1)
print(Fore.CYAN +"**You explained what happened but as you turn around, the door you came from was gone in thin air.**")
time.sleep(1)
print(Fore.CYAN +"**Was everything real? Or was it a dream? Who knows.**")
time.sleep(1)
print(Fore.CYAN +"**What matters is that you have escaped. Good job!**")