template = """drop table if exists profileids_bfsout_{};
create table profileids_bfsout_{} (
profileid integer primary key
);
copy profileids_bfsout_{} from '/tmp/output_{}.txt';
drop table if exists profiles_bfsjoined_{};
create table profiles_bfsjoined_{} as
select * from profiles inner join profileids_bfsout_{} using (profileid);"""
for ratio in [("0.01", "1"), ("0.10", "10"), ("0.15", "15"), ("0.20", "20")]:
	print(template.format(ratio[1], ratio[1], ratio[1], ratio[0], ratio[1], ratio[1], ratio[1]))
