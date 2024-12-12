import pymysql
from tabulate import tabulate


class UserFunctions:
    def __init__(self, connection):
        self.connection = connection

    def create_user(self, user_id, name, email, address, phone_number):
        try:
            cursor = self.connection.cursor()
            cursor.callproc("CreateUser", (user_id, name, email, address, phone_number))
            self.connection.commit()
            print(f"User '{name}' created successfully!")
        except pymysql.MySQLError as e:
            print("Error creating user:", e)

    def select_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.callproc("SelectAllUsers")
            result = cursor.fetchall()
            headers = ["UserID", "Name", "Email", "Address", "Phone Number"]
            print(tabulate(result, headers, tablefmt="grid"))
        except pymysql.MySQLError as e:
            print("Error fetching users:", e)

    def select_filtered_users(
        self, user_id=None, name=None, email=None, address=None, phone_number=None
    ):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(
                "SelectFilteredUsers", (user_id, name, email, address, phone_number)
            )
            result = cursor.fetchall()
            headers = ["UserID", "Name", "Email", "Address", "Phone Number"]
            print(tabulate(result, headers, tablefmt="grid"))
        except pymysql.MySQLError as e:
            print("Error fetching filtered users:", e)

    def select_filtered_user_contacts(
        self,
        user_id=None,
        contact_id=None,
        prefer_name=None,
        note=None,
    ):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(
                "SelectFilteredUserContacts",
                (
                    user_id,
                    contact_id,
                    prefer_name,
                    note,
                ),
            )
            result = cursor.fetchall()
            headers = [
                "UserID",
                "Name",
                "Email",
                "Address",
                "Phone Number",
                "ContactID",
                "Prefer Name",
                "Note",
            ]
            print(tabulate(result, headers, tablefmt="grid"))
        except pymysql.MySQLError as e:
            print("Error fetching filtered user contacts:", e)

    def update_filtered_users(
        self,
        user_id=None,
        new_user_id=None,
        new_name=None,
        new_email=None,
        new_address=None,
        new_phone_number=None,
    ):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(
                "UpdateFilteredUsers",
                (
                    user_id,
                    new_user_id,
                    new_name,
                    new_email,
                    new_address,
                    new_phone_number,
                ),
            )
            self.connection.commit()
            print("Users updated successfully.")
        except pymysql.MySQLError as e:
            print("Error updating users:", e)

    def delete_filtered_users(
        self, user_id=None, name=None, email=None, address=None, phone_number=None
    ):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(
                "DeleteFilteredUsers", (user_id, name, email, address, phone_number)
            )
            self.connection.commit()
            print("Users deleted successfully.")
        except pymysql.MySQLError as e:
            print("Error deleting users:", e)

    def count_filtered_users(
        self, user_id=None, name=None, email=None, address=None, phone_number=None
    ):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(
                "CountFilteredUsers", (user_id, name, email, address, phone_number)
            )
            result = cursor.fetchone()

            return result[0] if result else 0
        except pymysql.MySQLError as e:
            print("Error counting filtered users:", e)
            return None
