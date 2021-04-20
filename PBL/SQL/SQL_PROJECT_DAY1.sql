-- car 테이블
create table car(
car_id int not null auto_increment, 
car_type varchar(50) not null, # 자동차 종류
car_name varchar(50) not null, # 자동차 이름: 고객이 자동차 조회할 때 사용
primary key (car_id, car_type)); 

# car_type PK 조건 
# alter table car 
# change car_type car_type int not null primary key auto_increment;

select*from car;
desc car;

-- price 테이블: 자동차별 가격
create table price(
car_id int not null auto_increment, 
car_type varchar(50) not null,
price int not null,
foreign key (car_id,car_type) references car (car_id,car_type));

# PK와 FK 연결
# alter table price 
# add constraint price_fk foreign key(car_type)
# references car(car_type);

desc price;

-- 고객 정보
create table cus_info(
cus_id int not null primary key auto_increment,
cus_name varchar(50),
gender varchar(50),
age int not null);

desc cus_info;

-- 예약 정보 
create table reservation(
car_id int not null,
cus_id int not null,
from_time datetime not null, # 빌린 시간
to_time datetime not null, # 반납할 시간
foreign key (car_id) references car (car_id),
foreign key (cus_id) references cus_info (cus_id));

desc reservation;



-- 예약 시간 별 요금 정보 테이블 
create table timerate(
range_time int primary key auto_increment,
lohour int not null,
hihour int not null,
rate int not null);
 
desc timerate;

# SELECT TIMESTAMPDIFF(hour, '2018-03-28 23:59:59', '2018-03-29 12:59:59'); 시간계산






