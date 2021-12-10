import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test15.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# String variable for passing queries to cursor
query = """
    CREATE TABLE Student
    (studentID VARCHAR(4) PRIMARY KEY,
     fName VARCHAR(100) NOT NULL,
     lName VARCHAR(100) NOT NULL,
     initials VARCHAR(4) CONSTRAINT greaterThan1
	 CHECK (LENGTH(initials) > 1));
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# String variable for passing queries to cursor
query = """
    CREATE TABLE Major
    (majorID VARCHAR(4) PRIMARY KEY,
     majorName VARCHAR(100) NOT NULL,
     code VARCHAR(4) UNIQUE NOT NULL CONSTRAINT mustBe3 CHECK (LENGTH(code) = 3),
     deptName VARCHAR(100),
     FOREIGN KEY(deptName) REFERENCES Department ON DELETE CASCADE);

    
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# String variable for passing queries to cursor
query = """
    CREATE TABLE Department
    (deptName VARCHAR(100) PRIMARY KEY CONSTRAINT startDept
                                        CHECK (deptName LIKE 'Department%'),
     chairName VARCHAR(100) NOT NULL,
     noOfFaculty INT);

    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# String variable for passing queries to cursor
query = """
    CREATE TABLE Event
    (eventID VARCHAR(4) PRIMARY KEY,
     eventName VARCHAR(100) NOT NULL,
     startDate DATE,
     endDate DATE,
     CONSTRAINT startDateGreater
	    CHECK (startDate > '2021-12-08'),
     CONSTRAINT endDateGreater
	    CHECK (endDate > startDate));

    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# String variable for passing queries to cursor
query = """
    CREATE TABLE majorStudent
    (majorID VARCHAR(4),
     studentID VARCHAR(4),
     PRIMARY KEY(majorID, studentID),
     FOREIGN KEY(majorID) REFERENCES Major ON DELETE CASCADE,
     FOREIGN KEY(studentID) REFERENCES Student ON DELETE CASCADE);

    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# String variable for passing queries to cursor
query = """
    CREATE TABLE studentAttendance
    (studentID VARCHAR(4),
     eventID VARCHAR(4),
     PRIMARY KEY(studentID, eventID),
     FOREIGN KEY(studentID) REFERENCES Student ON DELETE CASCADE,
     FOREIGN KEY(eventID) REFERENCES Event ON DELETE CASCADE);

    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# String variable for passing queries to cursor
query = """
    CREATE TABLE departmentEvent
    (deptName VARCHAR(100),
     eventID VARCHAR(4),
     PRIMARY KEY(deptName, eventID),
     FOREIGN KEY(deptName) REFERENCES Department ON DELETE CASCADE,
     FOREIGN KEY(eventID) REFERENCES Event ON DELETE CASCADE);

    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# -------------------------- STUDENT INSERTS ------------------------------

# Insert row into table
query = """
    INSERT INTO Student
    Values ('S001', 'Nick', 'Sosnivka', 'NVS');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Student
    Values ('S002', 'Lionel', 'Messi', 'LM');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Student
    Values ('S003', 'Barry', 'Allen', 'BA');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Student
    Values ('S004', 'Julia', 'Sosnivka', 'JSS');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Student
    Values ('S005', 'Walter', 'White', 'WW');

    """
cursor.execute(query)

# -------------------------- DEPARTMENT INSERTS ----------------------------

# Insert row into table
query = """
    INSERT INTO Department
    VALUES ('Department of Physics', 'Albert Einstein', 15);

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Department
    VALUES ('Department of Mathematics', 'Isaac Newton', 10);

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Department
    VALUES ('Department of Engineering', 'Vanessa Aguiar', 26);

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Department
    VALUES ('Department of Psychology', 'Sigmund Freud', 32);

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Department
    VALUES ('Department of Business', 'Jordan Belfort', 51);

    """
cursor.execute(query)

# ----------------------------- EVENT INSERTS --------------------------------

# Insert row into table
query = """
    INSERT INTO Event
    VALUES ('E101', 'Homecoming', '2022-11-01', '2022-11-07');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Event
    VALUES ('E102', 'Parents Weekend', '2022-09-23', '2022-09-26');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Event
    VALUES ('E103', 'Welcome Week Festival', '2022-07-26', '2022-07-27');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Event
    VALUES ('E104', 'Canes Games', '2022-10-04', '2022-10-06');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Event
    VALUES ('E105', 'Easter Weekend', '2022-04-15', '2022-04-17');

    """
cursor.execute(query)

# ----------------------------- MAJOR INSERTS ---------------------------------

# Insert row into table
query = """
    INSERT INTO Major
    VALUES ('M001', 'Computer Science', 'CSC', 'Department of Engineering');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Major
    VALUES ('M002', 'Computer Engineering', 'CEG', 'Department of Engineering');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Major
    VALUES ('M006', 'Mathematics', 'MTH', 'Department of Mathematics');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Major
    VALUES ('M011', 'Psychology', 'PSY', 'Department of Psychology');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Major
    VALUES ('M020', 'Accounting', 'ACC', 'Department of Business');

    """
cursor.execute(query)

# --------------------------- MAJORSTUDENT INSERTS --------------------------------

# Insert row into table
query = """
    INSERT INTO majorStudent
    VALUES ('M002', 'S003');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO majorStudent
    VALUES ('M001', 'S001');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO majorStudent
    VALUES ('M006', 'S004');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO majorStudent
    VALUES ('M011', 'S002');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO majorStudent
    VALUES ('M020', 'S005');

    """
cursor.execute(query)

# --------------------------- STUDENTATTENDANCE INSERTS-------------------------

# Insert row into table
query = """
    INSERT INTO studentAttendance
    VALUES ('S004', 'E102');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO studentAttendance
    VALUES ('S002', 'E104');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO studentAttendance
    VALUES ('S001', 'E101');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO studentAttendance
    VALUES ('S003', 'E101');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO studentAttendance
    VALUES ('S005', 'E101');

    """
cursor.execute(query)

# -------------------------- DEPARTMENTEVENT INSERTS -----------------------------

# Insert row into table
query = """
    INSERT INTO departmentEvent
    VALUES ('Department of Business', 'E101');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO departmentEvent
    VALUES ('Department of Business', 'E105');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO departmentEvent
    VALUES ('Department of Psychology', 'E102');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO departmentEvent
    VALUES ('Department of Engineering', 'E104');

    """
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO departmentEvent
    VALUES ('Department of Mathematics', 'E103');

    """
cursor.execute(query)

# -------------------------- QUERIES ---------------------------------------

#a.	List all students and their names who attended the homecoming event

# Select data
query = """
    SELECT y.studentID, y.fName, y.lName
    FROM studentAttendance x, Student y, Event z
    WHERE x.studentID = y.studentID AND x.eventID = z.eventID AND z.eventName LIKE '%Homecoming%';

    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()

#b.	List all students and their names that study computer science.

# Select data
query = """
    SELECT z.studentID, z.fName, z.lName
    FROM majorStudent x, Major y, Student z
    WHERE x.majorID = y.majorID AND x.studentID = z.studentID AND y.majorName LIKE '%Computer Science%';

    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()

#c.	List the chair name in the department that oversees the computer science major

# Select data
query = """
    SELECT d.chairName, m.majorName
    FROM Department d, Major m
    WHERE d.deptName = m.deptName AND m.code LIKE 'CSC';

    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()

#d.	List the department name that hosts the homecoming event

# Select data
query = """
    SELECT d.deptName
    FROM departmentEvent d, Event e
    WHERE d.eventID = e.eventID AND e.eventName LIKE '%Homecoming';

    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()

#e.	Find the number of students studying finance

# Select data
query = """
    SELECT count(s.studentID)
    FROM majorStudent s, Major m
    WHERE s.majorID = m.majorID AND m.code LIKE 'PSY';

    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print()


# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
