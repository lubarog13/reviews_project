create database reviews;
CREATE USER 'review_admin'@'localhost' IDENTIFIED BY 'Password 123';
GRANT  ALL PRIVILEGES ON reviews.* TO 'review_admin'@'localhost';
flush privileges