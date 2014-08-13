.PHONY: app1 app2 db initial

app1:
	.virtualenv/bin/python app.py 1

app2:
	.virtualenv/bin/python app.py 2

db:
	sudo -Hnu postgres psql < db/users_and_tables.sql
	PGUSER=alice PGPASSWORD=wonderland psql test1 < db/test1.sql
	PGUSER=bob PGPASSWORD=ross psql test2 < db/test2.sql
	
initial: .virtualenv
	.virtualenv/bin/pip install -e flask_multidb

.virtualenv:
	virtualenv .virtualenv
