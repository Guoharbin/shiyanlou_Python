from flask import Flask,request,redirect,url_for,session
app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return "Welcome, %s"%session['username']
    else:
        return "You are not logged in"

@app.route('/login', methods=['GET', 'POST'])
def login():                                    
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if session['username'] == 'shiyanlou' and session['password'] == 'shiyanlou':
            return redirect(url_for('index'))
        else: return "You entered wrong username or password"
    return """
    <form action="" method="post">
    <p><input type=text name=username>
    <p><input type=password name=password>
    <p><input type=submit value=login>
    </form>
    """

@app.route('/logout')
def logout():
    session.pop("username")
    session.pop("password")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
