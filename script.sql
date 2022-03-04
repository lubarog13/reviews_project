create database reviews;
CREATE USER 'review_admin'@'localhost' IDENTIFIED BY 'Password 123';
GRANT create, SELECT, alter ,INSERT, UPDATE, DELETE ON reviews.* TO 'review_admin'@'localhost';
flush privileges