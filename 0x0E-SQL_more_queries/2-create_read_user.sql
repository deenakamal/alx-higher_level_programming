-- creates the database hbtn_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IS NOT EXISTS "user_0d_2"@"localhots" IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
