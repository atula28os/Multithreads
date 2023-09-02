/* 

create schema if not exists multi;

use multi;

create table if not exists prices(
	id int primary key auto_increment,
    symbol varchar(10),
    price float,
    extracted_time datetime
);

*/

select * from multi.prices;
