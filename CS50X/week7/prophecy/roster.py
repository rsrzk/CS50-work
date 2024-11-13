import csv
from cs50 import SQL

db = SQL("sqlite:///roster2.db")

# Open CSV file
with open("students.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, adding to database
    for row in reader:
        student = row["student_name"]
        house = row["house"]
        add_student = db.execute("INSERT INTO students (student_name) VALUES(?)", student)
        houses = db.execute("SELECT house FROM houses")
        houses = [x["house"] for x in houses]
        if house not in houses:
            add_house = db.execute("INSERT INTO houses (house, head) VALUES(?, ?)", house, row["head"])
        student_id = db.execute("SELECT id FROM students WHERE student_name = ?", student)[0]["id"]
        house_id = db.execute("SELECT id FROM houses WHERE house = ?", house)[0]["id"]
        add_assignment = db.execute(
            "INSERT INTO assignments (student_id, house_id) VALUES(?,?)",
            student_id,
            house_id
        )