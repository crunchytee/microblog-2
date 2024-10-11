from urllib.parse import urlparse
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db, posts
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app.posts import Posts


@app.route('/')
@app.route('/index')
# @login_required
def index():
    return render_template("posts.html", posts=posts.get_posts(), title="Home | Posts")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        # flash("Login requested for user {}, remember_me={}".format(form.username.data, form.remember_me.data))
        user = User.query.filter_by(username=form.username.data).first()
        print(form.password.data)
        if user is None or not user.check_password(form.password.data):
            flash("invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlparse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(url_for('index'))
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You're registered!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)

@app.route("/posts")
def view_posts():
    return render_template("posts.html", posts=posts.get_posts(), title="Posts")

@app.route("/posts/<post_id>")
def view_post(post_id):
    post = posts.get_post(post_id)
    return render_template("post.html", post=post, post_id=post_id, title="Post")