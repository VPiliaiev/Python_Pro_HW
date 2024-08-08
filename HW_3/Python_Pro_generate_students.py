import csv
from flask import Flask
from faker import Faker
from webargs.flaskparser import use_kwargs
from webargs import validate, fields

app = Flask(__name__)


@app.route("/generate_students")
@use_kwargs(
    {
        "quantity": fields.Int(
            missing=1,
            validate=validate.Range(min=1, max=1000, min_inclusive=True, max_inclusive=True)
        )
    },
    location="query"
)
def generate_students(quantity):
    fake = Faker(locale='uk_UA')
    file_path = "students_data.csv"
    students_data = []
    for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime(' %d-%m-%Y')
        students_data.append([first_name, last_name, email, password, birthday])
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First name", "Last name", "Email", "Password", "Birthday"])
        writer.writerows(students_data)

    output = "First name, Last name, Email, Password, Birthday\n"
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        rows = [f"{row['First name']}, {row['Last name']}, {row['Email']}, {row['Password']}, {row['Birthday']}" for row
                in reader]
        output += "\n".join(rows)
    return "<pre>" + output + "</pre>"


if __name__ == '__main__':
    app.run(debug=True)
