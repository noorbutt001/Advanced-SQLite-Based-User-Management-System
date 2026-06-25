from database import create_tables
from auth import register_user, login_user, forgot_password
from user_operations import view_profile, update_profile, delete_account
from admin_panel import (
    view_all_users, search_users, filter_by_role,
    delete_any_user, export_users
)
from utils import validate_email, validate_phone

current_user = None


def main_menu():
    print("\n========== 🏠 MAIN MENU ==========")
    print("1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit")
    print("==================================")


def user_menu():
    print("\n========== 👤 USER MENU ==========")
    print("1. View Profile")
    print("2. Update Profile")
    print("3. Delete Account")
    if current_user["role"] == "Admin":
        print("4. Admin Panel")
    print("0. Logout")
    print("==================================")


def admin_menu():
    print("\n========== 🛡️ ADMIN PANEL ==========")
    print("1. View All Users")
    print("2. Search Users")
    print("3. Filter by Role")
    print("4. Delete Any User")
    print("5. Export Users to CSV")
    print("0. Back")
    print("====================================")


def handle_register():
    username = input("Username: ").strip()
    email = input("Email: ").strip()
    if not validate_email(email):
        print("❌ Invalid email format.")
        return
    password = input("Password: ").strip()
    phone = input("Phone: ").strip()
    if not validate_phone(phone):
        print("❌ Invalid phone number.")
        return
    role = input("Role (Admin/User) [default: User]: ").strip() or "User"
    register_user(username, email, password, phone, role)


def handle_login():
    global current_user
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    user = login_user(username, password)
    if user:
        current_user = user
        user_session()


def handle_forgot_password():
    username = input("Enter username: ").strip()
    new_password = input("Enter new password: ").strip()
    forgot_password(username, new_password)


def user_session():
    global current_user
    while current_user:
        user_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            view_profile(current_user["id"])
        elif choice == "2":
            email = input("New email (skip to ignore): ").strip() or None
            phone = input("New phone (skip to ignore): ").strip() or None
            password = input("New password (skip to ignore): ").strip() or None
            update_profile(current_user["id"], email, phone, password)
        elif choice == "3":
            confirm = input("Are you sure? (yes/no): ").lower()
            if confirm == "yes":
                delete_account(current_user["id"])
                current_user = None
                break
        elif choice == "4" and current_user["role"] == "Admin":
            admin_session()
        elif choice == "0":
            print("👋 Logged out.")
            current_user = None
            break
        else:
            print("❌ Invalid choice.")


def admin_session():
    while True:
        admin_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            view_all_users()
        elif choice == "2":
            keyword = input("Enter username/email keyword: ").strip()
            search_users(keyword)
        elif choice == "3":
            role = input("Enter role (Admin/User): ").strip()
            filter_by_role(role)
        elif choice == "4":
            uid = input("Enter user ID to delete: ").strip()
            if uid.isdigit():
                delete_any_user(int(uid))
        elif choice == "5":
            export_users()
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice.")


def run():
    create_tables()
    while True:
        main_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            handle_register()
        elif choice == "2":
            handle_login()
        elif choice == "3":
            handle_forgot_password()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    run()