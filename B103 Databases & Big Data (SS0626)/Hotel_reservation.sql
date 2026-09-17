-- Creating database
create database Hotel_reservation;

-- Select the database to edit
use Hotel_reservation;

-- Creating Customers Table
create table customers (
customer_id int auto_increment primary key,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(50) not null,
phone_number varchar(13) not null,
address varchar(50) not null
);

-- Creating Rooms Table
create table rooms (
room_id int auto_increment primary key,
room_no varchar(3) not null unique,
room_floor int not null,
room_capacity int not null,
room_status varchar(20) default 'Available',
check (room_capacity > 0), 
check (room_status in ('Available', 'Occupied', 'Maintenance'))
);

-- Creating Bookings Table
create table bookings (
booking_id int auto_increment primary key,
customer_id int not null,
room_id int not null,
check_in datetime,
check_out datetime,
booking_status varchar(20) not null,
number_of_guests int not null,

foreign key (customer_id)
	references customers(customer_id),
	
foreign key (room_id)
	references rooms(room_id),

check (check_out > check_in),
check (booking_status in ('Confirmed', 'Cancelled', 'Completed'))
);

-- Creating Payments Table
create table payment (
payment_id int not null auto_increment primary key,
booking_id int not null,
payment_date date not null,
amount decimal(10,2) not null,
payment_method varchar(20) not null,
payment_status varchar(20) not null,
payment_description varchar(30),

foreign key (booking_id) references bookings(booking_id),

check (amount > 0),
check (payment_method in ('cash','card','bank transfer')),
check (payment_status in ('paid','pending','refunded'))
);

-- Renaming the table to 'Payments'
alter table payment 
rename to payments;

-- Changing the datatype of room_id from 'int' to 'varchar'
alter table bookings
drop foreign key `2`;

alter table rooms
modify room_id varchar(5) not null;

alter table bookings
drop column room_id;

alter table bookings
add column room_id varchar(5) NOT NULL AFTER customer_id;

alter table bookings
add constraint `2`
foreign key (room_id)
references rooms(room_id);

-- To show how a table was created
show create table customers;

-- Inerting data in all the tables
insert into customers
(first_name, last_name, email, phone_number, address)
values
('John', 'Smith', 'john@gmail.com', '+491234567890', 'lichtstreet 12, Berlin, Germany'),
('Will', 'Smith', 'Will@gmail.com', '+351762096762', 'hellstreet 22, Berlin, Germany'),
('Tom', 'Hardy', 'tomi@hardy.com', '+491745556789', 'firetstreet 44, Essen, Germany'),
('Jimmy', 'Sandhu', 'Sandhu34@gmail.com', '+491234567890', 'waterstreet 32, Munich, Germany'),
('Ammy', 'James', 'Ammy12@gmail.com', '+491234567890', 'risestreet 25, Dresden, Germany');


insert into rooms
(room_id, room_no, room_floor, room_capacity)
values
('A101', 101, 1, 5),
('A102', 102, 1, 4),
('B201', 201, 2, 3),
('B202', 202, 2, 3),
('C301', 301, 3, 2),
('C302', 302, 3, 2),
('D401', 401, 4, 1),
('D402', 402, 4, 1),
('D403', 403, 4, 1);


insert into bookings
(customer_id, room_id, check_in, check_out, booking_status, number_of_guests)
values
(1, 'D401', current_timestamp, '2026-09-11 12:00:00', 'confirmed', 1),
(2, 'C302', current_timestamp, '2026-09-12 22:00:00', 'confirmed', 2),
(3, 'B202', '2026-09-09 15:35:45', '2026-09-13 01:30:00', 'confirmed', 3),
(4, 'A101', '2026-09-01 12:22:32', '2026-09-03 18:22:32', 'completed', 5),
(5, 'A102', '2026-09-25 08:00:00', '2026-09-27 12:00:00', 'confirmed', 4);


insert into payments
(booking_id, payment_date, amount, payment_method, payment_status, payment_description)
values
(1, '2026-09-10', 60.00, 'Card', 'Paid', null),
(2, '2026-09-02', 150.00, 'Card', 'Paid', null),
(3, '2026-09-01', 400.00, 'Cash', 'Pending', null),
(4, '2026-09-03', 590.00, 'Card', 'Paid', "added 50 for broken things"),
(5, '2026-09-04', 490.00, 'Bank Transfer', 'Pending', null);

-- display all record
select * from customers;

-- adding a record
insert into customers
(first_name, last_name, email, phone_number, address)
values
('Lexi', 'singh', 'singhisking@gmail.com', '+491762345634', 'alexastreet 59, Berlin, Germany');

-- update a record
update customers
set phone_number = '+491234569089'
where customer_id = 3;

-- deleting a record
delete from customers
where customer_id = '6';


-- join query (It gives all the booking information along with the customer and room information)
select 
	c.first_name,
	c.last_name,
	r.room_id,
	b.check_in,
	b.check_out,
	b.booking_status
from bookings b
join customers c
	on b.customer_id = c.customer_id
left join rooms r
	on b.room_id = r.room_id;

-- count total rooms
select count(*) as total_rooms
from rooms
group by room_status;

-- average revenue
select avg(amount) as Average_revenue
from payments
where payment_status = 'Paid';

-- room for 3 or more guests
select * from rooms
where room_capacity > 2;

-- rooms costing more than average
select 
	r.room_no,
	r.room_id,
	p.amount,
	b.booking_id
from bookings b
join payments p
	on b.booking_id = p.booking_id
join rooms r
	on b.room_id = r.room_id
where p.amount > (
	select avg(amount)
	from payments);

-- all customers and their bookings
select
    c.customer_id,
    c.first_name,
    c.last_name,
    b.booking_id,
    b.room_id,
    b.check_in,
    b.check_out
from customers c
left join bookings b
    on c.customer_id = b.customer_id

union

select
    c.customer_id,
    c.first_name,
    c.last_name,
    b.booking_id,
    b.room_id,
    b.check_in,
    b.check_out
from customers c
right join bookings b
    on c.customer_id = b.customer_id;

-- a stored procedure to get booking information as per customer_id

delimiter //

create procedure Get_customer_bookings(in customerid int)
begin
	select
		b.booking_id,
		c.first_name,
		c.last_name,
		r.room_no,
		b.check_in,
		b.check_out,
		b.booking_status,
		b.number_of_guests
	from bookings b
	join customers c
		on b.customer_id = c.customer_id
	join rooms r
		on b.room_id = r.room_id
	where b.customer_id = customerid;
end

delimiter //


call get_customer_bookings(3);


-- Event to update the status of the room

set global event_scheduler = on;

delimiter //

create event update_booking_room_status
on schedule every 1 minute
do
begin
	
	update bookings
	set booking_status = 'Completed'
	where booking_status = 'Confirmed'
		and current_timestamp >= check_out;
	
	update bookings
	set booking_status = 'Confirmed'
	where booking_status not in ('completed', 'Cancelled')
		and current_timestamp >= check_in
		and current_timestamp < check_out;
	
	update rooms r
	join bookings b
		on r.room_id = b.room_id
	set r.room_status = 'Occupied'
	where b.booking_status = 'confirmed'
		and current_timestamp >= b.check_in
		and current_timestamp < b.check_out;
	
	update rooms r
	join bookings b
		on r.room_id = b.room_id
	set r.room_status = 'Available'
	where b.booking_status in ('Completed', 'Cancelled')
		or current_timestamp >= b.check_out;
	
	end //
	
	delimiter;
	
-- Transaction example
start transaction;

insert into customers
(first_name, last_name, email, phone_number, address)
values
('Tom', 'raj', 'rajtom@gmail.com', '+491235670989', 'warstreet 43, Berlin, Germany');

set @customer_id = last_insert_id();


insert into bookings
(customer_id, room_id, check_in, check_out, booking_status, number_of_guests)
values
(last_insert_id(), 'C302', '2026-09-15 12:00:00', '2026-09-17 11:00:00', 'Confirmed', '2');

set @booking_id = last_insert_id();
insert into payments
(booking_id, payment_date, amount, payment_method, payment_status)
values
(@booking_id, '2026-09-25', 240, 'card', 'pending');

commit;




