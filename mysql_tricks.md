# MySQL

## Dump DB

```sh
mysqldump --opt --host=0.0.0.0 --user=root -ppassword db_name > ../backupDB/backup2020.sql
```

## Reset primary key to 1

```sh
ALTER TABLE tbl AUTO_INCREMENT = 1;
```

## Quick create user and DB

```sh
CREATE USER "admin"@"localhost" IDENTIFIED BY "admin";
CREATE DATABASE demo CHARACTER SET utf8;
GRANT ALL ON demo.* to admin@localhost;
FLUSH PRIVILEGES;
```

## Change root password

```sh
ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';
```

## Disable foreign key check to be able to truncate DB

```sh
SET foreign_key_checks = 0;
```
