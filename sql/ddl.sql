CREATE SCHEMA IF NOT EXISTS FriendBook;

use FriendBook;

CREATE TABLE User
(
    userID      INT PRIMARY KEY,
    name        VARCHAR(255)        NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    address     VARCHAR(255),
    phoneNumber VARCHAR(20)
);

CREATE TABLE ContactList
(
    userID     INT NOT NULL,
    contactID  INT NOT NULL,
    preferName VARCHAR(255),
    note       VARCHAR(255),
    PRIMARY KEY (userID, contactID),
    FOREIGN KEY (userID) REFERENCES User (userID) ON DELETE CASCADE,
    FOREIGN KEY (contactID) REFERENCES User (UserID) ON DELETE CASCADE
);