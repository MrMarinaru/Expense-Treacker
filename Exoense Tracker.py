import mysql.connector

while True:
    DB_choice = input('Name of Database to be used ➡️ ')

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mrinal@1311",
        database=DB_choice)
    cursor = connection.cursor()

    while True:
        def add_entry(no_of_records):
            #for i in no_of_records:
            cursor.execute(f"INSERT INTO expenses()")

    cursor.close()
    connection.close()