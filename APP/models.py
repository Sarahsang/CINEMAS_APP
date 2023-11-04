from datetime import date
from datetime import datetime
from typing import List, Optional
from abc import ABC, abstractmethod
from db import Database
from contextlib import closing

db = Database('localhost', 'root', 'root', 'online_booking_system_dbase')

class General(ABC):
    def __init__(self):
        self.db = db 

    # same for all users
    def search_movie_by_title(self, title: str) -> List['Movie']:
        with closing(self.db.get_connection()) as conn:
            with conn.cursor(dictionary=True) as cursor:
                query = "SELECT * FROM Movie WHERE title LIKE %s"
                try:
                    cursor.execute(query, ('%' + title + '%',))
                    movies = cursor.fetchall()
                    # movie_objects = [Movie(**{k: v for k, v in movie.items() if k != 'movie_id'}) for movie in movies]
                    # for movie in movie_objects:
                    #     print(movie)  # 应该调用 __str__ 方法
                    print(movies)
                except Exception as e:
                    print(f"An error occurred: {e}")
                return [Movie(**{k: v for k, v in movie.items() if k != 'movie_id'}) for movie in movies]

    def search_movie_by_lang(self, lang: str) -> List['Movie']:
        with closing(self.db.get_connection()) as conn:
            with conn.cursor(dictionary=True) as cursor:
                query = "SELECT * FROM Movie WHERE lang = %s"
                try:
                    cursor.execute(query, (lang,))
                    movies = cursor.fetchall()
                    print(movies)
                except Exception as e:
                    print(f"An error occurred: {e}")
                return [Movie(**{k: v for k, v in movie.items() if k != 'movie_id'}) for movie in movies]

    def search_movie_by_genre(self, genre: str) -> List['Movie']:
        with closing(self.db.get_connection()) as conn:
            with conn.cursor(dictionary=True) as cursor:
                query = "SELECT * FROM Movie WHERE genre = %s"
                try:
                    cursor.execute(query, (genre,))
                    movies = cursor.fetchall()
                    print(movies)
                except Exception as e:
                    print(f"An error occurred: {e}")
                return [Movie(**{k: v for k, v in movie.items() if k != 'movie_id'}) for movie in movies]

    def search_movie_by_date(self, rDate: str) -> List['Movie']:
        with closing(self.db.get_connection()) as conn:
            with conn.cursor(dictionary=True) as cursor:
                query = "SELECT * FROM Movie WHERE rDate = %s"
                try:
                    cursor.execute(query, (rDate,))
                    movies = cursor.fetchall()
                    print(movies)
                except Exception as e:
                    print(f"An error occurred: {e}")
                return [Movie(**{k: v for k, v in movie.items() if k != 'movie_id'}) for movie in movies]


    def get_movie_details(self, movie) -> str:
        return f"Movie in model({movie.title}, {movie.genre}, {movie.rDate})"

class Guest(General):
    def register(self, username: str, password: str, name: str, address: str, email: str, phone: str) -> str:
        # Check if username or email already exists
        query = "SELECT * FROM User WHERE username = %s OR email = %s"
        self.cursor.execute(query, (username, email))
        result = self.cursor.fetchone()
        
        if result:
            return "Username or email already exists. Please choose a different one."
        else:
            # If username and email are unique, proceed to create a new user
            insert_query = "INSERT INTO User (username, password, name, address, email, phone, user_type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(insert_query, (username, password, name, address, email, phone, 'Customer'))
            self.conn.commit()
            return "Registration successful!"

class Person(ABC):

    @abstractmethod
    def __init__(self, name: str, address: str, email: str, phone: str):
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone

    @property
    @abstractmethod
    def name(self) -> str:
        return self._name

    @name.setter
    @abstractmethod
    def name(self, value: str):
        self._name = value

    @property
    @abstractmethod
    def address(self) -> str:
        return self._address

    @address.setter
    @abstractmethod
    def address(self, value: str):
        self._address = value

    @property
    @abstractmethod
    def email(self) -> str:
        return self._email

    @email.setter
    @abstractmethod
    def email(self, value: str):
        self._email = value

    @property
    @abstractmethod
    def phone(self) -> str:
        return self._phone

    @phone.setter
    @abstractmethod
    def phone(self, value: str):
        self._phone = value

class User(Person):

    def __init__(self, username: str, password: str, name: str, address: str, email: str, phone: str):
        super().__init__(name, address, email, phone)
        self.conn = db.get_connection()
        self.cursor = self.conn.cursor(dictionary=True)
        self._username = username
        self._password = password
        self.is_logged_in = False

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        self._username = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = value

    def login(self, username: str, password: str) -> str:
        try:
            query = "SELECT * FROM User WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, password))
            result = self.cursor.fetchone()
            if result:
                self.is_logged_in = True
                return "Login successful!"
            else:
                return "Incorrect username or password."
        except Exception as e:
            return f"An error occurred during login: {str(e)}"

    def logout(self) -> str:
        try:
            if self.is_logged_in:
                self.is_logged_in = False
                return "Logout successful!"
            else:
                return "You are already logged out."
        except Exception as e:
            return f"An error occurred during logout: {str(e)}"

    def reset_password(self, old_password: str, new_password: str) -> str:
        try:
            if not self.is_logged_in:
                return "You must be logged in to reset your password."
            
            if self._password != old_password:
                return "Old password is incorrect."
            
            self._password = new_password
            query = "UPDATE User SET password = %s WHERE username = %s"
            self.cursor.execute(query, (new_password, self._username))
            self.conn.commit()
            return "Password reset successfully!"
        except Exception as e:
            return f"An error occurred during password reset: {str(e)}"

class Admin(User):
    def __init__(self, username: str, password: str, fname: str, lname: str, address: str, email: str, phone: str):
        super().__init__(username, password, fname, lname, address, email, phone)

    def add_movie(self, title: str, lang: str, genre: str, rDate: date, duration: int, country: str, description: str) -> str:
        try:
            query = "INSERT INTO Movie (title, lang, genre, rDate, duration, country, description) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, (title, lang, genre, rDate, duration, country, description))
            self.conn.commit()
            return "Movie added successfully!"
        except Exception as e:
            return f"An error occurred while adding the movie: {str(e)}"

    def add_screening(self, movie_id: int, screening_date: datetime, start_time: datetime, end_time: datetime, hall_id: int) -> str:
        try:
            query = "INSERT INTO Screening (movie_id, screening_date, start_time, end_time, hall_id) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (movie_id, screening_date, start_time, end_time, hall_id))
            self.conn.commit()
            return "Screening added successfully!"
        except Exception as e:
            return f"An error occurred while adding the screening: {str(e)}"  
    
    def cancel_movie(self, movie_id: int) -> str:
        try:
            query = "DELETE FROM Movie WHERE movie_id = %s"
            self.cursor.execute(query, (movie_id,))
            self.conn.commit()
            return "Movie cancelled successfully!"
        except Exception as e:
            return f"An error occurred while cancelling the movie: {str(e)}"
    
    def cancel_screening(self, screening_id: int) -> str:
        try:
            query = "DELETE FROM Screening WHERE screening_id = %s"
            self.cursor.execute(query, (screening_id,))
            self.conn.commit()
            return "Screening cancelled successfully!"
        except Exception as e:
            return f"An error occurred while cancelling the screening: {str(e)}"

class FrontDeskStaff(User):
    def __init__(self, username: str, password: str, fname: str, lname: str, address: str, email: str, phone: str):
        super().__init__(username, password, fname, lname, address, email, phone)

    def make_booking(self, user_id: int, screening_id: int, seat_ids: list) -> str:
        try:
            # Check if seats are available
            query = "SELECT is_reserved FROM CinemaHallSeat WHERE seat_id IN %s"
            self.cursor.execute(query, (tuple(seat_ids),))
            seats = self.cursor.fetchall()
            if any(seat['is_reserved'] for seat in seats):
                return "One or more selected seats are already reserved."

            # Create booking
            query = "INSERT INTO Booking (user_id, screening_id, number_of_seats, created_on, status, order_total) VALUES (%s, %s, %s, NOW(), 1, 0)"
            self.cursor.execute(query, (user_id, screening_id, len(seat_ids)))
            booking_id = self.cursor.lastrowid

            # Reserve seats
            for seat_id in seat_ids:
                query = "INSERT INTO BookingSeat (booking_id, seat_id) VALUES (%s, %s)"
                self.cursor.execute(query, (booking_id, seat_id))
                query = "UPDATE CinemaHallSeat SET is_reserved = TRUE WHERE seat_id = %s"
                self.cursor.execute(query, (seat_id,))

            self.conn.commit()
            return "Booking successfully created!"
        except Exception as e:
            return f"An error occurred while making the booking: {str(e)}"

    def cancel_booking(self, booking_id: int) -> str:
        try:
            # Retrieve seat IDs from BookingSeat
            query = "SELECT seat_id FROM BookingSeat WHERE booking_id = %s"
            self.cursor.execute(query, (booking_id,))
            seat_ids = [seat['seat_id'] for seat in self.cursor.fetchall()]

            # Update seats to be not reserved
            query = "UPDATE CinemaHallSeat SET is_reserved = FALSE WHERE seat_id IN %s"
            self.cursor.execute(query, (tuple(seat_ids),))

            # Cancel booking
            query = "DELETE FROM Booking WHERE booking_id = %s"
            self.cursor.execute(query, (booking_id,))

            self.conn.commit()
            return "Booking successfully cancelled!"
        except Exception as e:
            return f"An error occurred while cancelling the booking: {str(e)}"

class Customer(User):
    def __init__(self, username: str, password: str, name: str, address: str, email: str, phone: str, booking_list: List['Booking'], notification_list: List['Notification']):
        super().__init__(username, password, name, address, email, phone)
        self.__booking_list = booking_list
        self.__notification_list = notification_list
        
    @property
    def booking_list(self) -> List['Booking']:
        return self.__booking_list

    @booking_list.setter
    def booking_list(self, value: List['Booking']):
        self.__booking_list = value

    @property
    def notification_list(self) -> List['Notification']:
        return self.__notification_list

    @notification_list.setter
    def notification_list(self, value: List['Notification']):
        self.__notification_list = value

    def get_booking_list(self) -> List['Booking']:
        query = "SELECT * FROM Booking WHERE user_id = %s"
        with closing(self.conn.cursor()) as cursor:
            cursor.execute(query, (self.user_id,))
            bookings = cursor.fetchall()
        return [Booking(*booking) for booking in bookings]

    def get_notification_list(self) -> List['Notification']:
        query = "SELECT * FROM Notification WHERE user_id = %s"
        with closing(self.conn.cursor()) as cursor:
            cursor.execute(query, (self.user_id,))
            notifications = cursor.fetchall()
        return [Notification(*notification) for notification in notifications]

    def make_booking(self, screening_id: int, number_of_seats: int, seat_ids: List[int]) -> str:
        try:
            with closing(self.conn.cursor()) as cursor:
                # Check if the screening is valid
                query = "SELECT * FROM Screening WHERE screening_id = %s"
                cursor.execute(query, (screening_id,))
                screening = cursor.fetchone()
                if not screening:
                    return "Invalid screening ID."

                # Check if the seats are valid and available
                for seat_id in seat_ids:
                    query = "SELECT * FROM CinemaHallSeat WHERE seat_id = %s AND hall_id = %s AND is_reserved = 0"
                    cursor.execute(query, (seat_id, screening['hall_id']))
                    seat = cursor.fetchone()
                    if not seat:
                        return f"Seat ID {seat_id} is invalid or already reserved."

                # Insert booking
                query = "INSERT INTO Booking (user_id, screening_id, number_of_seats, created_on, status, order_total) VALUES (%s, %s, %s, NOW(), 1, %s)"
                cursor.execute(query, (self.user_id, screening_id, number_of_seats, 0))  # Assuming order_total as 0 for simplicity
                booking_id = cursor.lastrowid

                # Insert BookingSeat entries and mark seats as reserved
                for seat_id in seat_ids:
                    query = "INSERT INTO BookingSeat (booking_id, seat_id) VALUES (%s, %s)"
                    cursor.execute(query, (booking_id, seat_id))
                    query = "UPDATE CinemaHallSeat SET is_reserved = 1 WHERE seat_id = %s"
                    cursor.execute(query, (seat_id,))

            self.conn.commit()
            return "Booking successful!"
        except Exception as e:
            self.conn.rollback()
            return f"An error occurred while making the booking: {str(e)}"

    def cancel_booking(self, booking_id: int) -> str:
        try:
            with closing(self.conn.cursor()) as cursor:
                # Check if the booking belongs to the user
                query = "SELECT * FROM Booking WHERE booking_id = %s AND user_id = %s"
                cursor.execute(query, (booking_id, self.user_id))
                booking = cursor.fetchone()
                if not booking:
                    return "Invalid booking ID or this booking does not belong to you."

                # Get all seat IDs associated with the booking
                query = "SELECT seat_id FROM BookingSeat WHERE booking_id = %s"
                cursor.execute(query, (booking_id,))
                seat_ids = [seat_id for (seat_id,) in cursor.fetchall()]

                # Update seats to not reserved
                for seat_id in seat_ids:
                    query = "UPDATE CinemaHallSeat SET is_reserved = 0 WHERE seat_id = %s"
                    cursor.execute(query, (seat_id,))

                # Delete BookingSeat entries
                query = "DELETE FROM BookingSeat WHERE booking_id = %s"
                cursor.execute(query, (booking_id,))

                # Delete booking
                query = "DELETE FROM Booking WHERE booking_id = %s"
                cursor.execute(query, (booking_id,))
                
            self.conn.commit()
            return "Booking cancelled successfully!"
        except Exception as e:
            self.conn.rollback()
            return f"An error occurred while cancelling the booking: {str(e)}"
        
class Movie:
    def __init__(self, title: str, lang: str, genre: str, rDate: date, duration: int, country: str, description: str, screeningList: List['Screening'] = []):
        self.__title = title
        self.__lang = lang
        self.__genre = genre
        self.__rDate = rDate
        self.__duration = duration
        self.__country = country
        self.__screeningList = screeningList
        self.__description = description

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        """Set the movie title."""
        if not value:
            raise ValueError("Title cannot be empty")
        self.__title = value

    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self, value):
        if not value:
            raise ValueError("Language cannot be empty")
        self.__lang = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if not value:
            raise ValueError("Genre cannot be empty")
        self.__genre = value

    @property
    def rDate(self):
        return self.__rDate

    @rDate.setter
    def rDate(self, value):
        if not value:
            raise ValueError("Release date cannot be empty")
        self.__rDate = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if not value:
            raise ValueError("Duration cannot be empty")
        self.__duration = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if not value:
            raise ValueError("Country cannot be empty")
        self.__country = value

    @property
    def screeningList(self) -> List['Screening']:
        return self.__screeningList

    @screeningList.setter
    def screeningList(self, value: List['Screening']) -> None:
        if not value:
            raise ValueError("Screening list cannot be empty")
        self.__screeningList = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Description cannot be empty")
        self.__description = value

    def get_screenings(self) -> List['Screening']:
        return self.__screeningList
    
    def __str__(self):
        print("movie str called")
        return f"{self.title} ({self.rDate}), {self.genre}, {self.duration} mins"

class Screening:
    def __init__(self, screening_date: datetime, start_time: datetime, end_time: datetime, hall: 'CinemaHall'):
        self.__screening_date = screening_date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__hall = hall

    @property
    def screening_date(self) -> datetime:
        return self.__screening_date

    @screening_date.setter
    def screening_date(self, value: datetime) -> None:
        if not isinstance(value, datetime):
            raise TypeError("screening_date must be a datetime object")
        self.__screening_date = value

    @property
    def start_time(self) -> datetime:
        return self.__start_time

    @start_time.setter
    def start_time(self, value: datetime) -> None:
        if not isinstance(value, datetime):
            raise TypeError("start_time must be a datetime object")
        self.__start_time = value

    @property
    def end_time(self) -> datetime:
        return self.__end_time

    @end_time.setter
    def end_time(self, value: datetime) -> None:
        if not isinstance(value, datetime):
            raise TypeError("end_time must be a datetime object")
        if value <= self.start_time:
            raise ValueError("end_time must be after start_time")
        self.__end_time = value

    @property
    def hall(self) -> 'CinemaHall':
        return self.__hall

    @hall.setter
    def hall(self, value: 'CinemaHall') -> None:
        if not isinstance(value, CinemaHall):
            raise TypeError("hall must be a CinemaHall object")
        self.__hall = value

    def __repr__(self) -> str:
        return f"Screening(screening_date={self.screening_date}, start_time={self.start_time}, end_time={self.end_time}, hall={self.hall})"
    
class CinemaHall:
    def __init__(self, name: str, total_seats: int, list_of_seats: List['CinemaHallSeat']):
        self.__name = name
        self.__total_seats = total_seats
        self.__list_of_seats = list_of_seats

    # getter for name
    @property
    def name(self) -> str:
        return self.__name

    # setter for name
    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def total_seats(self) -> int:
        return self.__total_seats

    @total_seats.setter
    def total_seats(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Total seats must be a positive integer")
        self.__total_seats = value

    @property
    def list_of_seats(self) -> List['CinemaHallSeat']:
        return self.__list_of_seats

    @list_of_seats.setter
    def list_of_seats(self, value: List['CinemaHallSeat']) -> None:
        if not isinstance(value, list):
            raise TypeError("List of seats must be a list")
        if len(value) != self.total_seats:
            raise ValueError("Length of list of seats must be equal to total seats")
        self.__list_of_seats = value
    
    def __repr__(self) -> str:
        return f"CinemaHall(name={self.name}, total_seats={self.total_seats})"
        
class CinemaHallSeat:
    def __init__(self, seat_number: int, seat_column: int, seat_type: int, is_reserved: bool, seat_price: float):
        self.__seat_number = seat_number
        self.__seat_column = seat_column
        self.__seat_type = seat_type
        self.__is_reserved = is_reserved
        self.__seat_price = seat_price

    @property
    def seat_number(self) -> int:
        return self.__seat_number

    @seat_number.setter
    def seat_number(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Seat number must be a positive integer")
        self.__seat_number = value

    @property
    def seat_column(self) -> int:
        return self.__seat_column

    @seat_column.setter
    def seat_column(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Seat column must be a positive integer")
        self.__seat_column = value

    @property
    def seat_type(self) -> int:
        return self.__seat_type

    @seat_type.setter
    def seat_type(self, value: int) -> None:
        self.__seat_type = value

    @property
    def is_reserved(self) -> bool:
        return self.__is_reserved

    @is_reserved.setter
    def is_reserved(self, value: bool) -> None:
        self.__is_reserved = value

    @property
    def seat_price(self) -> float:
        return self.__seat_price

    @seat_price.setter
    def seat_price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Seat price cannot be negative")
        self.__seat_price = value
    
    def __repr__(self) -> str:
        return f"CinemaHallSeat(seat_number={self.seat_number}, seat_column={self.seat_column}, seat_type={self.seat_type}, is_reserved={self.is_reserved}, seat_price={self.seat_price})"

class Booking:
    def __init__(self, booking_num: str, customer: 'Customer', number_of_seats: int, created_on: date, status: int, 
                 screening_seat_info: 'ScreeningSeat', screening_detail: 'Screening', seats: List['CinemaHallSeat'], order_total: float):
        self.__booking_num = booking_num
        self.__customer = customer
        self.__number_of_seats = number_of_seats
        self.__created_on = created_on
        self.__status = status
        self.__screening_seat_info = screening_seat_info
        self.__screening_detail = screening_detail
        self.__seats = seats
        self.__order_total = order_total

    @property
    def booking_num(self) -> str:
        return self.__booking_num

    @booking_num.setter
    def booking_num(self, value: str):
        self.__booking_num = value

    @property
    def customer(self) -> 'Customer':
        return self.__customer

    @customer.setter
    def customer(self, value: 'Customer'):
        self.__customer = value

    @property
    def number_of_seats(self) -> int:
        return self.__number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, value: int):
        self.__number_of_seats = value

    @property
    def created_on(self) -> date:
        return self.__created_on

    @created_on.setter
    def created_on(self, value: date):
        self.__created_on = value

    @property
    def status(self) -> int:
        return self.__status

    @status.setter
    def status(self, value: int):
        self.__status = value

    @property
    def screening_seat_info(self) -> 'ScreeningSeat':
        return self.__screening_seat_info

    @screening_seat_info.setter
    def screening_seat_info(self, value: 'ScreeningSeat'):
        self.__screening_seat_info = value

    @property
    def screening_detail(self) -> 'Screening':
        return self.__screening_detail

    @screening_detail.setter
    def screening_detail(self, value: 'Screening'):
        self.__screening_detail = value

    @property
    def seats(self) -> List['CinemaHallSeat']:
        return self.__seats

    @seats.setter
    def seats(self, value: List['CinemaHallSeat']):
        self.__seats = value

    @property
    def order_total(self) -> float:
        return self.__order_total

    @order_total.setter
    def order_total(self, value: float):
        self.__order_total = value

    def payment_detail(self) -> 'Payment':
            with closing(db.get_connection()) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM Payment WHERE booking_id = %s", (self.booking_num,))
                    result = cursor.fetchone()
                    if result:
                        return Payment(result['amount'], result['created_on'], result['payment_id'])
                    else:
                        return None

    def send_notification(self, content: str) -> 'Notification':
        created_on = datetime.now()
        with closing(db.get_connection()) as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO Notification (user_id, created_on, content) VALUES (%s, %s, %s)", 
                               (self.customer.user_id, created_on, content))
                conn.commit()
                notification_id = cursor.lastrowid
                return Notification(notification_id, created_on, content)
    
class Notification:
    def __init__(self, notification_id: int, created_on: date, content: str):
        self.__notification_id = notification_id
        self.__created_on = created_on
        self.__content = content

    @property
    def notification_id(self) -> int:
        return self.__notification_id

    @notification_id.setter
    def notification_id(self, value: int):
        self.__notification_id = value

    @property
    def created_on(self) -> date:
        return self.__created_on

    @created_on.setter
    def created_on(self, value: date):
        self.__created_on = value

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str):
        self.__content = value

class Payment(ABC):
    def __init__(self, amount: float, created_on: datetime, payment_id: int, coupon: Optional['Coupon'] = None):
        self.__amount = amount
        self.__created_on = created_on
        self.__payment_id = payment_id
        self.__coupon = coupon

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def created_on(self) -> datetime:
        return self.__created_on

    @property
    def payment_id(self) -> int:
        return self.__payment_id

    @property
    def coupon(self) -> Optional['Coupon']:
        return self.__coupon

    @coupon.setter
    def coupon(self, coupon: 'Coupon'):
        if coupon.is_valid():
            self.__coupon = coupon
        else:
            return "The coupon is not valid."

    def apply_coupon(self, coupon: 'Coupon'):
        self.coupon = coupon

    def calc_discount(self) -> float:
        if self.__coupon:
            return self.__coupon.discount
        return 0.0

    def calc_final_payment(self) -> float:
        discount = self.calc_discount()
        return self.__amount - (self.__amount * discount / 100)
    
class Coupon:
    def __init__(self, coupon_id: str, expiry_date: datetime, discount: float):
        self.__coupon_id = coupon_id
        self.__expiry_date = expiry_date
        self.__discount = discount

    @property
    def coupon_id(self) -> str:
        return self.__coupon_id

    @property
    def expiry_date(self) -> datetime:
        return self.__expiry_date

    @property
    def discount(self) -> float:
        return self.__discount

    def is_valid(self) -> bool:
        return datetime.now() < self.__expiry_date
    
class CreditCardPayment(Payment):
    def __init__(self, amount: float, created_on: datetime, payment_id: int, credit_card_number: str, card_type: str, expiry_date: datetime, name_on_card: str, coupon: Optional[Coupon] = None):
        super().__init__(amount, created_on, payment_id, coupon)
        self.__credit_card_number = credit_card_number
        self.__card_type = card_type
        self.__expiry_date = expiry_date
        self.__name_on_card = name_on_card

    @property
    def credit_card_number(self) -> str:
        return self.__credit_card_number

    @credit_card_number.setter
    def credit_card_number(self, value: str):
        self.__credit_card_number = value

    @property
    def card_type(self) -> str:
        return self.__card_type

    @card_type.setter
    def card_type(self, value: str):
        self.__card_type = value

    @property
    def expiry_date(self) -> datetime:
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value: datetime):
        self.__expiry_date = value

    @property
    def name_on_card(self) -> str:
        return self.__name_on_card

    @name_on_card.setter
    def name_on_card(self, value: str):
        self.__name_on_card = value
    
class DebitCardPayment(Payment):
    def __init__(self, amount: float, created_on: datetime, payment_id: int, card_number: str, bank_name: str, name_on_card: str, coupon: Optional[Coupon] = None):
        super().__init__(amount, created_on, payment_id, coupon)
        self.__card_number = card_number
        self.__bank_name = bank_name
        self.__name_on_card = name_on_card

    @property
    def card_number(self) -> str:
        return self.__card_number

    @card_number.setter
    def card_number(self, value: str):
        self.__card_number = value

    @property
    def bank_name(self) -> str:
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, value: str):
        self.__bank_name = value

    @property
    def name_on_card(self) -> str:
        return self.__name_on_card

    @name_on_card.setter
    def name_on_card(self, value: str):
        self.__name_on_card = value

class ScreeningSeat:
    def __init__(self, cinema_hall_seat: CinemaHallSeat):
        self.cinema_hall_seat = cinema_hall_seat

    def reserve(self, db):
        if not self.cinema_hall_seat.is_reserved:
            self.cinema_hall_seat.is_reserved = True
            db.execute("UPDATE CinemaHallSeat SET is_reserved = TRUE WHERE seat_id = %s", (self.cinema_hall_seat.seat_id,))
        else:
            raise ValueError("Seat is already reserved")

    def release(self, db):
        if self.cinema_hall_seat.is_reserved:
            self.cinema_hall_seat.is_reserved = False
            db.execute("UPDATE CinemaHallSeat SET is_reserved = FALSE WHERE seat_id = %s", (self.cinema_hall_seat.seat_id,))
        else:
            raise ValueError("Seat is not reserved")
        
        
general = General()

# test search
search_result = general.search_movie_by_title('the')
print(search_result)
for movie in search_result:
    print(general.get_movie_details(movie))

# movie = Movie(
#     title='The Shawshank Redemption',
#     lang='English',
#     genre='Drama',
#     rDate=date(1994, 9, 23),
#     duration=142,
#     country='USA',
#     description='Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
#     screeningList=[]
# )

# print(str(movie))  # 这应该会调用 __str__ 方法并打印输出