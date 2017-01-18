import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
#表单配置
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
#数据库配置
# SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# MYSQL_DB = 'sqlalchemy_migratetest'
# MYSQL_USER = 'root'
# MYSQL_PASSWD = 'dewei'
# MYSQL_HOST = 'localhost'
# MYSQL_POST = 3306
# SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s:%s/%s?charset=utf8" % (MYSQL_USER, MYSQL_PASSWD, MYSQL_HOST, MYSQL_POST, MYSQL_DB)
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')