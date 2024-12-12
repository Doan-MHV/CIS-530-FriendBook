import pymysql
from PyInquirer import prompt
from colorama import Fore, Style

from constants import (
    TABLE_SELECTION_PROMPT,
    USER_OPERATIONS_PROMPT,
    USER_FILTER_PROMPTS,
    USER_UPDATE_PROMPTS,
    CONTACT_OPERATIONS_PROMPT,
    CHECK_USER_EXISTS_PROMPT,
    USER_CREATE_PROMPTS,
    USER_FILTER_WITH_CONTACT_LIST_PROMPTS,
    CHECK_CONTACT_EXISTS_PROMPT,
    CONTACT_CREATE_PROMPTS,
    CONTACT_FILTER_PROMPTS,
    CHECK_USER_CONTACT_EXISTS_PROMPT,
    CONTACT_UPDATE_PROMPTS,
)
from contact_list import ContactListFunctions
from user import UserFunctions


class ContactDatabase:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host="localhost",
                port=3307,
                user="root",
                password="docker",
                database="FriendBook",
                charset="utf8mb4",
            )
            print(f"{Fore.GREEN}Connection established successfully.{Style.RESET_ALL}")
        except pymysql.MySQLError as e:
            print(f"{Fore.RED}Error while connecting to MySQL: {e}{Style.RESET_ALL}")
            self.connection = None

    def close_connection(self):
        if self.connection and self.connection.open:
            self.connection.close()
            print(f"{Fore.YELLOW}Connection closed.{Style.RESET_ALL}")


def main():
    db = ContactDatabase()
    user_funcs = UserFunctions(db.connection)
    contact_funcs = ContactListFunctions(db.connection)

    try:
        while True:
            answers = prompt(TABLE_SELECTION_PROMPT)
            selected_table = answers["table"]

            if selected_table == "Exit":
                print(
                    f"{Fore.BLUE}Exiting the application. Have a great day!{Style.RESET_ALL}"
                )
                break

            if selected_table == "User":
                while True:
                    user_operation = prompt(USER_OPERATIONS_PROMPT)["operation"]

                    if user_operation == "Create User":
                        print(
                            f"{Fore.CYAN}Please provide user details to create a new user.{Style.RESET_ALL}"
                        )
                        while True:
                            while True:
                                user_id = prompt([CHECK_USER_EXISTS_PROMPT])
                                user_count = user_funcs.count_filtered_users(
                                    user_id=int(user_id["user_id"])
                                )
                                if user_count > 0:
                                    print(
                                        f"{Fore.RED}The User ID '{user_id['user_id']}' already exists. Please enter a different User ID.{Style.RESET_ALL}"
                                    )
                                    continue
                                else:
                                    break

                            user_create_details = prompt(USER_CREATE_PROMPTS)

                            user_funcs.create_user(
                                user_id=int(user_id["user_id"]),
                                name=user_create_details["name"],
                                email=user_create_details["email"],
                                address=user_create_details["address"],
                                phone_number=user_create_details["phone_number"],
                            )
                            break

                    elif user_operation == "View All Users":
                        user_funcs.select_users()

                    elif user_operation == "Filter Users":
                        filters = prompt(USER_FILTER_PROMPTS)
                        print(
                            f"{Fore.CYAN}Applying filters for users. Please wait...{Style.RESET_ALL}"
                        )
                        user_funcs.select_filtered_users(
                            user_id=filters["user_id"] or None,
                            name=filters["name"] or None,
                            email=filters["email"] or None,
                            address=filters["address"] or None,
                            phone_number=filters["phone_number"] or None,
                        )

                    elif user_operation == "View Users with Contact List":
                        filters = prompt(USER_FILTER_WITH_CONTACT_LIST_PROMPTS)
                        print(
                            f"{Fore.CYAN}Fetching user contacts. Please wait...{Style.RESET_ALL}"
                        )
                        user_funcs.select_filtered_user_contacts(
                            user_id=filters["user_id"] or None,
                            contact_id=filters["contact_id"] or None,
                            prefer_name=filters["prefer_name"] or None,
                            note=filters["note"] or None,
                        )

                    elif user_operation == "Update Users":
                        while True:
                            user_id_details = prompt([CHECK_USER_EXISTS_PROMPT])
                            user_count = user_funcs.count_filtered_users(
                                user_id=int(user_id_details["user_id"])
                            )
                            if user_count == 0:
                                print(
                                    f"{Fore.RED}The User ID '{user_id_details['user_id']}' does not exist. Please enter a valid User ID.{Style.RESET_ALL}"
                                )
                                continue
                            else:
                                break

                        user_update_details = prompt(USER_UPDATE_PROMPTS)
                        print(
                            f"{Fore.CYAN}Updating user details. Please wait...{Style.RESET_ALL}"
                        )
                        user_funcs.update_filtered_users(
                            user_id=int(user_id_details["user_id"]),
                            new_user_id=user_update_details["new_user_id"] or None,
                            new_name=user_update_details["new_name"] or None,
                            new_email=user_update_details["new_email"] or None,
                            new_address=user_update_details["new_address"] or None,
                            new_phone_number=user_update_details["new_phone_number"]
                            or None,
                        )

                    elif user_operation == "Delete Users":
                        filters = prompt(USER_FILTER_PROMPTS)
                        print(f"{Fore.RED}Deleting filtered users.{Style.RESET_ALL}")
                        user_funcs.delete_filtered_users(
                            user_id=filters["user_id"] or None,
                            name=filters["name"] or None,
                            email=filters["email"] or None,
                            address=filters["address"] or None,
                            phone_number=filters["phone_number"] or None,
                        )

                    elif user_operation == "Count Filtered Users":
                        filters = prompt(USER_FILTER_PROMPTS)
                        count = user_funcs.count_filtered_users(
                            user_id=filters["user_id"] or None,
                            name=filters["name"] or None,
                            email=filters["email"] or None,
                            address=filters["address"] or None,
                            phone_number=filters["phone_number"] or None,
                        )
                        print(
                            f"{Fore.CYAN}Filtered Users Count: {count}{Style.RESET_ALL}"
                        )

                    elif user_operation == "Back":
                        print(
                            f"{Fore.YELLOW}Going back to table selection.{Style.RESET_ALL}"
                        )
                        break

            elif selected_table == "ContactList":
                while True:
                    contact_operation = prompt(CONTACT_OPERATIONS_PROMPT)["operation"]

                    if contact_operation == "Create Contact":
                        print(
                            f"{Fore.CYAN}Please provide contact details to create a new contact.{Style.RESET_ALL}"
                        )

                        while True:
                            user_id_input = prompt([CHECK_USER_EXISTS_PROMPT])
                            user_id = user_id_input["user_id"]
                            user_count = user_funcs.count_filtered_users(
                                user_id=user_id
                            )
                            if user_count == 0:
                                print(
                                    f"{Fore.RED}User ID '{user_id}' does not exist{Style.RESET_ALL}"
                                )
                                continue
                            break

                        while True:
                            contact_id_input = prompt([CHECK_CONTACT_EXISTS_PROMPT])
                            contact_id = contact_id_input["contact_id"]

                            if user_id == contact_id:
                                print(
                                    f"{Fore.RED}User ID and Contact ID cannot be the same. Please enter different values.{Style.RESET_ALL}"
                                )
                                continue

                            contact_user_count = user_funcs.count_filtered_users(
                                user_id=contact_id
                            )

                            if contact_user_count == 0:
                                print(
                                    f"{Fore.RED}User Contact ID '{contact_id}' does not exist{Style.RESET_ALL}"
                                )
                                continue

                            break

                        # Prompt for additional contact details
                        contact_details = prompt(CONTACT_CREATE_PROMPTS)

                        contact_funcs.create_contact_list(
                            user_id=user_id,
                            contact_id=contact_id,
                            prefer_name=contact_details["prefer_name"] or None,
                            note=contact_details["note"] or None,
                        )

                    elif contact_operation == "View All Contacts":
                        contact_funcs.select_contacts()

                    elif contact_operation == "Filter Contacts":
                        filters = prompt(CONTACT_FILTER_PROMPTS)
                        print(
                            f"{Fore.CYAN}Fetching contacts. Please wait...{Style.RESET_ALL}"
                        )
                        contact_funcs.select_filtered_contacts(
                            user_id=filters["user_id"] or None,
                            contact_id=filters["contact_id"] or None,
                            prefer_name=filters["prefer_name"] or None,
                            note=filters["note"] or None,
                        )
                    elif contact_operation == "Update Contact":
                        while True:
                            user_contact_input = prompt(
                                CHECK_USER_CONTACT_EXISTS_PROMPT
                            )

                            user_id = user_contact_input["user_id"]
                            contact_id = user_contact_input["contact_id"]

                            contact_count = contact_funcs.count_filtered_contacts(
                                user_id=user_id, contact_id=contact_id
                            )

                            if contact_count == 0:
                                print(
                                    f"{Fore.RED}Contact with User ID '{user_id}' and Contact ID '{contact_id}' does not exist.{Style.RESET_ALL}"
                                )
                                continue
                            break

                        update_input = prompt(CONTACT_UPDATE_PROMPTS)

                        contact_funcs.update_filtered_contact_lists(
                            user_id=user_id,
                            contact_id=contact_id,
                            new_user_id=update_input.get("new_user_id"),
                            new_contact_id=update_input.get("new_contact_id"),
                            new_prefer_name=update_input.get("new_prefer_name"),
                            new_note=update_input.get("new_note"),
                        )

                        print(
                            f"{Fore.GREEN}Contact updated successfully!{Style.RESET_ALL}"
                        )

                    elif contact_operation == "Delete Contacts":
                        filters = prompt(CONTACT_FILTER_PROMPTS)
                        print(f"{Fore.RED}Deleting filtered contacts.{Style.RESET_ALL}")
                        contact_funcs.delete_filtered_contact_lists(
                            user_id=filters["user_id"] or None,
                            contact_id=filters["contact_id"] or None,
                            prefer_name=filters["prefer_name"] or None,
                            note=filters["note"] or None,
                        )

                    elif contact_operation == "Count Filtered Contacts":
                        filters = prompt(CONTACT_FILTER_PROMPTS)
                        count = contact_funcs.count_filtered_contacts(
                            user_id=filters["user_id"] or None,
                            contact_id=filters["contact_id"] or None,
                            prefer_name=filters["prefer_name"] or None,
                            note=filters["note"] or None,
                        )
                        print(
                            f"{Fore.CYAN}Filtered Contacts Count: {count}{Style.RESET_ALL}"
                        )

                    elif contact_operation == "Back":
                        print(
                            f"{Fore.YELLOW}Going back to table selection.{Style.RESET_ALL}"
                        )
                        break

    finally:
        db.close_connection()


if __name__ == "__main__":
    main()
