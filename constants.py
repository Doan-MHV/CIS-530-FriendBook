CHECK_USER_EXISTS_PROMPT = {
    "type": "input",
    "name": "user_id",
    "message": "Enter a User ID:",
}

CHECK_CONTACT_EXISTS_PROMPT = {
    "type": "input",
    "name": "contact_id",
    "message": "Enter a User Contact ID:",
}

CHECK_USER_CONTACT_EXISTS_PROMPT = [
    {
        "type": "input",
        "name": "user_id",
        "message": "Enter User ID:",
    },
    {
        "type": "input",
        "name": "contact_id",
        "message": "Enter Contact ID:",
    },
]

USER_CREATE_PROMPTS = [
    {
        "type": "input",
        "name": "name",
        "message": "Enter name:",
    },
    {
        "type": "input",
        "name": "email",
        "message": "Enter email:",
    },
    {
        "type": "input",
        "name": "address",
        "message": "Enter address:",
    },
    {
        "type": "input",
        "name": "phone_number",
        "message": "Enter phone number:",
    },
]

CONTACT_CREATE_PROMPTS = [
    {
        "type": "input",
        "name": "prefer_name",
        "message": "Enter Preferred Name:",
    },
    {
        "type": "input",
        "name": "note",
        "message": "Enter Note:",
    },
]

USER_FILTER_PROMPTS = [
    {"type": "input", "name": "user_id", "message": "Enter User ID (or leave blank):"},
    {"type": "input", "name": "name", "message": "Enter Name (or leave blank):"},
    {"type": "input", "name": "email", "message": "Enter Email (or leave blank):"},
    {"type": "input", "name": "address", "message": "Enter Address (or leave blank):"},
    {
        "type": "input",
        "name": "phone_number",
        "message": "Enter Phone Number (or leave blank):",
    },
]

CONTACT_FILTER_PROMPTS = [
    {"type": "input", "name": "user_id", "message": "Enter User ID (or leave blank):"},
    {
        "type": "input",
        "name": "contact_id",
        "message": "Enter Contact ID (or leave blank):",
    },
    {
        "type": "input",
        "name": "prefer_name",
        "message": "Enter Preferred Name (or leave blank):",
    },
    {"type": "input", "name": "note", "message": "Enter Note (or leave blank):"},
]

USER_FILTER_WITH_CONTACT_LIST_PROMPTS = [
    {"type": "input", "name": "user_id", "message": "Enter User ID (or leave blank):"},
    {
        "type": "input",
        "name": "contact_id",
        "message": "Enter Contact ID (or leave blank):",
    },
    {
        "type": "input",
        "name": "prefer_name",
        "message": "Enter Preferred Name (or leave blank):",
    },
    {
        "type": "input",
        "name": "note",
        "message": "Enter Note (or leave blank):",
    },
]

USER_UPDATE_PROMPTS = [
    {
        "type": "input",
        "name": "new_user_id",
        "message": "Enter New User ID (or leave blank):",
    },
    {
        "type": "input",
        "name": "new_name",
        "message": "Enter New Name (or leave blank):",
    },
    {
        "type": "input",
        "name": "new_email",
        "message": "Enter New Email (or leave blank):",
    },
    {
        "type": "input",
        "name": "new_address",
        "message": "Enter New Address (or leave blank):",
    },
    {
        "type": "input",
        "name": "new_phone_number",
        "message": "Enter New Phone Number (or leave blank):",
    },
]

CONTACT_UPDATE_PROMPTS = [
    {
        "type": "input",
        "name": "new_user_id",
        "message": "Enter new User ID (Leave blank for no change):",
    },
    {
        "type": "input",
        "name": "new_contact_id",
        "message": "Enter new Contact ID (Leave blank for no change):",
    },
    {
        "type": "input",
        "name": "new_prefer_name",
        "message": "Enter new Preferred Name (Leave blank for no change):",
    },
    {
        "type": "input",
        "name": "new_note",
        "message": "Enter new Note (Leave blank for no change):",
    },
]

USER_OPERATIONS_PROMPT = [
    {
        "type": "list",
        "name": "operation",
        "message": "Select the operation:",
        "choices": [
            "Create User",
            "View All Users",
            "Filter Users",
            "View Users with Contact List",
            "Update Users",
            "Delete Users",
            "Count Filtered Users",
            "Back",
        ],
    }
]

TABLE_SELECTION_PROMPT = [
    {
        "type": "list",
        "name": "table",
        "message": "Which table do you want to choose?",
        "choices": ["User", "ContactList", "Exit"],
    }
]

CONTACT_OPERATIONS_PROMPT = [
    {
        "type": "list",
        "name": "operation",
        "message": "Select the operation:",
        "choices": [
            "Create Contact",
            "View All Contacts",
            "Filter Contacts",
            "Update Contact",
            "Delete Contact",
            "Count Filtered Contacts",
            "Back",
        ],
    }
]
