use FriendBook;

# Data Seeding

####---------------------------------------------------

INSERT INTO User (userID, name, email, address, phoneNumber)
VALUES (1,'student 1', '1@example.com', '123 Cherry', '111-1234'),
       (2,'student 2', '2@example.com', '456 Orange', '222-5678'),
       (3,'student 3', '3@example.com', '789 Apple', '333-9012');

INSERT INTO ContactList (userID, contactID, preferName, note)
VALUES (1, 2, 'Orange', 'Met at CIS 530'),
       (1, 3, 'Apple', 'Met at CIS 530'),
       (2, 3, 'Apple', 'Met at CIS 530');


