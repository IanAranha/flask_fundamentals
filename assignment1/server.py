from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def level1():
    return render_template('index2.html')

@app.route('/play/<num>')
def level2(num):
    return render_template('index3.html', times=int(num))

@app.route('/play/<num>/<color>')
def level3(num, color):
    return render_template('index4.html', background=color, times=int(num))

if __name__ == "__main__":
    app.run(debug=True)
