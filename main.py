from datetime import datetime

now = datetime.now()

feedbacks = {}

user_accounts ={"joel": {
                        "password": "12345678",
                        "full_name": "dbsljdb",
                        "contact_number": "contact_number",
                        "balance": 10000000.00,
                        "cashback":0.00,
                        "room_rented": {}
                    }
                }

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

spacing = " " * 19
design_1 = '~' * 10
design_2 = '=' * 10
design_3 = '-' * 10

admin_username = "admin"
admin_password = "adminhotel01"

def register():
    hotel_header()
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
                        "balance": 0.00,
                        "cashback":0.00,
                        "room_rented": {}
                    }
                    print("\nYou have successfully created your account!")
                    print(f"Welcome to Azure Bay Hotel, {full_name}! Please log in to continue.")
                    break
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def user_login():
    hotel_header()
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
                    print (f"\nYou have successfully logged in!")
                    print ('Welcome to Azure Bay Hotel')
                    user_menu(username)
                    break
                else:
                    print ("\nPlease try again! Password doesn't match.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def admin_login():
    hotel_header()
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
                    print (f'\nWelcome to Azure Bay Hotel: {username}')
                    admin_menu()
                    break
                else:
                    print ("\nPlease try again! Password doesn't match.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def hotel_amenities():
    hotel_header()
    print("\n         ------- HOTEL ROOMS INFO -------")
    print("")
    print("         ------ STANDARD ROOMS INFO ------")
    print("\nSTANDARD (Single)")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Single Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 1 sofa, Window/Split AC")
    print("and an attached washroom with hot/cold water.\n")
    print("STANDARD (Double)")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("STANDARD (Suite)")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double King Size Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 3 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("         ------ DELUXE ROOMS INFO ------")
    print("\nDELUXE (Single)")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Queen Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 1 sofa, Window/Split AC,")
    print("Mini Fridge, and an attached washroom with hot/cold water.\n")
    print("DELUXE (Double)")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 King Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Window/Split AC,")
    print("Mini Fridge, and an attached washroom with hot/cold water.\n")
    print("DELUXE (Suite)")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 King Size Bed, Television, Telephone,")
    print("Triple-Door Cupboard, 1 Coffee table with 3 sofa, 1 Side table,")
    print("Balcony with an Accent table with 2 Chairs, Window/Split AC,")
    print("Mini Fridge, and an attached washroom with hot/cold water.\n")

def branch_hotel():
    print("\nHOTEL BRANCHES: \n")
    for i in range (len(hotel_branches)):
        print (f"{i+1}. " + hotel_branches[i])

def available_room():
    print (f"\n{design_3*2} CHECK AVAILABLE ROOMS AND PRICES {design_3*2}")
    branch_hotel()
    branch = input ("\nSelect Hotel Branch (Press ENTER to go back): ")
    if not branch:
        return
    elif branch not in hotel_branches:
        print (f"\n{branch} is not a valid branch. Please try again.")
    else:
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

def check_dates():
    while True:
        try:
            global check_in
            global check_out
            check_in = input("\nEnter Check-in Date (YYYY-MM-DD): ")
            if datetime.strptime(check_in, "%Y-%m-%d") < now:
                print("Check-in date should be greater than or equal to the present date.")
            else:
                check_out = input("Enter Check-out Date (YYYY-MM-DD): ")
                if datetime.strptime(check_out, "%Y-%m-%d") <= datetime.strptime(check_in, "%Y-%m-%d"):
                    print("Check-out date should be greater than the check-in date.")
                else:
                    break
        except ValueError as e:
            print (f"\nAn error occured: {e}")


def book_room(username):
    print (f"\n{design_1 * 3} BOOK A ROOM {design_1 * 3}")
    while True:
        try:
            if user_accounts[username]["room_rented"]:
                print ("\nYou have already rented a room. Please check out first.")
                break
            else:
                branch_hotel()
                branch = input ("\nSelect Hotel Branch (Press ENTER to go back): ")
                if not branch:
                    return
                elif branch not in hotel_branches:
                    print (f"\n{branch} is not a valid branch. Please try again.")
                else:
                    room_type = input ("Select Room Type (Standard/Deluxe): ")
                    if room_type not in hotel_info:
                        print ("\n Room not Found! Choose a Valid Room Type.")
                    else:
                        room_size = input ("Select Room Type (Single/Double/Suite): ")
                        if room_size not in hotel_info[room_type][branch]:
                            print ("\nRoom not Found! Choose a Valid Room Size.")
                        else:
                            if hotel_info[room_type][branch][room_size]["Available"] > 0:
                                check_dates()
                                days_stay = (datetime.strptime(check_out, "%Y-%m-%d") - datetime.strptime(check_in, "%Y-%m-%d")).days
                                balance = user_accounts[username]["balance"]
                                price = hotel_info[room_type][branch][room_size]["Price"]* days_stay
                                if balance > price:
                                    user_accounts[username]["balance"] -= price
                                    cashback = price * 0.10
                                    user_accounts[username]["balance"] += cashback
                                    user_accounts[username]["cashback"] += cashback
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
                                    print (f"\n{design_1 * 7}")
                                    print("\nYou have successfully booked a room!")
                                    print(f"\nYou have paid ₱{price}.")
                                    print(f"You have earned ₱{cashback} cashback. ")
                                    print(f"Your current balance is ₱{user_accounts[username]['balance']}")
                                    print("\nTo see further details proceed to 'View Current Rented Room'.")
                                    print (f"\n{design_1 * 7}")
                                    break
                                else:
                                    print ("\nInsufficient Balance! Please deposit money to your account.")
                            else:
                                print ("\nRoom is not available. Please choose another room.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def current_rented_room(username):
    print (f"\n{design_1 * 3} CURRENT RENTED ROOM {design_1 * 3}")
    print ("\nTo Check in, please proceed to the front desk.")
    for username, details in user_accounts.items():
        if details["room_rented"]:
            print(f"\n{username} rented a room.\n")
            for key, value in details["room_rented"].items():
                if key == "Price":
                    value = "₱" + str(value)
                print(f"{key}: {value}")
        else:
            print(f"\n{username} has no rented room.")

def return_room(username):
    if user_accounts[username]["room_rented"]:
        room_type = user_accounts[username]["room_rented"]["Room Type"]
        room_size = user_accounts[username]["room_rented"]["Room Size"]
        branch = user_accounts[username]["room_rented"]["Branch"]
        hotel_info[room_type][branch][room_size]["Available"] += 1
        user_accounts[username]["room_rented"] = {}
        print("\nYou have successfully checked out.")
        feedback()
    else:
        print("\nYou have no rented room.")
    
def perform_check_out(username):
    print (f"\n{design_1 * 3} CHECK OUT {design_1 * 3}")
    while True:
        try:
            response = input("\nDo you want to check out? (y/n): ")
            if response.lower() == "n":
                break
            elif response.lower() == "y":
                return_room(username)
                break
            else:
                print("\nInvalid Input! Please try again.")
        except ValueError as e:
            print (f"\nAn error occurred: {e}")

def cancel_reservation(username):
    print (f"\n{design_1 * 3} CANCEL RESERVATION {design_1 * 3}")
    while True:
        try:
            response = input("\nDo you want to cancel your reservation? (y/n): ")
            if response.lower() == "n":
                break
            elif response.lower() == "y":
                return_room(username)
                break
            else:
                print("\nInvalid Input! Please try again.")
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def cash_in (username):
    print (f"\n{design_1 * 3} CASH-IN {design_1 * 3}")
    while True:
        try:
            amount = float(input ("\nEnter the amount you want to cash in (Press ENTER to go Back): "))
            if not amount:
                return
            elif amount <= 0:
                print ("Amount should be greter than 0.")
            else:
                    user_accounts [username] ["balance"] += amount
                    print(f"Successfully cashed in ₱{amount}.")
                    print(f"\nCurrent balance for {username}: ₱{user_accounts[username]["balance"]}.")
                    break
        except ValueError as e:
            print (f"\nAn error occured: {e}")

def view_wallet(username):
    print (f"\n{design_1 * 3} VIEW WALLET {design_1 * 3}")
    print(f"\nCurrent balance for {username}: ₱{user_accounts[username]['balance']}.")

def view_cashback(username):
    print (f"\n{design_1 * 3} VIEW CASHBACK {design_1 * 3}")
    print(f"\nCurrent accumulated cashbacks for {username}: ₱{user_accounts[username]['cashback']}.")

def feedback():
    while True:
        try:
            response = input("\nDo you want to rate our service? (y/n): ")
            if response.lower() == "n":
                break
            elif response.lower() == "y":
                print("\nCUSTOMER FEEDBACK")
                user = input("\nEnter your name: ")
                rating = int(input("Rate our service from 1 to 5 stars: "))
                if rating < 1 or rating > 5:
                    print("Invalid rating! Please rate from 1 to 5 stars.")
                else:
                    if user in feedbacks:
                        feedbacks[user].append(rating)
                    else:
                        feedbacks[user] = [rating]
                    print("\nThank you for your feedback!")
                    break
            else:
                print("\nInvalid Input! Please try again.")
        except ValueError as e:
            print(f"\nAn error occurred: {e}")

def view_feedback():
    hotel_header()
    print("\nVIEW FEEDBACK")
    print("\nFeedbacks: ")
    if feedbacks:
        for user, ratings in feedbacks.items():
            average_rating = sum(ratings) / len(ratings)
            print(f"\n{user}: {'★ ' * int(average_rating)}")
    else:
        print("Sorry, there is no available feedback yet.")

def add_branch():
    while True:
        try:
            print(f"\n{design_3*2} ADD BRANCH {design_3*2}")
            branch = input("\nEnter the location of the branch (Press Enter to go Back): ")
            if not branch:
                return
            elif branch in hotel_branches:
                print("\nBranch already exists.")
            else:
                hotel_branches.append(branch)
                hotel_info["Standard"][branch] = {"Single": {"Available": 0, "Price": 0}, 
                        "Double": {"Available": 0, "Price": 0}, 
                        "Suite": {"Available": 0, "Price": 0}}
                hotel_info["Deluxe"][branch] = {"Single": {"Available": 0, "Price": 0},
                            "Double": {"Available": 0, "Price": 0},
                            "Suite": {"Available": 0, "Price": 0}}
                print("\nBranch has been added.")
                modify_branch = input(f"\nDo you want to modify the number of rooms of {branch} Branch? (y/n): ")
                if modify_branch.lower() == "y":
                    room_type = input("\nEnter Room Type (Standard/Deluxe): ")
                    if room_type not in hotel_info:
                        print("\nRoom not found! Choose a valid room type.")
                    else:
                        room_size = input("\nEnter Room Size (Single/Double/Suite): ")
                        if room_size not in hotel_info[room_type][branch]:
                            print("\nRoom not found! Choose a valid room size.")
                        else:
                            amount = int(input("\nEnter the number of available rooms: "))
                            price = int(input("\nEnter the price of the room: "))
                            hotel_info[room_type][branch][room_size]["Available"] = amount
                            hotel_info[room_type][branch][room_size]["Price"] = price
                            print(f"\n{amount} rooms has been added to {room_size} Room, {room_type} Type in {branch} Branch with a price of {price} per unit.") 
                elif modify_branch.lower() == "n":
                    return
                else:
                    print("\nInvalid Input!")
        except ValueError as e:
            print(f"\nAn error occurred: {e}")


def modify_room():
    print(f"\n{design_3*2} MODIFY ROOM {design_3*2}")
    branch_hotel()
    branch = input("\nSelect Hotel Branch (Press ENTER to go back): ")
    if not branch:
        return
    elif branch not in hotel_branches:
        print(f"\n{branch} is not a valid branch. Please try again.")
    else:
        room_type = input("\nEnter Room Type (Standard/Deluxe): ")
        if room_type not in hotel_info:
            print("\nRoom not found! Choose a valid room type.")
        else:
            room_size = input("\nEnter Room Size (Single/Double/Suite): ")
            if room_size not in hotel_info[room_type][branch]:
                print("\nRoom not found! Choose a valid room size.")
            else:
                action = input("\nChoose an action (Add/Decrease): ")
                if action.lower() == "add":
                    amount = int(input("\nEnter the number of available rooms: "))
                    hotel_info[room_type][branch][room_size]["Available"] += amount
                    print(f"\n{amount} rooms has been added to {room_size} Room, {room_type} Type in {branch} Branch.")
                elif action.lower() == "decrease":
                    amount = int(input("\nEnter the number of rooms to decrease: "))
                    if amount > hotel_info[room_type][branch][room_size]["Available"]:
                        print("\nInvalid input! Number of rooms to decrease is greater than the available rooms.")
                    else:
                        hotel_info[room_type][branch][room_size]["Available"] -= amount
                        print(f"\n{amount} rooms has been added to {room_size} Room, {room_type} Type in {branch} Branch.")
                else:
                    print("\nInvalid action! Please choose either 'Add' or 'Decrease'.")

def edit_price_room():
    print(f"\n{design_3*2} EDIT PRICE OF ROOM {design_3*2}")
    branch_hotel()
    branch = input("\nSelect Hotel Branch (Press ENTER to go back): ")
    if not branch:
        return
    elif branch not in hotel_branches:
        print(f"\n{branch} is not a valid branch. Please try again.")
    else:
        room_type = input("\nEnter Room Type (Standard/Deluxe): ")
        if room_type not in hotel_info:
            print("\nRoom not found! Choose a valid room type.")
        else:
            room_size = input("\nEnter Room Size (Single/Double/Suite): ")
            if room_size not in hotel_info[room_type][branch]:
                print("\nRoom not found! Choose a valid room size.")
            else:
                price = float(input("\nEnter the new daily rate: "))
                hotel_info[room_type][branch][room_size]["Price"] = price
                print(f"\nPrice of {room_size} Room, {room_type} Type in {branch} Branch has been updated to {price} per unit.")  

def remove_branch():
    print(f"\n{design_3*2} REMOVE BRANCH {design_3*2}")
    branch_hotel()
    branch = input("\nEnter the location of the branch to remove (Press ENTER to go back): ")
    if not branch:
        return
    elif branch not in hotel_branches:
        print("\nBranch not found! Please try again.")
    else:
        hotel_branches.remove(branch)
        hotel_info["Standard"].pop(branch)
        hotel_info["Deluxe"].pop(branch)
        print(f"\n{branch} Branch has been removed.")  

def display_time():
        current_date = now.strftime('%Y-%m-%d')
        current_time = now.strftime('%H:%M:%S')
        print(f"\nDate: {current_date}")
        print(f"Time: {current_time}")

def hotel_header():
    print (f'\n{design_3*6}')
    print (f"{spacing} AZURE BAY HOTEL")
    print (f'{design_3*6}')

def admin_menu():
    while True:
        hotel_header()
        print("\nADMIN MENU")
        print("\n1. View Available Rooms")
        print("2. Add Branch")
        print("3. Modify Number of Rooms")
        print("4. Edit Price of Rooms")
        print("5. Remove Branch")
        print("6. Exit")
        choice = input("\nEnter the number corresponding to your choice: ")
        if choice == "1":
            available_room()
        elif choice == "2":
            add_branch()
        elif choice == "3":
            modify_room()
        elif choice == "4":
            edit_price_room()
        elif choice == "5":
            remove_branch()
        elif choice == "6":
            print("Exiting Admin Menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(username):
    while True:
        hotel_header()
        print(f"\nUSER MENU")
        print("\n1. View Available Rooms and Prices")
        print("2. Book a Room")
        print("3. View Current Rented Room")
        print("4. Check Out")
        print("5. Cash In")
        print("6. View Wallet Balance")
        print("7. View Cashback")
        print("8. Cancel Reservation")
        print("9. Log Out")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            available_room()
        elif choice == "2":
            book_room(username)
        elif choice == "3":
            current_rented_room(username)
        elif choice == "4":
            perform_check_out(username)
        elif choice == "5":
            cash_in(username)
        elif choice == "6":
            view_wallet(username)
        elif choice == "7":
            view_cashback(username)
        elif choice == "8":
            cancel_reservation(username)
        elif choice == "9":
            print(f"Exiting User Menu. Goodbye {username}!")
            break
        else:
            print("Invalid Input! Please enter a number from 1 to 9.")

def main():
    while True:
        print (f"\n{design_2} WELCOME TO AZURE BAY HOTEL {design_2}")
        display_time()
        print("\nSERVICES OFFERED: ")
        print("\n1. Register as a New User")
        print("2. User Log In")
        print("3. Admin Log In")
        print("4. Explore Hotel Amenities")
        print("5. View Customer Feedbacks")
        print("6. Exit")
        print("\nHow can we assist you today?")
        choice = input("\nEnter the number corresponding to your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            user_login()
        elif choice == "3":
            admin_login()
        elif choice == "4":
            hotel_amenities()
        elif choice == "5":
            view_feedback()
        elif choice == "6":
            print("\nThank you for staying with us. Have a Nice Day! Goodbye!")
            print (f"\n{design_2*2} AZURE BAY HOTEL {design_2*2}")
            break
        else:
            print("\nInvalid Input! Please try again.")

main()