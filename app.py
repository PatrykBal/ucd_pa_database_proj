from flask import Flask, render_template, flash, redirect
from routes.forms import LoginForm, SignUpForm, PasswordChangeForm
from flask_login import login_user, login_required, logout_user
from flask_login import LoginManager

from models import  Customer, Product, Cart, Order , db



app = Flask(__name__)
app.config.from_object('config')


#with app.app_context():
db.init_app(app)  
    #db.create_all()
    #print('Database Created') 


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'app.login'


@login_manager.user_loader
def load_user(id):
        return Customer.query.get(int(id))




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




@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        customer = Customer.query.filter_by(email=email).first()

        if customer:
            if customer.verify_password(password=password):
                login_user(customer)
                return redirect('/')
            else:
                flash('Incorrect Email or Password')

        else:
            flash('Account does not exist please Sign Up')

    return render_template('login.html', form=form)



@app.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    return redirect('/')



@app.route('/profile/<int:customer_id>')
@login_required
def profile(customer_id):
    customer = Customer.query.get(customer_id)
    return render_template('profile.html', customer=customer)

    

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password1 = form.password1.data
        password2 = form.password2.data

        if password1 == password2:
            new_customer = Customer()
            new_customer.email = email
            new_customer.username = username
            new_customer.password = password2

            try:
                db.session.add(new_customer)
                db.session.commit()
                flash('Account Created Successfully, You can now Login')
                return redirect('/login')
            except Exception as e:
                print(e)
                flash('Account Not Created!!, Email already exists')

            form.email.data = ''
            form.username.data = ''
            form.password1.data = ''
            form.password2.data = ''

    return render_template('signup.html', form=form)



@app.route('/change-password/<int:customer_id>', methods=['GET', 'POST'])
@login_required
def change_password(customer_id):
    form = PasswordChangeForm()
    customer = Customer.query.get(customer_id)
    if form.validate_on_submit():
        current_password = form.current_password.data
        new_password = form.new_password.data
        confirm_new_password = form.confirm_new_password.data

        if customer.verify_password(current_password):
            if new_password == confirm_new_password:
                customer.password = confirm_new_password
                db.session.commit()
                flash('Password Updated Successfully')
                return redirect(f'/profile/{customer.id}')
            else:
                flash('New Passwords do not match!!')

        else:
            flash('Current Password is Incorrect')

    return render_template('change-password.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)


