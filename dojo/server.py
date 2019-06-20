from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def show_results():
    print ("Got POST results")
    print(request.form['name'])
    print(request.form['dojo_location'])
    print(request.form['language'])
    print(request.form['comment'])
    return render_template('result.html',
    name = request.form['name'],
    dojo_location = request.form['dojo_location'],
    language = request.form['language'],
    comment = request.form['comment']
    )

@app.route('/return', methods=['POST'])
def back():
    return redirect('/')

@app.route('/danger')
def danger():
    print("A user tried to visit '/danger'. We have redirectd back to'/'")
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
