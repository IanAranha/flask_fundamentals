from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def Dojo():
    return "DOJO"

@app.route("/say/<name>")
def say(name):
    return "Hi "+ name.capitalize()

@app.route("/repeat/<num>/<string>")
def repeat(num, string):
    return (string + " ") * int(num)



if __name__=="__main__":
    app.run(debug=True)
