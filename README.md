brew services start mysql
brew services stop mysql

mysql -u root -p
CREATE DATABASE mydatabase;
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON mydatabase.\* TO 'myuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
