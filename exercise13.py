from flask import Flask
import json

app = Flask(__name__)

@app.route('/prime_number/<int:number>')

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)