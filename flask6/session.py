from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Hello %s' %escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'shiyanlou' and request.form['password'] == 'shiyanlou':
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            return redirect(url_for('index'))
        else:
            error = "invalid username or password"
            return redirect(url_for('error', error=error))
    return '''
        <form action=="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

@app.route('/error/<error>')
def error(error):
    return render_template('error.html', error=error)


#app.secret_key = 'wing1995 is a very good girl'


if __name__ == '__main__':
    app.run()
