from prettytable import PrettyTable
import database
from database import connect_to_db, get_user, create_user, close_connection, set_user_type
import hashlib

def prompt_login():
    user = input('Username: ')
    password = input('Password: ')
    return user, password

def main_menu():
    print('1. Login')
    print('2. Signup')
    print('3. Exit')

def attendee_menu():
    print('1. Buy Tickets')
    print('2. View Purchased Tickets')
    print('3. Sell Tickets')
    print('4. Logout')

def staff_menu():
    print('1. View Shifts')
    print('2. View Venue Assignments')
    print('3. Swap Shifts')
    print('4. Logout')

def admin_menu():
    print('1. Assign User Roles')
    print('2. Assign Shifts')
    print('3. Approve Shift Swaps')
    print('4. Create Fighter/Staff/Organizer Account')
    print('5. Logout')

def organizer_menu():
    print('1. Schedule Event')
    print('2. Manage Sponsors')
    print('3. Approve Fight Requests')
    print('4. Logout')

def fighter_menu():
    print('1. View Fight Schedule')
    print('2. View Upcoming Fights')
    print('3. Request Fight')
    print('4. Logout')

def create_user_account(conn, user_type='attendee'):
    user_id = input('User ID: ')
    email = input('Email: ')
    username = input('Username: ')
    full_name = input('Full Name: ')
    password = input('Password: ')
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    dob = input('Date of Birth (YYYY-MM-DD): ')
    create_user(conn, user_id, email, username, full_name, hashed_pw, dob)
    set_user_type(conn, username, user_type)
    print(f'{user_type.capitalize()} account created successfully')

def run_ui():
    conn = connect_to_db()

    while True:
        main_menu()
        choice = input('Select an option: ')

        if choice == '1':
            username, password = prompt_login()
            user = get_user(conn, username)
            if user and hashlib.sha256(password.encode()).hexdigest() == user[4]:
                print(f'Welcome {user[3]}!')
                if user[6] == 'attendee':
                    while True:
                        attendee_menu()
                        attendee_choice = input('Select an option: ')
                        if attendee_choice == '4':
                            break
                elif user[6] == 'staff':
                    while True:
                        staff_menu()
                        staff_choice = input('Select an option: ')
                        if staff_choice == '4':
                            break
                elif user[6] == 'admin':
                    while True:
                        admin_menu()
                        admin_choice = input('Select an option: ')
                        if admin_choice == '5':
                            break
                        elif admin_choice == '4':
                            print("Create account for:")
                            print("1. Fighter")
                            print("2. Staff")
                            print("3. Organizer")
                            role_choice = input('Select an option: ')
                            if role_choice == '1':
                                create_user_account(conn, 'fighter')
                            elif role_choice == '2':
                                create_user_account(conn, 'staff')
                            elif role_choice == '3':
                                create_user_account(conn, 'organizer')
                            else:
                                print('Invalid choice')
                        elif admin_choice == '4':
                            break
                elif user[6] == 'organizer':
                    while True:
                        organizer_menu()
                        organizer_choice = input('Select an option: ')
                        if organizer_choice == '4':
                            break
                elif user[6] == 'fighter':
                    while True:
                        fighter_menu()
                        fighter_choice = input('Select an option: ')
                        if fighter_choice == '4':
                            break
            else:
                print('Invalid username or password')

        elif choice == '2':
            create_user_account()

        elif choice == '3':
            break

        else:
            print('Invalid choice')

    close_connection(conn)
