from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return "puppyWorl"

@app.route('/puppy/<name>')
def puppy_latin(name):
    # return "last letter : {}".format(name[-1])
    if name[-1].lower() !="y":
        return f"{name}y"

    else:
        newname = name[:-1]+"iful"
        return f"{newname,name}"


if __name__ == "__main__":
    app.run(debug="True")