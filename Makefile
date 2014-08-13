app1:
	.virtualenv/bin/python app.py 1

app2:
	.virtualenv/bin/python app.py 2

db:
	sudo -Hnu postgres psql < db.sql
	
initial: .virtualenv
	.virtualenv/bin/pip install -e flask_multidb

.virtualenv:
	virtualenv .virtualenv
