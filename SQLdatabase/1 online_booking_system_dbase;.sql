-- Insert into CinemaHall
INSERT INTO CinemaHall (name, total_seats) VALUES
('Hall 1', 120),
('Hall 2', 90),
('Hall 3', 110),
('Hall 4', 80);

-- Insert into CinemaHallSeat
-- Here we're assuming 10 rows (A-J) and varying numbers of seats per row for simplicity
-- Repeat the similar pattern for other halls
INSERT INTO CinemaHallSeat (hall_id, seat_number, seat_column, seat_type, seat_price) VALUES
(1, 1, 1, 1, 10.0), (1, 2, 1, 1, 10.0), (1, 3, 1, 1, 10.0),(1, 4, 1, 1, 10.0), (1, 5, 1, 1, 10.0), (1, 6, 1, 1, 10.0),(1, 7, 1, 1, 10.0), (1, 8, 1, 1, 10.0), (1, 9, 1, 1, 10.0),(1, 10, 1, 1, 10.0), (1, 11, 1, 1, 10.0), (1, 12, 1, 1, 10.0),
(1, 1, 2, 1, 10.0), (1, 2, 2, 1, 10.0), (1, 3, 2, 1, 10.0),(1, 4, 2, 1, 10.0), (1, 5, 2, 1, 10.0), (1, 6, 2, 1, 10.0),(1, 7, 2, 1, 10.0), (1, 8, 2, 1, 10.0), (1, 9, 2, 1, 10.0),(1, 10, 2, 1, 10.0), (1, 11, 2, 1, 10.0), (1, 12, 2, 1, 10.0),
(1, 1, 3, 1, 10.0), (1, 2, 3, 1, 10.0), (1, 3, 3, 1, 10.0),(1, 4, 3, 1, 10.0), (1, 5, 3, 1, 10.0), (1, 6, 3, 1, 10.0),(1, 7, 3, 1, 10.0), (1, 8, 3, 1, 10.0), (1, 9, 3, 1, 10.0),(1, 10, 3, 1, 10.0), (1, 11, 3, 1, 10.0), (1, 12, 3, 1, 10.0),
(1, 1, 4, 1, 10.0), (1, 2, 4, 1, 10.0), (1, 3, 4, 1, 10.0),(1, 4, 4, 1, 10.0), (1, 5, 4, 1, 10.0), (1, 6, 4, 1, 10.0),(1, 7, 4, 1, 10.0), (1, 8, 4, 1, 10.0), (1, 9, 4, 1, 10.0),(1, 10, 4, 1, 10.0), (1, 11, 4, 1, 10.0), (1, 12, 4, 1, 10.0),
(1, 1, 5, 1, 10.0), (1, 2, 5, 1, 10.0), (1, 3, 5, 1, 10.0),(1, 4, 5, 1, 10.0), (1, 5, 5, 1, 10.0), (1, 6, 5, 1, 10.0),(1, 7, 5, 1, 10.0), (1, 8, 5, 1, 10.0), (1, 9, 5, 1, 10.0),(1, 10, 5, 1, 10.0), (1, 11, 5, 1, 10.0), (1, 12, 5, 1, 10.0),
(1, 1, 6, 1, 10.0), (1, 2, 6, 1, 10.0), (1, 3, 6, 1, 10.0),(1, 4, 6, 1, 10.0), (1, 5, 6, 1, 10.0), (1, 6, 6, 1, 10.0),(1, 7, 6, 1, 10.0), (1, 8, 6, 1, 10.0), (1, 9, 6, 1, 10.0),(1, 10, 6, 1, 10.0), (1, 11, 6, 1, 10.0), (1, 12, 6, 1, 10.0),
(1, 1, 7, 1, 10.0), (1, 2, 7, 1, 10.0), (1, 3, 7, 1, 10.0),(1, 4, 7, 1, 10.0), (1, 5, 7, 1, 10.0), (1, 6, 7, 1, 10.0),(1, 7, 7, 1, 10.0), (1, 8, 7, 1, 10.0), (1, 9, 7, 1, 10.0),(1, 10, 7, 1, 10.0), (1, 11, 7, 1, 10.0), (1, 12, 7, 1, 10.0),
(1, 1, 8, 1, 10.0), (1, 2, 8, 1, 10.0), (1, 3, 8, 1, 10.0),(1, 4, 8, 1, 10.0), (1, 5, 8, 1, 10.0), (1, 6, 8, 1, 10.0),(1, 7, 8, 1, 10.0), (1, 8, 8, 1, 10.0), (1, 9, 8, 1, 10.0),(1, 10, 8, 1, 10.0), (1, 11, 8, 1, 10.0), (1, 12, 8, 1, 10.0),
(1, 1, 9, 1, 10.0), (1, 2, 9, 1, 10.0), (1, 3, 9, 1, 10.0),(1, 4, 9, 1, 10.0), (1, 5, 9, 1, 10.0), (1, 6, 9, 1, 10.0),(1, 7, 9, 1, 10.0), (1, 8, 9, 1, 10.0), (1, 9, 9, 1, 10.0),(1, 10, 9, 1, 10.0), (1, 11, 9, 1, 10.0), (1, 12, 9, 1, 10.0),
(1, 1, 10, 1, 10.0), (1, 2, 10, 1, 10.0), (1, 3, 10, 1, 10.0),(1, 4, 10, 1, 10.0), (1, 5, 10, 1, 10.0), (1, 6, 10, 1, 10.0),(1, 7, 10, 1, 10.0), (1, 8, 10, 1, 10.0), (1, 9, 10, 1, 10.0),(1, 10, 10, 1, 10.0), (1, 11, 10, 1, 10.0), (1, 12, 10, 1, 10.0);
 -- for Hall 1 (120 seats)
 
INSERT INTO CinemaHallSeat (hall_id, seat_number, seat_column, seat_type, seat_price) VALUES
(2, 1, 1, 1, 10.0), (2, 2, 1, 1, 10.0), (2, 3, 1, 1, 10.0),
(2, 4, 1, 1, 10.0), (2, 5, 1, 1, 10.0), (2, 6, 1, 1, 10.0),
(2, 7, 1, 1, 10.0), (2, 8, 1, 1, 10.0), (2, 9, 1, 1, 10.0),
(2, 10, 1, 1, 10.0), (2, 1, 2, 1, 10.0), (2, 2, 2, 1, 10.0),
(2, 3, 2, 1, 10.0), (2, 4, 2, 1, 10.0), (2, 5, 2, 1, 10.0),
(2, 6, 2, 1, 10.0), (2, 7, 2, 1, 10.0), (2, 8, 2, 1, 10.0),
(2, 9, 2, 1, 10.0), (2, 10, 2, 1, 10.0), (2, 1, 3, 1, 10.0),
(2, 2, 3, 1, 10.0), (2, 3, 3, 1, 10.0), (2, 4, 3, 1, 10.0),
(2, 5, 3, 1, 10.0), (2, 6, 3, 1, 10.0), (2, 7, 3, 1, 10.0),
(2, 8, 3, 1, 10.0), (2, 9, 3, 1, 10.0), (2, 10, 3, 1, 10.0),
(2, 1, 4, 1, 10.0), (2, 2, 4, 1, 10.0), (2, 3, 4, 1, 10.0),
(2, 4, 4, 1, 10.0), (2, 5, 4, 1, 10.0), (2, 6, 4, 1, 10.0),
(2, 7, 4, 1, 10.0), (2, 8, 4, 1, 10.0), (2, 9, 4, 1, 10.0),
(2, 10, 4, 1, 10.0), (2, 1, 5, 1, 10.0), (2, 2, 5, 1, 10.0),
(2, 3, 5, 1, 10.0), (2, 4, 5, 1, 10.0), (2, 5, 5, 1, 10.0),
(2, 6, 5, 1, 10.0), (2, 7, 5, 1, 10.0), (2, 8, 5, 1, 10.0),
(2, 9, 5, 1, 10.0), (2, 10, 5, 1, 10.0), (2, 1, 6, 1, 10.0),
(2, 2, 6, 1, 10.0), (2, 3, 6, 1, 10.0), (2, 4, 6, 1, 10.0),
(2, 5, 6, 1, 10.0), (2, 6, 6, 1, 10.0), (2, 7, 6, 1, 10.0),
(2, 8, 6, 1, 10.0), (2, 9, 6, 1, 10.0), (2, 10, 6, 1, 10.0),
(2, 1, 7, 1, 10.0), (2, 2, 7, 1, 10.0), (2, 3, 7, 1, 10.0),
(2, 4, 7, 1, 10.0), (2, 5, 7, 1, 10.0), (2, 6, 7, 1, 10.0),
(2, 7, 7, 1, 10.0), (2, 8, 7, 1, 10.0), (2, 9, 7, 1, 10.0),
(2, 10, 7, 1, 10.0), (2, 1, 8, 1, 10.0), (2, 2, 8, 1, 10.0),
(2, 3, 8, 1, 10.0), (2, 4, 8, 1, 10.0), (2, 5, 8, 1, 10.0),
(2, 6, 8, 1, 10.0), (2, 7, 8, 1, 10.0), (2, 8, 8, 1, 10.0),
(2, 9, 8, 1, 10.0), (2, 10, 8, 1, 10.0), (2, 1, 9, 1, 10.0),
(2, 2, 9, 1, 10.0), (2, 3, 9, 1, 10.0), (2, 4, 9, 1, 10.0),
(2, 5, 9, 1, 10.0), (2, 6, 9, 1, 10.0), (2, 7, 9, 1, 10.0),
(2, 8, 9, 1, 10.0), (2, 9, 9, 1, 10.0), (2, 10, 9, 1, 10.0);
 -- for Hall 2 (90 seats);
INSERT INTO CinemaHallSeat (hall_id, seat_number, seat_column, seat_type, seat_price) VALUES
(3, 1, 1, 1, 10.0), (3, 2, 1, 1, 10.0), (3, 3, 1, 1, 10.0),
(3, 4, 1, 1, 10.0), (3, 5, 1, 1, 10.0), (3, 6, 1, 1, 10.0),
(3, 7, 1, 1, 10.0), (3, 8, 1, 1, 10.0), (3, 9, 1, 1, 10.0),
(3, 10, 1, 1, 10.0), (3, 1, 2, 1, 10.0), (3, 2, 2, 1, 10.0),
(3, 3, 2, 1, 10.0), (3, 4, 2, 1, 10.0), (3, 5, 2, 1, 10.0),
(3, 6, 2, 1, 10.0), (3, 7, 2, 1, 10.0), (3, 8, 2, 1, 10.0),
(3, 9, 2, 1, 10.0), (3, 10, 2, 1, 10.0), (3, 1, 3, 1, 10.0),
(3, 2, 3, 1, 10.0), (3, 3, 3, 1, 10.0), (3, 4, 3, 1, 10.0),
(3, 5, 3, 1, 10.0), (3, 6, 3, 1, 10.0), (3, 7, 3, 1, 10.0),
(3, 8, 3, 1, 10.0), (3, 9, 3, 1, 10.0), (3, 10, 3, 1, 10.0),
(3, 1, 4, 1, 10.0), (3, 2, 4, 1, 10.0), (3, 3, 4, 1, 10.0),
(3, 4, 4, 1, 10.0), (3, 5, 4, 1, 10.0), (3, 6, 4, 1, 10.0),
(3, 7, 4, 1, 10.0), (3, 8, 4, 1, 10.0), (3, 9, 4, 1, 10.0),
(3, 10, 4, 1, 10.0), (3, 1, 5, 1, 10.0), (3, 2, 5, 1, 10.0),
(3, 3, 5, 1, 10.0), (3, 4, 5, 1, 10.0), (3, 5, 5, 1, 10.0),
(3, 6, 5, 1, 10.0), (3, 7, 5, 1, 10.0), (3, 8, 5, 1, 10.0),
(3, 9, 5, 1, 10.0), (3, 10, 5, 1, 10.0), (3, 1, 6, 1, 10.0),
(3, 2, 6, 1, 10.0), (3, 3, 6, 1, 10.0), (3, 4, 6, 1, 10.0),
(3, 5, 6, 1, 10.0), (3, 6, 6, 1, 10.0), (3, 7, 6, 1, 10.0),
(3, 8, 6, 1, 10.0), (3, 9, 6, 1, 10.0), (3, 10, 6, 1, 10.0),
(3, 1, 7, 1, 10.0), (3, 2, 7, 1, 10.0), (3, 3, 7, 1, 10.0),
(3, 4, 7, 1, 10.0), (3, 5, 7, 1, 10.0), (3, 6, 7, 1, 10.0),
(3, 7, 7, 1, 10.0), (3, 8, 7, 1, 10.0), (3, 9, 7, 1, 10.0),
(3, 10, 7, 1, 10.0), (3, 1, 8, 1, 10.0), (3, 2, 8, 1, 10.0),
(3, 3, 8, 1, 10.0), (3, 4, 8, 1, 10.0), (3, 5, 8, 1, 10.0),
(3, 6, 8, 1, 10.0), (3, 7, 8, 1, 10.0), (3, 8, 8, 1, 10.0),
(3, 9, 8, 1, 10.0), (3, 10, 8, 1, 10.0), (3, 1, 9, 1, 10.0),
(3, 2, 9, 1, 10.0), (3, 3, 9, 1, 10.0), (3, 4, 9, 1, 10.0),
(3, 5, 9, 1, 10.0), (3, 6, 9, 1, 10.0), (3, 7, 9, 1, 10.0),
(3, 8, 9, 1, 10.0), (3, 9, 9, 1, 10.0), (3, 10, 9, 1, 10.0),
(3, 1, 10, 1, 10.0), (3, 2, 10, 1, 10.0), (3, 3, 10, 1, 10.0),
(3, 4, 10, 1, 10.0), (3, 5, 10, 1, 10.0), (3, 6, 10, 1, 10.0),
(3, 7, 10, 1, 10.0), (3, 8, 10, 1, 10.0), (3, 9, 10, 1, 10.0),
(3, 10, 10, 1, 10.0), (3, 1, 11, 1, 10.0), (3, 2, 11, 1, 10.0),
(3, 3, 11, 1, 10.0), (3, 4, 11, 1, 10.0), (3, 5, 11, 1, 10.0),
(3, 6, 11, 1, 10.0), (3, 7, 11, 1, 10.0), (3, 8, 11, 1, 10.0),
(3, 9, 11, 1, 10.0), (3, 10, 11, 1, 10.0), (3, 1, 11, 1, 10.0);

INSERT INTO CinemaHallSeat (hall_id, seat_number, seat_column, seat_type, seat_price) VALUES
(4, 1, 1, 1, 10.0), (4, 2, 1, 1, 10.0), (4, 3, 1, 1, 10.0),
(4, 4, 1, 1, 10.0), (4, 5, 1, 1, 10.0), (4, 6, 1, 1, 10.0),
(4, 7, 1, 1, 10.0), (4, 8, 1, 1, 10.0), (4, 9, 1, 1, 10.0),
(4, 10, 1, 1, 10.0), (4, 1, 2, 1, 10.0), (4, 2, 2, 1, 10.0),
(4, 3, 2, 1, 10.0), (4, 4, 2, 1, 10.0), (4, 5, 2, 1, 10.0),
(4, 6, 2, 1, 10.0), (4, 7, 2, 1, 10.0), (4, 8, 2, 1, 10.0),
(4, 9, 2, 1, 10.0), (4, 10, 2, 1, 10.0), (4, 1, 3, 1, 10.0),
(4, 2, 3, 1, 10.0), (4, 3, 3, 1, 10.0), (4, 4, 3, 1, 10.0),
(4, 5, 3, 1, 10.0), (4, 6, 3, 1, 10.0), (4, 7, 3, 1, 10.0),
(4, 8, 3, 1, 10.0), (4, 9, 3, 1, 10.0), (4, 10, 3, 1, 10.0),
(4, 1, 4, 1, 10.0), (4, 2, 4, 1, 10.0), (4, 3, 4, 1, 10.0),
(4, 4, 4, 1, 10.0), (4, 5, 4, 1, 10.0), (4, 6, 4, 1, 10.0),
(4, 7, 4, 1, 10.0), (4, 8, 4, 1, 10.0), (4, 9, 4, 1, 10.0),
(4, 10, 4, 1, 10.0), (4, 1, 5, 1, 10.0), (4, 2, 5, 1, 10.0),
(4, 3, 5, 1, 10.0), (4, 4, 5, 1, 10.0), (4, 5, 5, 1, 10.0),
(4, 6, 5, 1, 10.0), (4, 7, 5, 1, 10.0), (4, 8, 5, 1, 10.0),
(4, 9, 5, 1, 10.0), (4, 10, 5, 1, 10.0), (4, 1, 6, 1, 10.0),
(4, 2, 6, 1, 10.0), (4, 3, 6, 1, 10.0), (4, 4, 6, 1, 10.0),
(4, 5, 6, 1, 10.0), (4, 6, 6, 1, 10.0), (4, 7, 6, 1, 10.0),
(4, 8, 6, 1, 10.0), (4, 9, 6, 1, 10.0), (4, 10, 6, 1, 10.0),
(4, 1, 7, 1, 10.0), (4, 2, 7, 1, 10.0), (4, 3, 7, 1, 10.0),
(4, 4, 7, 1, 10.0), (4, 5, 7, 1, 10.0), (4, 6, 7, 1, 10.0),
(4, 7, 7, 1, 10.0), (4, 8, 7, 1, 10.0), (4, 9, 7, 1, 10.0),
(4, 10, 7, 1, 10.0), (4, 1, 8, 1, 10.0), (4, 2, 8, 1, 10.0),
(4, 3, 8, 1, 10.0), (4, 4, 8, 1, 10.0), (4, 5, 8, 1, 10.0),
(4, 6, 8, 1, 10.0), (4, 7, 8, 1, 10.0), (4, 8, 8, 1, 10.0);

-- Insert into Movie
INSERT INTO Movie (title, lang, genre, rDate, duration, country, description) VALUES
('The Shawshank Redemption', 'English', 'Drama', '1994-09-23', 142, 'USA', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'),
('Inception', 'English', 'Sci-Fi', '2010-07-16', 148, 'USA', 'A thief who enters the dreams of others must complete an impossible task to have his past crimes forgiven.');

-- Insert into User (Admin, FrontDeskStaff, Customer, and Guest)
-- Passwords are stored in plaintext for simplicity, but they should be securely hashed in a real application
INSERT INTO User (username, password, name, address, email, phone, user_type) VALUES
('admin', 'admin123', 'Admin User', '123 Main St, Lincoln', 'admin@lincolncinemas.com', '123-456-7890', 'Admin'),
('frontdesk', 'frontdesk123', 'Front Desk Staff', '123 Main St, Lincoln', 'frontdesk@lincolncinemas.com', '123-456-7891', 'FrontDeskStaff'),
('john_doe', 'john123', 'John Doe', '456 Oak St, Lincoln', 'john.doe@email.com', '123-456-7892', 'Customer'),
('mia', 'mia', 'Sarah Green', '', 'sarahgreen@email.com', '', 'Customer');

-- Insert into Screening
-- Assuming each movie has multiple screenings across different halls
INSERT INTO Screening (movie_id, screening_date, start_time, end_time, hall_id) VALUES
(1, '2023-11-10', '2023-11-10 18:00:00', '2023-11-10 20:30:00', 1),
(2, '2023-11-10', '2023-11-10 19:00:00', '2023-11-10 21:30:00', 2),
(1, '2023-11-11', '2023-11-11 14:00:00', '2023-11-11 16:30:00', 1),
(1, '2023-11-11', '2023-11-11 17:00:00', '2023-11-11 19:30:00', 2),
(1, '2023-11-12', '2023-11-12 18:00:00', '2023-11-12 20:30:00', 3),
(2, '2023-11-11', '2023-11-11 15:00:00', '2023-11-11 17:30:00', 4),
(2, '2023-11-12', '2023-11-12 16:00:00', '2023-11-12 18:30:00', 1),
(2, '2023-11-12', '2023-11-12 19:00:00', '2023-11-12 21:30:00', 2);

-- Insert into Booking
-- Assuming some bookings have already been made
INSERT INTO Booking (user_id, screening_id, number_of_seats, created_on, status, order_total) VALUES
(3, 1, 2, '2023-11-01', 1, 20.0),
(3, 2, 3, '2023-11-02', 1, 30.0);

-- Insert into BookingSeat
-- Mapping bookings to specific seats
INSERT INTO BookingSeat (booking_id, seat_id) VALUES
(1, 1), (1, 2), -- for booking 1
(2, 3), (2, 4), (2, 5) -- for booking 2
;

-- Insert into Notification
-- Assuming some notifications have already been sent
INSERT INTO Notification (user_id, created_on, content) VALUES
(3, '2023-11-01', 'Your booking for The Shawshank Redemption is confirmed!'),
(3, '2023-11-02', 'Your booking for Inception is confirmed!');

-- Insert into CreditCard
INSERT INTO CreditCard (credit_card_number, card_type, expiry_date, name_on_card, user_id) VALUES
('1234-5678-9012-3456', 'Visa', '2025-12-31 00:00:00', 'John Doe', 3);

-- Insert into DebitCard
INSERT INTO DebitCard (card_number, bank_name, name_on_card, user_id) VALUES
('9876-5432-1098-7654', 'Lincoln Bank', 'John Doe', 3);

-- Insert into Coupon
INSERT INTO Coupon (coupon_id, expiry_date, discount) VALUES
('SUMMER2023', '2023-08-31 00:00:00', 10.0);

-- Insert into Payment
-- Assuming some payments have been made
-- Insert into Payment
INSERT INTO Payment (booking_id, amount, created_on, payment_type, credit_card_number) VALUES
(1, 20.0, '2023-11-01 18:30:00', 'Cash', NULL),
(2, 30.0, '2023-11-02 19:30:00', 'CreditCard', '1234-5678-9012-3456');