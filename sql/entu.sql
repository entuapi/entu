
create database entudb;
grant all on entudb.* to entuapp@'%' identified by '0000';
grant all on entudb.* to entuapp@'localhost' identified by '0000';
flush privileges;
use entudb;
source /home/kom/Documents/Aptana Studio 3 Workspace/entu/sql/create_tables.sql;
source /home/kom/Documents/Aptana Studio 3 Workspace/entu/sql/setup.sql;
insert into app_settings (keyname,value) values ('default_path','/entu');
insert into app_settings (keyname, value) values ('default_language','et');
