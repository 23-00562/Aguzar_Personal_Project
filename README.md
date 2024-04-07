# 🏨Azure Bay Hotel Management System

## Introduction
The Azure Bay Hotel Management System is a comprehensive Python-based application designed to streamline the operations of a hotel, providing efficient management of bookings, room availability, user accounts, and administrative tasks. This system offers a user-friendly interface for both guests and administrators, enhancing the overall experience of managing hotel operations.

## Features
1. **User Management:**
   - **User Registration:** Guests can register as users by providing essential details such as username, password, full name, and contact number. 📝
   - **User Login:** Registered users can log in securely using their credentials to access various services offered by the hotel. 🔒

2. **Admin Functionality**
   - **Admin Login:** Administrators have access to a dedicated interface for performing administrative tasks. 👨‍💼
   - **Room Management:** Admins can manage available rooms, including adding, modifying, or removing rooms across different branches of the hotel. 🛏️
   - **Branch Management:** Admins can add new branches, remove existing ones, or modify details related to branches. 🏢
   - **Price Management:** Admins have the authority to edit room prices based on room type, size, and branch location. 💰

3. **Room Booking and Availability**
   - **View Available Rooms:** Users can check the availability of rooms and their corresponding prices based on room type and branch location. 🛎️
   - **Book a Room:** Guests can book a room by specifying the branch, room type, size, and desired dates for check-in and check-out. 📅
   - **Check Room Availability:** The system automatically updates room availability upon booking or cancellation, ensuring accurate availability status. 🔄

4. **Transaction Management**
   - **Cash In:** Users can deposit money into their account, which can be used for future bookings and transactions. 💳
   - **View Wallet Balance:** Users can view their current wallet balance to track their account's financial status. 💰
   - **View Cashback:** Users can view accumulated cashback rewards earned from previous bookings, enhancing user engagement and loyalty. 🎁

5. **Reservation Management**
   - **View Current Rented Room:** Users can view details of the room they have currently rented, including check-in/out dates, room type, price, etc. 🛏️
   - **Check Out:** Users can check out from their rented room, updating room availability and prompting for feedback to improve service quality. 🚪
   - **Cancel Reservation:** Users can cancel their room reservation before check-in, which updates room availability and ensures efficient management of bookings. ❌

6. **Hotel Amenities and Information**
   - **Branch Information:** Users can access information about different branches of the hotel, including location details and available facilities. 📍
   - **Explore Hotel Amenities:** Users can explore the amenities available in different types of rooms (Standard, Deluxe) across various branches of the hotel. 🏊‍♂️

8. **Feedback and Rating System**
   - **Customer Feedback:** Administrators can view feedback provided by customers and their ratings, facilitating continuous improvement of services and guest satisfaction. 📝⭐

## Implementation
- The system is implemented using Python programming language, leveraging its simplicity and versatility. 🐍
- Data structures like dictionaries are utilized to store user accounts, hotel information, feedbacks, etc., ensuring efficient data management. 🗃️
- Object-oriented programming principles are incorporated to encapsulate functionalities into modular and reusable components. 🔄
- Exception handling mechanisms are implemented to handle errors gracefully and ensure smooth user interaction. ⚠️

## Dependencies
- The system is designed to minimize external dependencies and relies solely on Python's standard library for its functionality. 📦

## Usage
1. Clone or download the repository containing the source code files.
2. Ensure Python (version 3.x recommended) is installed on your system.
3. Run the `azure_hotel_management_system.py` file using a Python interpreter to launch the application.
4. Follow the on-screen instructions and prompts to navigate through different functionalities.
5. Use the admin interface to perform administrative tasks, manage rooms, branches, etc.
6. Register as a new user or log in using existing credentials to access user-specific functionalities such as room booking, check-in/out, etc. 🔑

## Contributors
- This project, developed and maintained by **Joel Lazernnie A. Aguzar**, was created as an academic requirement for CS 121: Advanced Computer Programming under the supervision of Prof. Francis Jesmar Montalbo. The project aims to demonstrate proficiency in Python programming and software development through the implementation of a comprehensive hotel management system.
- Contributions, suggestions, and feedback from the community are welcome and encouraged to enhance the functionality and usability of the system. 🙌
