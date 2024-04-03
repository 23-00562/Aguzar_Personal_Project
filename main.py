from datetime import datetime

now = datetime.now()

user_accounts ={}

hotel_branches = ["Baguio", "Manila", "Batangas"]

hotel_info = {
    "Standard": {
        hotel_branches[0]: {"Single": {"Available": 17, "Price": 549}, 
                   "Double": {"Available": 12, "Price": 799}, 
                   "Suite": {"Available": 3, "Price": 1450}}, 
        hotel_branches[1]: {"Single": {"Available": 23, "Price": 649}, 
                   "Double": {"Available": 15, "Price": 1000},
                   "Suite": {"Available": 7, "Price": 2300}},
        hotel_branches[2]: {"Single": {"Available": 9, "Price": 599}, 
                     "Double": {"Available": 7, "Price": 999}, 
                     "Suite": {"Available": 4, "Price": 1999}}
    },

    "Deluxe":{
        hotel_branches[0]: {"Single": {"Available": 15, "Price": 749}, 
                   "Double": {"Available": 10, "Price": 999}, 
                   "Suite": {"Available": 3, "Price": 1550}},
        hotel_branches[1]: {"Single": {"Available": 21, "Price": 850},
                   "Double": {"Available": 11, "Price": 1200},
                   "Suite": {"Available": 6, "Price": 2500}},
        hotel_branches[2] : {"Single": {"Available": 10, "Price": 799}, 
                     "Double": {"Available": 6, "Price": 1159}, 
                     "Suite": {"Available": 2, "Price": 2249}}
    }
}

design_1 = '~' * 10

admin_username = "admin"
admin_password = "adminhotel01"

def register():
    print ("\nREGISTER")
    while True:
        try:
            username = input ("\nEnter a Valid Username (Press ENTER to go back): ")
            if not username:
                return
            else:
                password = str(input("Enter a Password (at least 8 characters): "))
                if len(password) < 8:
                    print("\nTry Again! Password must be at least 8 characters long.")
                else:
                    full_name = input ("Enter your Full Name: ")
                    contact_number = input ("Enter your Contact Number: ")
                    user_accounts [username] = {
                        "password": password,
                        "full_name": full_name,
                        "contact_number": contact_number,
                        "balance": 0,
                        "cashback":0,
                        "room_rented": {}
                    }
                    print("\nYou have successfully created your account!")
                    break
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def user_login():
    print ("\nLOG IN")
    while True:
        try:
            username = input ("\nEnter your Username (Press ENTER to go back): ")
            if not username:
                return
            elif username not in user_accounts:
                print ("\nUser not found! Please create an acoount.")
            else:
                password = str (input("Enter your Password: "))
                if user_accounts [username] ["password"] == password:
                    print ('\nWelcome to Azure Bay Hotel')
                    #user_menu(username)
                    #break
                else:
                    print ("\nPlease try again! Password doesn't match.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def admin_login():
    print ("\nADMIN LOG IN")
    while True:
        try:
            username = input ("\nEnter your Username (Press ENTER to go back): ")
            if not username:
                return
            elif username != admin_username:
                print ("\nUser not found! Please create an acoount.")
            else:
                password = str (input("Enter your Password: "))
                if password == admin_password:
                    print ('\nWelcome to Azure Bay Hotel: Admin Panel')
                    #admin_menu()
                    #break
                else:
                    print ("\nPlease try again! Password doesn't match.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def hotel_amenities():
    pass

def view_feedback():
    pass

def branch_hotel():
    print("\nHOTEL BRANCHES: \n")
    for i in range (len(hotel_branches)):
        print (f"{i+1}. " + hotel_branches[i])

def available_room():
    print ("Check Available Rooms and Prices")
    branch_hotel()
    branch = input ("\nSelect Hotel Branch (Enter the number): ")
    if branch == "1":
        branch = hotel_branches[0]
    elif branch == "2":
        branch = hotel_branches[1]
    elif branch == "3":
        branch = hotel_branches[2]
    else:
        print ("Invalid Input")
        return
    room_details_standard = hotel_info["Standard"][branch]
    room_details_deluxe = hotel_info["Deluxe"][branch]
    
    print("\nSTANDARD ROOMS")
    print(design_1*3)
    for room, details in room_details_standard.items():
        available = details["Available"]
        price = details["Price"]
        print(f"Room Size: {room}")
        print(f"Available Units: {available}")
        print(f"Daily Rate: {price}")
        print(design_1*3)
    
    print("\nDELUXE ROOMS")
    print(design_1*3)
    for room, details in room_details_deluxe.items():
        available = details["Available"]
        price = details["Price"]
        print(f"Room Size: {room}")
        print(f"Available: {available}")
        print(f"Price: {price}")
        print(design_1*3)

def book_room():
    print ("Book a Room")
    available_room()
    while True:
        try:
            if user_accounts[username]["room_rented"]:
                print ("\nYou have already rented a room. Please check out first.")
                break
            else:
                room_type = input ("\nSelect Room Type (Standard/Deluxe|Press Enter to go Back): ")
                if not room:
                    return
                elif room not in hotel_info:
                    print ("\n Room not Found! Choose a Valid Room Type.")
                else:
                    room_size = input ("\nSelect Room Type (Single/Double/Suite): ")
                    if room_size not in hotel_info[room_type][branch]:
                        print ("\nRoom not Found! Choose a Valid Room Size.")
                    else:
                        if hotel_info[room_type][branch][room_size]["Available"] > 0:
                            check_in = input("\nEnter Check-in Date (YYYY-MM-DD): ")
                            check_out = input("\nEnter Check-out Date (YYYY-MM-DD): ")
                            days_stay = (datetime.strptime(check_out, "%Y-%m-%d") - datetime.strptime(check_in, "%Y-%m-%d")).days
                            balance = user_accounts[username]["balance"]
                            price = hotel_info[room_type][branch][room_size]["Price"]* days_stay
                            if balance > price:
                                user_accounts[username]["balance"] -= price
                                cashback = price * 0.30
                                user_accounts[username]["balance"] += cashback
                                hotel_info[room_type][branch][room_size]["Available"] -= 1
                                user_accounts[username]["room_rented"] = {
                                    "Date Booked": now.strftime("%Y-%m-%d %H:%M:%S"),
                                    "Check-in": check_in,
                                    "Check-out": check_out,
                                    "Days of Stay": days_stay,
                                    "Branch": branch,
                                    "Room Type": room_type,
                                    "Room Size": room_size,
                                    "Price": price,
                                }
                                print("\nYou have successfully booked a room!")
                                print(f"You have earned ₱{cashback} cashback. ")
                                print(f"\nYour current balance is ₱{user_accounts[username]['balance']}.")
                                print("To see further details proceed to 'Current Rented Room'.")
                                break
                            else:
                                print ("\nInsufficient Balance! Please deposit money to your account.")
                        else:
                            print ("\nRoom is not available. Please choose another room.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def current_rented_room():
    print ("\nCURRENT RENTED ROOM")
    print ("\nTo Check in, please proceed to the front desk.")
    for username, details in user_accounts.items():
        if details["room_rented"]:
            print(f"\n{username} rented a room.")
            for key, value in details["room_rented"].items():
                print(f"{key}: {value}")
        else:
            print(f"\n{username} has no rented room.")

def return_room

def manual_check_out():
    print ("\nCHECK OUT")
    while True:
        try:
            response = input("\nDo you want to check out? (y/n): ")
            if response.lower() == "n":
                break
            elif response.lower() == "y":
                if user_accounts[username]["room_rented"]:
                    room_type = user_accounts[username]["room_rented"]["Room Type"]
                    room_size = user_accounts[username]["room_rented"]["Room Size"]
                    branch = user_accounts[username]["room_rented"]["Branch"]
                    hotel_info[room_type][branch][room_size]["Available"] += 1
                    user_accounts[username]["room_rented"] = {}
                    print("\nYou have successfully checked out.")
                    break
                else:
                    print("\nYou have no rented room.")
            else:
                print("\nInvalid Input! Please try again.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def cancel_reservation():
    print ("\nCANCEL RESERVATION")
    while True:
        try:
            response = input("\nDo you want to cancel your reservation? (y/n): ")
            if response.lower() == "n":
                break
            elif response.lower() == "y":
                if user_accounts[username]["room_rented"]:
                    room_type = user_accounts[username]["room_rented"]["Room Type"]
                    room_size = user_accounts[username]["room_rented"]["Room Size"]
                    branch = user_accounts[username]["room_rented"]["Branch"]
                    hotel_info[room_type][branch][room_size]["Available"] += 1
                    user_accounts[username]["room_rented"] = {}
                    print("\nYou have successfully cancelled your reservation.")
                    break
                else:
                    print("\nYou have no reserved room.")
            else:
                print("\nInvalid Input! Please try again.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

        

def cash_in ():
    print ("\nCASH-IN")
    while True:
        try:
            amount = float(input ("\nEnter the amount you want to cash in (Press ENTER to go Back): "))
            if not amount:
                return
            elif amount <= 0:
                print ("Amount should be greter than 0.")
            else:
                    user_accounts [username] ["balance"] += amount
                    print(f"Successfully cashed in ${amount}.")
                    print(f"\nCurrent balance for {username}: ${user_accounts[username]["balance"]}.")
                    break
        except ValueError as e:
            print (f"\nAn error occured: {e}")


book_room()
 
#user menu

