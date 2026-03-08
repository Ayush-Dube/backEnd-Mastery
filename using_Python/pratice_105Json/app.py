from flask import Flask,request,render_template,jsonify
import json 

app = Flask(__name__)

FILE = 'someData.json'

@app.route('/')
def indexPage():
    return "HeHe1🌹"

@app.route('/add/<item>')
# request object demo
def addItem(item):
    print(request.method)
    print(request.headers)
    # print(request.json)
    return f"ok G {item} /n {FILE}"

@app.route('/one')
def onePage():
    try:
        with open(FILE,'r') as f :
            data = json.load(f)
            
        # return jsonify(data["items"][2])
        # return jsonify(data)
        return jsonify(data['items'])
    except Exception as e:
        return f"Error reading file:{e}"


@app.route('/usr')
def get_usr():
    return render_template('loginPage.html')

@app.route('/usr',methods=["POST"])
def showUsr():
    usrname =  request.form.get("username")
    phNo = request.form.get("phoneNumber")
    return f"{usrname}'s phone number is {phNo}"







if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

