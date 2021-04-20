-- database
use sql_project;
show tables;

-- 고객별 총 요금 계산하기
# 세타조인 활용
select X.customer 고객명, X.carName 자동차,  X.diff 빌린시간, (X.diff*Y.rate)+X.car_price 총요금
from(select cus.cus_name customer, c.car_name carName, p.price car_price, timestampdiff(hour, from_time, to_time) diff
      from reservation res 
      join car c on res.car_id = c.car_id
      join cus_info cus on res.cus_id = cus.cus_id
      join price p on res.car_id = p.car_id) X, timerate as Y
where X.diff between Y.lohour and Y.hihour;

# left join 활용
select 차량이름,고객명, 시간, 차요금, 시간*tr.rate, 시간*tr.rate+차요금, range_time
from timerate tr, (select c.car_name 차량이름,cu.cus_name 고객명,timestampdiff(hour, from_time,to_time) 시간, price 차요금
               from reservation 
               left join price using(car_id) 
               left join car c using(car_id) 
               left join cus_info cu using(cus_id)) a
                    where 시간 between lohour and hihour;
                    
desc price;



