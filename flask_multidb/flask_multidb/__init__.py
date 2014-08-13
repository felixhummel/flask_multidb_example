"""
Flask-MultiDB
=============

Proof-of-Concept Flask Extension that can utilize multiple database
connections which are provided by Flask-SQLAlchemy.
"""


class MultiDB(object):

    def __init__(self, app=None, db=None):
        self.app = app
        self.db = db
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if self.db is None:
            from flask.ext.sqlalchemy import SQLAlchemy
            self.db = SQLAlchemy(app)

    def execute(self, *args, **kwargs):
        return self.db.engine.execute(*args, **kwargs)
