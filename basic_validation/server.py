from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = "Yankees Suck"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash('Name cannot be blank')
    else:
        flash(f"Success! Your name is {request.form['name']}.")

    if len(request.form['email']) < 1:
        flash('Email cannot be blank')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email')
    else:
        flash('Success')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
