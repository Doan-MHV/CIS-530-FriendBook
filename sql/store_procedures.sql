####---------------------------------------------------
### User
## Create
CREATE PROCEDURE CreateUser(
    IN p_userID INT,
    IN p_name VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_address VARCHAR(255),
    IN p_phoneNumber VARCHAR(20)
)
BEGIN
    INSERT INTO User (userID, name, email, address, phoneNumber)
    VALUES (
        p_userID,
        COALESCE(p_name, ''),
        COALESCE(p_email, ''),
        COALESCE(p_address, ''),
        COALESCE(p_phoneNumber, '')
    );
END;

## Select
CREATE PROCEDURE SelectAllUsers()
BEGIN
    SELECT * FROM User;
END;

CREATE PROCEDURE SelectFilteredUsers(
    IN p_userID INT,
    IN p_name VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_address VARCHAR(255),
    IN p_phoneNumber VARCHAR(20)
)
BEGIN
    SELECT *
    FROM User
    WHERE (userID = COALESCE(p_userID, userID))
      AND (name LIKE CONCAT('%', COALESCE(p_name, ''), '%'))
      AND (email = COALESCE(p_email, email))
      AND (address LIKE CONCAT('%', COALESCE(p_address, ''), '%'))
      AND (phoneNumber = COALESCE(p_phoneNumber, phoneNumber));
END;

CREATE PROCEDURE SelectFilteredUserContacts(
    IN p_userID INT,
    IN p_contactID INT,
    IN p_preferName VARCHAR(255),
    IN p_note VARCHAR(255)
)
BEGIN
    SELECT u.userID,
           u.name,
           u.email,
           u.address,
           u.phoneNumber,
           c.contactID,
           c.preferName,
           c.note
    FROM User u
             JOIN
         ContactList c ON u.userID = c.userID
    WHERE (u.userID = COALESCE(p_userID, u.userID))
      AND (c.contactID = COALESCE(p_contactID, c.contactID))
      AND (c.preferName LIKE CONCAT('%', COALESCE(p_preferName, ''), '%'))
      AND (c.note LIKE CONCAT('%', COALESCE(p_note, ''), '%'));
END;

### Update
CREATE PROCEDURE UpdateFilteredUsers(
    IN p_userID INT,
    IN p_new_userID INT,
    IN p_new_name VARCHAR(255),
    IN p_new_email VARCHAR(255),
    IN p_new_address VARCHAR(255),
    IN p_new_phoneNumber VARCHAR(20)
)
BEGIN
    UPDATE User
    SET userID      = COALESCE(p_new_userID, userID),
        name        = COALESCE(p_new_name, name),
        email       = COALESCE(p_new_email, email),
        address     = COALESCE(p_new_address, address),
        phoneNumber = COALESCE(p_new_phoneNumber, phoneNumber)
    WHERE (userID = COALESCE(p_userID, userID));
END;

### Delete
CREATE PROCEDURE DeleteFilteredUsers(
    IN p_userID INT,
    IN p_name VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_address VARCHAR(255),
    IN p_phoneNumber VARCHAR(20)
)
BEGIN
    DELETE
    FROM User
    WHERE (userID = COALESCE(p_userID, userID))
      AND (name LIKE CONCAT('%', COALESCE(p_name, ''), '%'))
      AND (email = COALESCE(p_email, email))
      AND (address LIKE CONCAT('%', COALESCE(p_address, ''), '%'))
      AND (phoneNumber = COALESCE(p_phoneNumber, phoneNumber));
END;

## Additional

CREATE PROCEDURE CountFilteredUsers(
    IN p_userID INT,
    IN p_name VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_address VARCHAR(255),
    IN p_phoneNumber VARCHAR(20)
)
BEGIN
    SELECT COUNT(*)
    FROM User
    WHERE (userID = COALESCE(p_userID, userID))
      AND (name LIKE CONCAT('%', COALESCE(p_name, ''), '%'))
      AND (email = COALESCE(p_email, email))
      AND (address LIKE CONCAT('%', COALESCE(p_address, ''), '%'))
      AND (phoneNumber = COALESCE(p_phoneNumber, phoneNumber));
END;

####---------------------------------------------------
### Contact List
## Create

CREATE PROCEDURE CreateContact(
    IN p_contactID INT,
    IN p_userID INT,
    IN p_preferName VARCHAR(255),
    IN p_note VARCHAR(255)
)
BEGIN
    INSERT INTO ContactList (contactID, userID, preferName, note)
    VALUES (
        p_contactID,
        p_userID,
        COALESCE(p_preferName, ''),
        COALESCE(p_note, '')
    );
END;

## Select

CREATE PROCEDURE SelectAllContacts()
BEGIN
    SELECT * FROM ContactList;
END;

CREATE PROCEDURE SelectFilteredContacts(
    IN p_contactID INT,
    IN p_userID INT,
    IN p_preferName VARCHAR(255),
    IN p_note VARCHAR(255)
)
BEGIN
    SELECT *
    FROM ContactList
    WHERE (contactID = COALESCE(p_contactID, contactID))
      AND (userID = COALESCE(p_userID, userID))
      AND (preferName LIKE CONCAT('%', COALESCE(p_preferName, ''), '%'))
      AND (note LIKE CONCAT('%', COALESCE(p_note, ''), '%'));
END;

## Update

CREATE PROCEDURE UpdateFilteredContacts(
    IN p_userID INT,
    IN p_contactID INT,
    IN p_new_userID INT,
    IN p_new_contactID INT,
    IN p_new_preferName VARCHAR(255),
    IN p_new_note VARCHAR(255)
)
BEGIN
    UPDATE ContactList
    SET userID     = COALESCE(p_new_userID, userID),
        contactID  = COALESCE(p_new_contactID, contactID),
        preferName = COALESCE(p_new_preferName, preferName),
        note       = COALESCE(p_new_note, note)
    WHERE (contactID = COALESCE(p_contactID, contactID))
      AND (userID = COALESCE(p_userID, userID));
END;

## Delete

CREATE PROCEDURE DeleteFilteredContacts(
    IN p_contactID INT,
    IN p_userID INT,
    IN p_preferName VARCHAR(255),
    IN p_note VARCHAR(255)
)
BEGIN
    DELETE
    FROM ContactList
    WHERE (contactID = COALESCE(p_contactID, contactID))
      AND (userID = COALESCE(p_userID, userID))
      AND (preferName LIKE CONCAT('%', COALESCE(p_preferName, ''), '%'))
      AND (note LIKE CONCAT('%', COALESCE(p_note, ''), '%'));
END;

## Additional

CREATE PROCEDURE CountFilteredContacts(
    IN p_userID INT,
    IN p_contactID INT,
    IN p_prefer_name VARCHAR(255),
    IN p_note VARCHAR(255)
)
BEGIN
    SELECT COUNT(*)
    FROM ContactList
    WHERE (userID = COALESCE(p_userID, userID))
      AND (contactID = COALESCE(p_contactID, contactID))
      AND (preferName = COALESCE(p_prefer_name, preferName))
      AND (note = COALESCE(p_note, note));
END;