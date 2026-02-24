from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Backend Beginnings!</h1> <br> <h2>Beautifully Built🌹</h2> <br> <a href='https://www.google.com'>abc</a>" 

@app.route('/one')
def one():
    return "<marquee direction='up'><h1>Hi one</h1></marquee>"


@app.route('/user/<username>')
def x(username):
    return f"🤖 : Hello  {username} ji!"

@app.route('/code')
def code():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)