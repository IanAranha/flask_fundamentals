from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Yankees suck"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/destroy_session', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two', methods=['POST'])
def add_two():
    session['counter'] += 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
