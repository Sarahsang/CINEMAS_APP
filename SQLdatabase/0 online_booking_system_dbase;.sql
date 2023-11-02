DROP DATABASE IF EXISTS online_booking_system_dbase;
CREATE DATABASE IF NOT EXISTS online_booking_system_dbase;
USE online_booking_system_dbase;

-- Movie table
CREATE TABLE Movie (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    lang VARCHAR(100) NOT NULL,
    genre VARCHAR(100) NOT NULL,
    rDate DATETIME NOT NULL,
    duration INT NOT NULL,
    country VARCHAR(100),
    description TEXT,
    UNIQUE(title, rDate)
);

-- Cinema Hall table
CREATE TABLE CinemaHall (
    hall_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    total_seats INT NOT NULL
);

-- Cinema Hall Seat table
CREATE TABLE CinemaHallSeat (
    seat_id INT AUTO_INCREMENT PRIMARY KEY,
    hall_id INT,
    seat_number INT NOT NULL,
    seat_column INT NOT NULL,
    seat_type INT NOT NULL,
    is_reserved BOOLEAN DEFAULT FALSE,
    seat_price FLOAT NOT NULL,
    FOREIGN KEY (hall_id) REFERENCES CinemaHall(hall_id)
);

-- User table
-- info allows to be null, bcs guest users, we can make sure other users fill up the info by adding code logic
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NULL,
    password VARCHAR(255) NULL,
    name VARCHAR(255) NULL,
    address TEXT NULL,
    email VARCHAR(255) NULL,
    phone VARCHAR(20) NULL,
    user_type ENUM('Admin', 'FrontDeskStaff', 'Customer') NOT NULL,
    UNIQUE(username)
);

-- Screening table
CREATE TABLE Screening (
    screening_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    screening_date DATETIME NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    hall_id INT,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (hall_id) REFERENCES CinemaHall(hall_id)
);

-- Booking table
CREATE TABLE Booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    screening_id INT,
    number_of_seats INT NOT NULL,
    created_on DATETIME NOT NULL,
    status INT NOT NULL,
    order_total FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (screening_id) REFERENCES Screening(screening_id)
);

-- BookingSeat table (to keep track of which seats are booked in a booking)
CREATE TABLE BookingSeat (
    booking_id INT,
    seat_id INT,
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id),
    FOREIGN KEY (seat_id) REFERENCES CinemaHallSeat(seat_id)
);

-- Notification table
CREATE TABLE Notification (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    created_on DATETIME NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- CreditCard table
CREATE TABLE CreditCard (
    credit_card_number VARCHAR(20) PRIMARY KEY,
    card_type VARCHAR(50) NOT NULL,
    expiry_date DATETIME NOT NULL,
    name_on_card VARCHAR(255) NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- DebitCard table
CREATE TABLE DebitCard (
    card_number VARCHAR(20) PRIMARY KEY,
    bank_name VARCHAR(100) NOT NULL,
    name_on_card VARCHAR(255) NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Coupon table
CREATE TABLE Coupon (
    coupon_id VARCHAR(20) PRIMARY KEY,
    expiry_date DATETIME NOT NULL,
    discount FLOAT NOT NULL
);

-- Payment table
CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    amount FLOAT NOT NULL,
    created_on DATETIME NOT NULL,
    payment_type ENUM('CreditCard', 'DebitCard', 'Cash') NOT NULL,
    credit_card_number VARCHAR(20) NULL,
	debit_card_number VARCHAR(20) NULL,
	coupon_id VARCHAR(20) NULL,
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id),
    FOREIGN KEY (credit_card_number) REFERENCES CreditCard(credit_card_number),
    FOREIGN KEY (debit_card_number) REFERENCES DebitCard(card_number),
    FOREIGN KEY (coupon_id) REFERENCES Coupon(coupon_id)
);