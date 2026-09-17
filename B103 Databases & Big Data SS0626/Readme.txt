# Hotel Reservation System

---

A short demonstration video showing the Hotel Reservation System is available here:

**Video: 
https://gismauniversity-my.sharepoint.com/:v:/g/personal/aditya_kumar_gisma-student_com/IQDp8tDwx37jQrrT_7c1WuxcAW4YMMKqTcEAM3bmFw9xMQs?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=OpwQhB

The demonstration covers the database structure, sample data and selected SQL queries.

---

## B103 – Databases & Big Data

A relational **Hotel Reservation System** developed using SQL as part of the B103 Databases & Big Data individual project at Gisma University of Applied Sciences.

The purpose of this project is to design and implement a structured relational database that can manage hotel customers, rooms, bookings and payments efficiently.

---

## Project Overview

The Hotel Reservation System provides a database structure for managing the main activities involved in hotel reservations.

The database allows information to be stored, updated, retrieved and managed using SQL. Relationships between customers, rooms, bookings and payments are implemented using primary keys and foreign keys.

---

## Database Structure

The main entities in the system are:

### Customers

Stores information about customers.

Example information includes:

* Customer ID
* Customer's First Name
* Customer's Last Name
* Email
* Phone Number
* Address

### Rooms

Stores information about the rooms in the hotel.

Example information includes:

* Room ID
* Room number
* Room Floor
* Room Capacity
* Room availability/status

### Bookings

Stores reservation information and connects customers with rooms.

Example information includes:

* Booking ID
* Customer ID
* Room ID
* Check-in date
* Check-out date
* Booking status
* Number of Guests

### Payments

Stores payment information associated with reservations.

Example information includes:

* Payment ID
* Booking ID
* Payment date
* Payment amount
* Payment status
* Payment Description


---

## Entity Relationship Diagram

The database design is represented using an Entity Relationship Diagram (ERD).

The ERD shows the entities, attributes, primary keys, foreign keys and relationships between the tables.

**ER Diagram:**

`[Insert your ER diagram image here]`

For example:

Customers
    |
    | 1 : M
    |
Bookings
    |
    | M : 1
    |
Rooms

Bookings
    |
    | 1 : M
    |
Payments

---

## Technologies Used

* **SQL**
* **Dbeaver**
* **MariaDB**
* **GitHub**

---

## Project Report

The complete B103 project report is available in the repository:

**Report:** `Gisma/B103_Project_Report.pdf`

---

## Author

**Name: Aditya Kumar
**Student ID: Gh1039641
**University: Gisma University of Applied Sciences
**Module: B103 Databases & Big Data
**Module Tutor: Ramin Baghaei Mehr

---

## Academic Project

This repository was created for the **B103 Databases & Big Data**
The project demonstrates the design and implementation of a relational database for a real-world Hotel Reservation System.
