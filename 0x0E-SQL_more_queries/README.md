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