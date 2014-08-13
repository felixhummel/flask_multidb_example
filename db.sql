DROP DATABASE IF EXISTS test1;
DROP DATABASE IF EXISTS test2;
DROP USER IF EXISTS scott;

CREATE USER scott WITH PASSWORD 'tiger';
CREATE DATABASE test1 WITH OWNER scott;
CREATE DATABASE test2 WITH OWNER scott;