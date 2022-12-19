Database Installation and Commands on UBUNTU 20.4
Installatiom
Install MySQL Server
$ sudo apt install mysql-server
Setup and Commands
Set password for the first time
$ mysqladmin -u root password NEWPASSWORD
Change existing Password
$ sudo mysql ALTER USER 'root'@'localhost' IDENTIFIED BY 'PASSWORD';
$ sudo systemctl stop mysql
$ sudo mysqld -init-file=~/mysql-pwd
$ sudo systemctl start mysql
Import dumb table into a database
$ mysql -u root -p 'database_name' < 'filename.sql'
Download file online
$ wget 'https://web_address.com'/filename
Enter mysql prompt
$ mysql -u root -p
Create New MySQL User
mysql> CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
Create New MySQL User with mysql_native_password
mysql> CREATE USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
Alter MySQL User with mysql_native_password
mysql> ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
Granting a User Permissions
mysql> GRANT PRIVILEGE ON database.table TO 'username'@'host';
mysql> GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
Granting All privileges to a User
mysql> GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
Reload grant table to effect new privileges
mysql> FLUSH PRIVILEGES;
Revoke a permission
mysql> REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';
Review a User permissions
mysql> SHOW GRANTS FOR 'username'@'host';
Delete a User
mysql> DROP USER 'username'@'localhost';
Exit MySQL clint
mysql> exit
New User log in
$ mysql -u username -p
Usage	Command
Usage Example	$ cat 0-list_databases.sql | mysql -uroot -p

https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221130%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221130T131059Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=70ae222a1a3854c1d86f82a609a6a6cd25d5b0ae1a11a1b6039df8ccb2d4d207