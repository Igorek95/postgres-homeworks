-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employees_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date varchar(10) NOT NULL,
	notes varchar(500) NOT NULL
);

CREATE TABLE customers
(
	customer_id text PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
    customer_id REFERENCES customers(customer_id) NOT NULL,
	employee_id REFERENCES employees(employees_id) NOT NULL,
	order_date varchar(10) NOT NULL,
	ship_city varchar(50) NOT NULL
)