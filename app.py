from flask import Flask #Import the Flask class from the flask module

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello DevOps World from FA22-BCS-085"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)