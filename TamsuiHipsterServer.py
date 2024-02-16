from flask import Flask, request
from message_to_MySQL import update

app = Flask(__name__)

@app.route("/")
def test():
    return 'successful'

@app.route("/message", methods=['POST'])
def message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    update(name, email, message)
    print("{}, {}, {}".format(name, email, message))
    return ''

if __name__ == "__main__":
    app.run()
