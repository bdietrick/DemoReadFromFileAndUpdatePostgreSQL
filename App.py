import psycopg2
import csv

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="Demo",
    user="postgres",
    password="password"
)

# Create cursor object
cursor = conn.cursor()

# Uncomment to clear the tables
# cursor.execute("DELETE FROM \"Departments\";")
# cursor.execute("DELETE FROM \"Employees\";")
# conn.commit()



# Open the CSV file and insert the data into the database
with open('Departments.csv', mode='r', newline='') as departments:
    reader = csv.reader(departments)
    for record in reader:
        department_name = record
        print(department_name)
        # Insert the data into the "Departments" table
        cursor.execute("INSERT INTO \"Departments\" (\"DepartmentName\") VALUES (%s);", (department_name[0],))

# Open the CSV file and insert the data into the database
with open('Employees.csv', mode='r', newline='') as employees:
    reader = csv.reader(employees)
    for record in reader:
        first_name, last_name, department_id = record
        print(first_name, last_name, department_id)
        # Insert the data into the "Employees" table
        cursor.execute("INSERT INTO \"Employees\" (\"FirstName\",\"LastName\",\"DepartmentId\") VALUES (%s,%s,%s);", (first_name,last_name,department_id))  

# Commit the transactions
conn.commit()

# Query the Departments table
cursor.execute("SELECT * FROM \"Departments\";")
departments = cursor.fetchall()

for department in departments:
    print(department)


# Query the Employees table
cursor.execute("SELECT \"FirstName\",\"LastName\",\"DepartmentId\" FROM \"Employees\";")
employees = cursor.fetchall()

for employee in employees:
    first_name, last_name, department_id = employee
    print( first_name, last_name, department_id)


# Close the cursor and connection
cursor.close()
conn.close()
