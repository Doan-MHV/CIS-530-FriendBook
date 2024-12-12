import pymysql
from colorama import Fore, Style
from tabulate import tabulate


class ContactListFunctions:
    def __init__(self, connection):
        self.connection = connection

    def create_contact_list(self, user_id, contact_id, prefer_name, note):
        try:
            cursor = self.connection.cursor()
            cursor.callproc("CreateContact", (user_id, contact_id, prefer_name, note))
            self.connection.commit()
            print(
                f"{Fore.CYAN}Contact list for user '{user_id}' with '{contact_id}' created successfully!{Style.RESET_ALL}"
            )
        except pymysql.MySQLError as e:
            print("Error creating contact list:", e)

    def select_contacts(self):
        try:
            cursor = self.connection.cursor()
            cursor.callproc("SelectAllContacts")
            result = cursor.fetchall()
            headers = ["User ID", "Contact ID", "Preferred Name", "Note"]
            print(tabulate(result, headers, tablefmt="grid"))
        except pymysql.MySQLError as e:
            print("Error fetching contacts:", e)

    def select_filtered_contacts(
        self, user_id=None, contact_id=None, prefer_name=None, note=None
    ):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(
                "SelectFilteredContacts", (user_id, contact_id, prefer_name, note)
            )
            result = cursor.fetchall()
            headers = ["User ID", "Contact ID", "Preferred Name", "Note"]
            print(tabulate(result, headers, tablefmt="grid"))
        except pymysql.MySQLError as e:
            print("Error fetching filtered contacts:", e)

    def update_filtered_contact_lists(
        self,
        user_id=None,
        contact_id=None,
        new_user_id=None,
        new_contact_id=None,
        new_prefer_name=None,
        new_note=None,
    ):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(
                "UpdateFilteredContacts",
                (
                    user_id,
                    contact_id,
                    new_user_id,
                    new_contact_id,
                    new_prefer_name,
                    new_note,
                ),
            )
            self.connection.commit()
            print("Contacts updated successfully.")
        except pymysql.MySQLError as e:
            print("Error updating filtered contacts:", e)

    def delete_filtered_contact_lists(
        self, user_id=None, contact_id=None, prefer_name=None, note=None
    ):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(
                "DeleteFilteredContacts", (user_id, contact_id, prefer_name, note)
            )
            self.connection.commit()
            print("Contacts deleted successfully.")
        except pymysql.MySQLError as e:
            print("Error deleting filtered contacts:", e)

    def count_filtered_contacts(
        self, user_id=None, contact_id=None, prefer_name=None, note=None
    ):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(
                "CountFilteredContacts", (user_id, contact_id, prefer_name, note)
            )
            result = cursor.fetchone()

            return result[0] if result else 0
        except pymysql.MySQLError as e:
            print("Error counting filtered contacts:", e)
            return None
