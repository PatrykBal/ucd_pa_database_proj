from routes import app 




@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/login')
def login():
    return ' This is the login page'

@app.route('/sign-up')
def sign_up():
    return ' This is the sign-up page'




if __name__ == '__main__':
    app.run(debug=True)


