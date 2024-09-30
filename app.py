from flask import Flask, render_template



app = Flask(__name__)
app.config['SECRET_KEY'] = ' dhuiqwhfudeiwf fewjfhiewf'





@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/men')
def men():
    return render_template('men-page.html')

@app.route('/women')
def women():
    return render_template('women-page.html')


@app.route('/login')
def login():
    return ' This is the login page'

@app.route('/sign-up')
def sign_up():
    return ' This is the sign-up page'




if __name__ == '__main__':
    app.run(debug=True)


