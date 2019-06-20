from flask import Flask, render_template, redirect, request, flash, session


app = Flask(__name__)
app.secret_key = "Yankees suck"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def show_results():
    print ("Got POST results")
    if len(request.form['name']) < 1:
        flash('Name cannot be blank')
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash('Comment cannot be blank')
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash('Comment cannot be more than 120 characters')
        return redirect('/')
    else:
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
