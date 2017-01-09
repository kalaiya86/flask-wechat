from app import app
from flask import render_template
# from flask_bootstrap import Bootstrap


# bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'} # fake user
    posts = [# fake array of posts
        {
            'arender_templateuthor': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)
