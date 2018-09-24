from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
def index():
    return "Hello World"

    app.run()