from flask import Flask, render_template, redirect, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    order_total = 0
    strawberry_counter = 0
    strawberry_counter += int(request.form['strawberry'])
    raspberry_counter = 0
    raspberry_counter += int(request.form['raspberry'])
    apple_counter = 0
    apple_counter += int(request.form['apple'])
    order_total = strawberry_counter + raspberry_counter + apple_counter
    date1 = datetime.datetime.now().strftime("%a, %b %d, %Y %H:%M")
    return render_template('shoppingcart.html',
        s_counter = strawberry_counter,
        r_counter=raspberry_counter,
        a_counter=apple_counter,
        order_total=order_total,
        name=request.form['name'],
        id=request.form['id'],
        date_ordred = date1
        )


@app.route('/back', methods=['POST'])
def back():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
