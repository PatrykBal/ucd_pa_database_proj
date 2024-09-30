from flask import Flask, render_template
from routes.forms import LoginForm, SignUpForm


from models import  Customer, Product, Cart, Order , db



app = Flask(__name__)
app.config.from_object('config')


with app.app_context():
     db.init_app(app)  
     db.create_all()
     print('Database Created')  



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
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/sign-up')
def sign_up():
    form = SignUpForm()

    return render_template('signup.html', form=form)




if __name__ == '__main__':
    app.run(debug=True)


