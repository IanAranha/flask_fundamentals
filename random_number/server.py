from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Yankees Suck"

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randrange(0, 101)
    else:
        session.clear()
        session['num'] = random.randrange(0, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    print(session['num'])
    if session['num'] == int(request.form['number']):
        return redirect('/correct')
    if session['num'] > int(request.form['number']):
        return redirect('/low')
    if session['num'] < int(request.form['number']):
        return redirect('/high')

@app.route('/correct' , methods=['GET'])
def correct():
    return render_template('correct.html')

@app.route('/restart', methods=['POST'])
def restart():
    session.clear()
    return redirect('/')

@app.route('/low', methods=['GET'])
def low():
    return render_template('low.html')

@app.route('/high', methods=['GET'])
def high():
    return render_template('high.html')



if __name__ == '__main__':
    app.run(debug=True)
