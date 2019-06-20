from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name = "Ian")

@app.route('/success')
def success():
    return "SUCCESS!!"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello "+name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "Username: "+ username + " ID: "+ id

if __name__ == "__main__":
    app.run(debug = True)
