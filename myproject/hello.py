from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/shiyanlou')
def helloshiyanlou():
    return 'Guohaobin'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/sum/<int:a>/<int:b>')
def sum_a_b(a,b):
    return '%d' % (a+b)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    #当请求形式为“GET”或者认证失败则执行以下代码
    return render_template('login.html', error=error)

@app.route('/upload', method=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))

if __name__ == '__main__':
    app.debug
    app.run()
