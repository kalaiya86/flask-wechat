from app import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Account(db.Model):
    __tablename__ = 'app_accounts'
    id = db.Column(db.Integer, primary_key = True)
    appname = db.Column(db.String(30), index = True, unique = True)
    appid = db.Column(db.String(18), index = True, unique = True)
    appsecrit = db.Column(db.String(32), index = True, unique = True)
    access_token = db.Column(db.String(255), index = True)
    call_times = db.Column(db.SmallInteger, index = True)
    
    def __repr__(self):
        return '<Account %r>' % (self.appname)

class Menu(db.Model):
    __tablename__ = 'app_menus'
    id = db.Column(db.Integer, primary_key = True)
    button = db.Column(db.String(30), index = True, unique = True, nullable = False)
    sub_button = db.Column(db.String(30), index = True, unique = True)
    type = db.Column(db.String(30), index = True)
    name = db.Column(db.String(60), index = True, unique = True, nullable = False)
    key = db.Column(db.String(128))
    url = db.Column(db.Text(1024))
    media_id = db.Column(db.SmallInteger, index = True)
    
    def __repr__(self):
        return '<Menu %r>' % (self.appname)