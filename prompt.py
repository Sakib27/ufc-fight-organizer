import psycopg2
from psycopg2 import sql

def connect():
    return psycopg2.connect(
        dbname="yourdbname", 
        user="yourusername", 
        password="yourpassword", 
        host="yourhost", 
        port="yourport"
    )

def login(cursor, username, password):
    cursor.execute("SELECT * FROM Users WHERE Username=%s AND HashedPW=%s", (username, password))
    user = cursor.fetchone()
    return user

def main_menu():
    print("Welcome to the UFC Event Management System")
    print("1. Login")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice

def user_menu(user):
    user_type = user[6]  # Assuming UserType is the 7th column in Users table
    if user_type == 'Attendee':
        attendee_menu(user)
    elif user_type == 'Staff':
        staff_menu(user)
    elif user_type == 'Admin':
        admin_menu(user)
    elif user_type == 'Organizer':
        organizer_menu(user)
    elif user_type == 'Fighter':
        fighter_menu(user)

def attendee_menu(user):
    print("Attendee Menu")
    # Implement attendee-specific functionality

def staff_menu(user):
    print("Staff Menu")
    # Implement staff-specific functionality

def admin_menu(user):
    print("Admin Menu")
    # Implement admin-specific functionality

def organizer_menu(user):
    print("Organizer Menu")
    # Implement organizer-specific functionality

def fighter_menu(user):
    print("Fighter Menu")
    # Implement fighter-specific functionality

def main():
    conn = connect()
    cursor = conn.cursor()
    while True:
        choice = main_menu()
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = login(cursor, username, password)
            if user:
                user_menu(user)
            else:
                print("Invalid login credentials")
        elif choice == '2':
            break
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
