from flask import Flask, render_template, redirect, request, session, flash
import random
import datetime

app = Flask(__name__)
app.secret_key = "Yankees Suck"

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
    if 'activity' not in session:
        session['activity'] = ''
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    message = []
    if request.form['building'] == 'farm':
        num = random.randrange(10, 21)
        session['total_gold'] += num
        right_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session['activity'] = "<p class='won'>You have earned {0} gold from the farm ({1})</p>".format(num, right_now)
    if request.form['building'] == 'cave':
        num = random.randrange(5, 11)
        session['total_gold'] += num
        flash("You have earned {} gold.".format(num))
    if request.form['building'] == 'house':
        num = random.randrange(2, 6)
        session['total_gold'] += num
        flash("You have earned {} gold.".format(num))
    if request.form['building'] == 'casino':
        num = random.randrange(-50, 51)
        session['total_gold'] += random.randrange(-50, 51)
        flash("You have earned {} gold.".format(num))
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
