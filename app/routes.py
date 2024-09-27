from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {
        "username": "Tosh"
    }
    posts = [
        {
            "author": {"username": "Tosh"},
            "body": "Beautiful day in Sacramento!"
        }, 
        {
            "author": {"username": "Serhii"},
            "body": "horrible day in Sacramento..."
        }
    ]
    return render_template("index.html", title="home", user=user, posts=posts)