from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return 'test'

@app.route('/')
def default():
    return 'Welcome to Blockchain'

app.run(port=5001)

