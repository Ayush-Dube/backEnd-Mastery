
from flask import Flask, request,jsonify,render_template
import json

app = Flask(__name__)

FILE = 'aircrafts.json'

@app.route("/")
def home():
    print("REQUEST FROM:", request.remote_addr)
    return "ok"


@app.route("/all")
def allAircgrafts():

   with open(FILE,'r') as f:
    data = json.load(f)

    # return jsonify(data[0]["name"])
    maal = []
    dictA={}
    for i in  data :
        maal.append(i["name"])
        

    return jsonify(maal)

@app.route("/query")
def showQuery():
    all_q = request.args    
    print(all_q)
    return "see"
        
    
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)