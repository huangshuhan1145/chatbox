from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于 session 和 flash 消息

# 模拟用户数据库（生产环境应使用真实数据库）
users = {
    "admin": "123456",
}

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return render_template('welcome.html', username=username)
        else:
            flash("用户名或密码错误，请重试！")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash("用户名已存在，请选择其他用户名。")
            return redirect(url_for('register'))

        users[username] = password
        flash("注册成功，请登录。")
        return redirect(url_for('login'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
