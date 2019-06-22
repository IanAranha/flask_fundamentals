from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key="Yankess suck"

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register' , methods=['POST'])
def register():
    if len(request.form['first_name']) < 1:
        flash('Correct errors: First name cannot be blank')
    elif len(request.form['last_name']) < 1:
        flash('Correct errors: Last name cannot be blank')
    elif len(request.form['email']) < 1:
        flash('Correct errors: Email cannot be blank')
    elif len(request.form['password']) < 1:
        flash('Correct error: Password cannot be blank')
    elif len(request.form['password']) < 8:
        flash(u'Password must be 8 or more characters.', 'error')
    elif len(request.form['c_password']) < 1:
        flash('Please confirm password!')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash('Correct errors: First name can only contain alphabets')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash('Correct errors: Last name can only contain alphabets')
    elif request.form['password'] != request.form['c_password']:
        flash ('Passwords do not match')
        return redirect('/')
    else:
        return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
