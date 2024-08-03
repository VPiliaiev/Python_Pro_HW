from flask import Flask
import csv


app = Flask(__name__)


@app.route("/calculate-average")
def calculate_average():
    file_path = "/Users/valeriypilyaev/Desktop/Python_Pro/Python_Pro_HW/Python_Pro_HW/HW_2/hw.csv"
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [field.strip() for field in reader.fieldnames]
        data = [row for row in reader]

    heights = [float(row['Height(Inches)']) for row in data]
    weights = [float(row['Weight(Pounds)']) for row in data]

    average_height = sum(heights) / len(heights)
    average_weight = sum(weights) / len(weights)
    result = f"Average Height: {average_height}, Average Weight: {average_weight}"
    return result


if __name__ == '__main__':
    app.run(debug=True, port=5001)


