import datetime

now = datetime.datetime.now()

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
                        "wallet": 0,
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
        print(f"Room: {room}")
        print(f"Available Units: {available}")
        print(f"Daily Rate: {price}")
        print(design_1*3)
    
    print("\nDELUXE ROOMS")
    print(design_1*3)
    for room, details in room_details_deluxe.items():
        available = details["Available"]
        price = details["Price"]
        print(f"Room: {room}")
        print(f"Available: {available}")
        print(f"Price: {price}")
        print(design_1*3)


available_price_room()

#user menu

