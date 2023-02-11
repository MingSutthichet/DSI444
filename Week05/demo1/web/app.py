from flask import Flask, jsonify
import datetime as dt
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!!'

@app.route('/date')
def count():
    x= dt.datetime.now()
    return jsonify(
        weekday=x.weekday(),
        day=x.day,
        month=x.month,
        year=x.year
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)