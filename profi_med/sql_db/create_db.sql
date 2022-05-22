CREATE DATABASE baza;
CREATE USER azamat WITH PASSWORD 'qwe123';
ALTER ROLE azamat SET client_encoding TO 'utf-8';
ALTER ROLE azamat SET default_transaction_isolation TO 'read committed';
ALTER ROLE azamat SET timezone TO 'Asia/Bishkek';
GRANT ALL PRIVILEGES ON DATABASE baza TO azamat;