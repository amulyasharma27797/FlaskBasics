from flask import Flask, render_template, flash, redirect, url_for

from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '768f736bc10e93de845f67884d7c80fa'


@app.route('/')
@app.route('/home/')
def home():
    return "Home Page"


@app.route('/about/')
def about():
    return "About Page"


@app.route('/greet/<name>')
def greet(name):
    return 'Good Morning: {}!'.format(name)


@app.route('/divide/<numerator>/<denominator>')
def divide(numerator, denominator):
    result = int(numerator) / int(denominator)
    return "{} / {} = {}".format(numerator, denominator, result)


@app.route('/contact/')
def contact():
    return render_template('contact.html')


fruit = [
        'apple',
        'banana',
        'pear',
        'oranges',
        'guava'
    ]


@app.route('/fruits/')
def fruits():
    return render_template('fruits.html', fruits=fruit)


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('about'))
    print(form.errors)
    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
