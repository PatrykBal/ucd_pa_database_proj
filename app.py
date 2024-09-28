from flask import Flask, render_template



app = Flask(__name__)
app.config['SECRET_KEY'] = ' dhuiqwhfudeiwf fewjfhiewf'




@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html')

@app.route('/login')
def login():
    return ' This is the login page'

@app.route('/sign-up')
def sign_up():
    return ' This is the sign-up page'




if __name__ == '__main__':
    app.run(debug=True)


