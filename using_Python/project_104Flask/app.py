from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Backend Beginnings!</h1> <br> <h2>Beautifully Built🌹</h2> <br> <a href='https://www.google.com'>abc</a>" 

@app.route('/one')
def one():
    return "<marquee direction='up'><h1>Hi one</h1></ma rquee>"


@app.route('/user/<username>')
def x(username):
    return f"🤖 : Hello  {username} ji!"


@app.route('/code')
def code():
    return render_template('index.html')

@app.route('/fun')
def fun_page():
    return render_template('jinJaPage.html',name="Rambo")

@app.route('/items')
def db_item():
    return users

@app.route('/items/<usritem>')
def db_add(usritem):
    users.append(usritem)
    return users

users=['Apple','banana','cherry']


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
    # by default 5000 pr aa rha hoga, bcoz test server ki ek minimum requirment hoti hai .