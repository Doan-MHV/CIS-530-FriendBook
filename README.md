# Friend Book

## Installation

```
pip install -r requirements.txt
```

##### **Update MySQL Configuration**
The application connects to a MySQL database using the `pymysql` library. Update the database configuration in the `ContactDatabase` class to suit your server settings:
Open the file containing the connection settings (e.g., `main.py` file or equivalent) and locate the following code:

```python
self.connection = pymysql.connect(
    host="localhost",  # Replace with your database's hostname
    port=3307,  # Replace with your database's port (default is often 3306)
    user="root",  # Replace with your MySQL username
    password="docker",  # Replace with your MySQL password
    database="FriendBook",  # Replace with your database name
    charset="utf8mb4",  # Charset setting
)
```

##### **Table Creation and Data Seeding**

I included those files inside [sql folder](sql)