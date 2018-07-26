# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, session
import config
from models import User, Question
from exts import db
from decorators import login_required

# 1
app = Flask(__name__)
# 2
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    context = {
        'questions': Question.query.order_by('-create_time').all()
    }
    return render_template('index.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        tel = request.form.get('tel')
        pwd = request.form.get('pwd')
        user = User.query.filter(User.telephone == tel, User.password == pwd).first()

        print tel
        print pwd
        if user:
            session['user_id'] = user.uid
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'手机号码或者密码错误，请确认后再登录.'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephone == telephone).first()

        if user:
            return u'该手机号码已被注册，请更换手机号码。'
        else:
            if password1 != password2:
                return u'两次密码不相同，请核对后重试。'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/question/', methods=["GET", "POST"])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.uid == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.uid == user_id).first()
        if user:
            return {'user': user}
    return {}


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
