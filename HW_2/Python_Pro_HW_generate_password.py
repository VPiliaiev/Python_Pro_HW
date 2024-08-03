
from flask import Flask
import random
import string

app = Flask(__name__)


@app.route("/generate-password")
def generate_password():
    length = random.randint(10, 20)
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password += [random.choice(symbols) for i in range(length - 4)]
    password = ''.join(password)
    return password


if __name__ == '__main__':
    app.run(debug=True)

