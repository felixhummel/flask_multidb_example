from setuptools import setup


setup(
    name='flask-multidb',
    version='1.0.0',
    packages=['flask_multidb'],
    install_requires=[
        'flask',  # http://flask.pocoo.org/
        'SQLAlchemy',  # http://docs.sqlalchemy.org/
        'Flask-SQLAlchemy',  # https://pypi.python.org/pypi/Flask-SQLAlchemy
        'psycopg2',  # https://pypi.python.org/pypi/sqlparse
    ]
)
