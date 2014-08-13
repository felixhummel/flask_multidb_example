"""
Example app for Flask-MultiDB extension.

Note that we use two completely different schemas (test1, test2) here.
"""
from flask import Flask
from flask_multidb import MultiDB


# first app
app1 = Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://alice:wonderland@localhost/test1'
multidb1 = MultiDB(app1)

# second app
app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bob:ross@localhost/test2'
multidb2 = MultiDB(app2)


@app1.route('/')
def index1():
    return multidb1.execute("select x from foo").scalar()


@app2.route('/')
def index2():
    return multidb2.execute("select x from foo").scalar()


if __name__ == "__main__":
    import sys
    assert sys.argv[1] in ['1', '2']
    i = int(sys.argv[1])
    appname = 'app{}'.format(i)
    app = globals()[appname]
    app.run(debug=True, port=(5000 + i))
