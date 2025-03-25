# Restaurant Management System

## Overview
This project is an interactive **Restaurant Management System** built using Python and MySQL
## Features
- **Food Ordering** – Customers can place orders from the menu.
- **Table & Hall Booking** – Users can book or cancel table and hall reservations.
- **Buffet Selection** – Option to choose a buffet facility.
- **Staff Management** – Add, modify, delete, and search staff records.
- **Feedback Collection** – Collects and stores customer feedback.
- **Transaction Record Keeping** – Stores order and booking details for future reference.
- **Complaint System** – Staff can register complaints for management review.
## Modules Used

### 1. **MySQL Connector**
- **`mysql.connector`** – Enables Python programs to access MySQL databases using an API that complies with the Python Database API Specification.

### 2. **Datetime Module**
- **`datetime`** – Provides functions for handling dates, times, and time intervals.

### 3. **Random Module**
- **`random`** – Generates random float values uniformly in the range [0.0, 1.0).

### 4. **Pickle Module**
- **`pickle`** – Used for object serialization, allowing data (such as orders, bookings, and customer details) to be stored and retrieved efficiently.


## User-Defined Functions

- **`menu()`** – Displays the menu to customers.
- **`order()`** – Allows customers to order food.
- **`book()`** – Booking-related operations:
  - **`display()`** – Shows existing bookings.
  - **`insert()`** – Books a table.
  - **`dele()`** – Cancels a booking.
- **`buffet()`** – Enables selection of buffet facility.
- **`party()`** – Party hall-related operations:
  - **`hall()`** – Books a party hall.
  - **`show()`** – Displays party bookings.
  - **`cancel()`** – Cancels a party booking.
- **`Us()`** – Fetches restaurant details.
- **`feed()`** – Collects customer feedback.
- **`DETAILS()`** – Displays staff details.
- **`RECORD()`** – Inserts staff record.
- **`MODIFY()`** – Modifies staff record.
- **`DELETE()`** – Deletes staff record.
- **`SEARCH()`** – Searches staff records.
- **`COMPLAIN()`** – Allows staff to express complaints.

