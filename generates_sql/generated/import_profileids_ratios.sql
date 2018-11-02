drop table if exists profileids_bfsout_1;
create table profileids_bfsout_1 (
profileid integer primary key
);
copy profileids_bfsout_1 from '/tmp/output_0.01.txt';
drop table if exists profiles_bfsjoined_1;
create table profiles_bfsjoined_1 as
select * from profiles inner join profileids_bfsout_1 using (profileid);
drop table if exists profileids_bfsout_10;
create table profileids_bfsout_10 (
profileid integer primary key
);
copy profileids_bfsout_10 from '/tmp/output_0.10.txt';
drop table if exists profiles_bfsjoined_10;
create table profiles_bfsjoined_10 as
select * from profiles inner join profileids_bfsout_10 using (profileid);
drop table if exists profileids_bfsout_15;
create table profileids_bfsout_15 (
profileid integer primary key
);
copy profileids_bfsout_15 from '/tmp/output_0.15.txt';
drop table if exists profiles_bfsjoined_15;
create table profiles_bfsjoined_15 as
select * from profiles inner join profileids_bfsout_15 using (profileid);
drop table if exists profileids_bfsout_20;
create table profileids_bfsout_20 (
profileid integer primary key
);
copy profileids_bfsout_20 from '/tmp/output_0.20.txt';
drop table if exists profiles_bfsjoined_20;
create table profiles_bfsjoined_20 as
select * from profiles inner join profileids_bfsout_20 using (profileid);
