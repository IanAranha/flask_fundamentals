from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<x>/<y>')
def index2(x,y):
    return render_template('index2.html', a=int(x), b=int(y))

if __name__ == '__main__':
    app.run(debug=True)
