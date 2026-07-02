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
    # return render_template('animate.html')
    return render_template('loginPage.html')

@app.route('/usr',methods=["POST"])
def showUsr():
    usrname =  request.form.get("username")
    phNo = request.form.get("phoneNumber")
    return f"{usrname}'s phone number is {phNo}"


# =====================DEMO OF JSON FILE==============================
# READ & WRITE FUNCTIONS

def read_data():
    with open(FILE,"r") as f:
        return json.load(f)

def write_data(dataMaal):
    with open (FILE,"w") as f:
        json.dump(dataMaal,f) 
# Observe it does not return , it performs a writing function , to see effect read the data(newly)

# ROUTES
@app.route("/data")
def get_items():
    substance = read_data()
    # return substance
    return substance["items"]
    # return substance["items"][1]

@app.route("/data/add/<item>")
def add_show_items(item):
    maal = read_data()
    maal["items"].append(item)
    write_data(maal)
    return f"Ur item:{item} was succesfully added. To chk visit /data"






if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

