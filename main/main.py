import sqlite3

# ----------------- DATABASE -------------------------------
# Rev: I might move this to a separate file so that we can just import it
#      and use all of its methods, similar to class. Gagawin kong OOP.

# Connect to the HotelManagement.db
connection = sqlite3.connect('../HotelManagementDB/HotelManagement.db')

# SQL Statement
strSQL = "SQL Statement Here!"

# Execute methods that run the SQL Query
cursor = connection.execute(strSQL)

# Fetches/Gets/Retrieves all of the records on the database from the cursor
# (Depending on the SQL Statement)
# rows = Instance of a Record
rows = cursor.fetchall()


# Closes the cursor that gets the SQL QUERIES and Holds the Record/List of Records
cursor.close()
# Closes the connection to the Database
connection.close()
# ----------------- DATABASE -------------------------------

# ------------------ START UI BELOW ------------------------