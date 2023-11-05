from models import General, Guest, Person, User, Movie, Customer
from db import Database
from contextlib import closing


class GuestController:
    def __init__(self, db_connection):
        self.general = General()
        self.guest = Guest()
        self.db = db_connection
        # self.Movie = movie()

    def view_movie_details(self, search_term: str):
        try:
            print(f"view_movie_details is called with search_term={search_term}")
            movies = self.general.search_movie_by_search_term(search_term)
            print(f"view_movie_details found: {movies}")

            if not movies:
                print("No movies found with the specified criteria.")
                return "No movies found with the specified criteria."

            movie_details = [str(movie) for movie in movies]
            print(f"Returning from view_movie_details: {movie_details}")
            return movie_details
        except Exception as e:
            print(f"An error occurred in view_movie_details: {e}")
            # Optionally re-raise the exception if you want it to be handled by an outer try/except block or to crash the program
            raise
        
    def register_guest(self, username, password, name, address, email, phone):
        return self.guest.register(username, password, name, address, email, phone)

class UserController:
    def __init__(self, db_connection):
        self.db = db_connection
        self.current_user = None  
        self.is_logged_in = False  

    def login(self, username, password):

        user = User(username=username, password=password)  
        login_result = user.login(username, password)
        if login_result == "Login successful!":
            self.current_user = user
            self.is_logged_in = True
            self.load_user_details(username)
            return True
        else:
            return False

    def logout(self):

        if self.current_user:
            self.current_user.logout()
            self.current_user = None
            self.is_logged_in = False

class CustomerController(UserController):
    def __init__(self, db_connection):
        self.db = db_connection
        self.general = General()
        super().__init__(db_connection)
        # self.customer = Customer()
        
    def view_movie_details(self, search_term: str):
        try:
            print(f"view_movie_details is called with search_term={search_term}")
            movies = self.general.search_movie_by_search_term(search_term)
            print(f"view_movie_details found: {movies}")

            if not movies:
                print("No movies found with the specified criteria.")
                return "No movies found with the specified criteria."

            movie_details = [str(movie) for movie in movies]
            print(f"Returning from view_movie_details: {movie_details}")
            return movie_details
        except Exception as e:
            print(f"An error occurred in view_movie_details: {e}")
            # Optionally re-raise the exception if you want it to be handled by an outer try/except block or to crash the program
            raise
        
    def make_booking(self, screening_id, number_of_seats, seat_ids):
        if not self.is_logged_in or not isinstance(self.current_user, Customer):
            return "User must be logged in and must be a Customer to make a booking."

        return self.current_user.make_booking(screening_id, number_of_seats, seat_ids)

    def get_movie_id_by_title(self, title):
        if self.is_logged_in and self.current_user:
            return self.current_user.get_movie_id_by_title(title)
        else:
            print("User is not logged in or current_user is not set.")
            return None


    def get_movie_sessions(self, movie_id):
            with closing(self.db.get_connection()) as conn:
                with conn.cursor(dictionary=True) as cursor:
                    query = """
                    SELECT 
                        Movie.title, 
                        Screening.screening_date, 
                        CinemaHall.name AS hall_name, 
                        Screening.start_time, 
                        Screening.end_time,
                        Screening.screening_id
                    FROM 
                        Screening
                    JOIN Movie ON Screening.movie_id = Movie.movie_id
                    JOIN CinemaHall ON Screening.hall_id = CinemaHall.hall_id
                    WHERE 
                        Screening.movie_id = %s;
                    """
                    try:
                        cursor.execute(query, (movie_id,))
                        sessions = cursor.fetchall()
                        return sessions
                    except Exception as e:
                        print(f"An error occurred while fetching movie sessions: {e}")
                        return []

    def get_hall_seats(self, hall_name):
        with closing(self.db.get_connection()) as conn:
            with conn.cursor(dictionary=True) as cursor:
                query = """
                SELECT 
                    seat_id, 
                    seat_number, 
                    seat_column, 
                    seat_type, 
                    is_reserved, 
                    seat_price
                FROM 
                    CinemaHallSeat
                JOIN CinemaHall ON CinemaHallSeat.hall_id = CinemaHall.hall_id
                WHERE 
                    CinemaHall.name = %s
                ORDER BY 
                    seat_number, 
                    seat_column;
                """
                try:
                    cursor.execute(query, (hall_name,))
                    seats = cursor.fetchall()
                    return seats
                except Exception as e:
                    print(f"An error occurred while fetching hall seats: {e}")
                    return []



    def admin_add_movie(self, title, lang, genre, rDate, duration, country, description):
        with closing(self.db.get_connection()) as conn:
            with conn.cursor() as cursor:
                query = """
                INSERT INTO Movie (title, lang, genre, rDate, duration, country, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                """
                try:
                    cursor.execute(query, (title, lang, genre, rDate, duration, country, description))
                    conn.commit()  
                    return True  
                except Exception as e:
                    print(f"An error occurred while adding a new movie: {e}")
                    conn.rollback()  
                    return False  


    def admin_add_screening(self, movie_id, screening_date, start_time, end_time, hall_id):
        with closing(self.db.get_connection()) as conn:
            with conn.cursor() as cursor:
                query = """
                INSERT INTO Screening (movie_id, screening_date, start_time, end_time, hall_id)
                VALUES (%s, %s, %s, %s, %s);
                """
                try:
                    cursor.execute(query, (movie_id, screening_date, start_time, end_time, hall_id))
                    conn.commit()  
                    return True  
                except Exception as e:
                    print(f"An error occurred while adding a new screening: {e}")
                    conn.rollback()  
                    return False  


    def admin_cancel_movie(self, movie_id):

        with closing(self.db.get_connection()) as conn:
            with conn.cursor() as cursor:
                cancel_screenings_query = """
                DELETE FROM Screening WHERE movie_id = %s;
                """
                try:
                    cursor.execute(cancel_screenings_query, (movie_id,))
                    cancel_movie_query = """
                    DELETE FROM Movie WHERE movie_id = %s;
                    """
                    cursor.execute(cancel_movie_query, (movie_id,))
                    conn.commit()
                    return True
                except Exception as e:
                    print(f"An error occurred while cancelling the movie: {e}")
                    conn.rollback()
                    return False

    def admin_cancel_screening(self, screening_id):
        with closing(self.db.get_connection()) as conn:
            with conn.cursor() as cursor:
                query = """
                DELETE FROM Screening WHERE screening_id = %s;
                """
                try:
                    cursor.execute(query, (screening_id,))
                    conn.commit()
                    return True
                except Exception as e:
                    print(f"An error occurred while cancelling the screening: {e}")
                    conn.rollback()
                    return False


    def staff_make_booking(self, user_id, screening_id, seat_ids):
        with closing(self.db.get_connection()) as conn:
            with conn.cursor() as cursor:
                try:
                    create_booking_query = """
                    INSERT INTO Booking (user_id, screening_id, number_of_seats, created_on, status, order_total)
                    VALUES (%s, %s, %s, NOW(), 1, (SELECT SUM(seat_price) FROM CinemaHallSeat WHERE seat_id IN (%s)));
                    """
                    cursor.execute(create_booking_query, (user_id, screening_id, len(seat_ids), ','.join(map(str, seat_ids))))

                    booking_id = cursor.lastrowid  

                    for seat_id in seat_ids:
                        create_booking_seat_query = """
                        INSERT INTO BookingSeat (booking_id, seat_id)
                        VALUES (%s, %s);
                        """
                        cursor.execute(create_booking_seat_query, (booking_id, seat_id))
                    conn.commit()
                    return True
                except Exception as e:
                    print(f"An error occurred while making a booking: {e}")
                    conn.rollback()
                    return False


    def staff_cancel_booking(self, booking_id):
        with closing(self.db.get_connection()) as conn:
            with conn.cursor() as cursor:
                try:
                    update_booking_query = """
                    UPDATE Booking SET status = 0 WHERE booking_id = %s;
                    """
                    cursor.execute(update_booking_query, (booking_id,))

                    release_seats_query = """
                    UPDATE CinemaHallSeat SET is_reserved = FALSE WHERE seat_id IN (
                        SELECT seat_id FROM BookingSeat WHERE booking_id = %s
                    );
                    """
                    cursor.execute(release_seats_query, (booking_id,))

                    conn.commit()
                    return True
                except Exception as e:
                    print(f"An error occurred while cancelling a booking: {e}")
                    conn.rollback()
                    return False


    def customer_cancel_booking(self, booking_id):
        with closing(self.db.get_connection()) as conn:
            with conn.cursor() as cursor:
                try:
                    update_booking_query = """
                    UPDATE Booking SET status = 0 WHERE booking_id = %s;
                    """
                    cursor.execute(update_booking_query, (booking_id,))
                    release_seats_query = """
                    UPDATE CinemaHallSeat SET is_reserved = FALSE WHERE seat_id IN (
                        SELECT seat_id FROM BookingSeat WHERE booking_id = %s
                    );
                    """
                    cursor.execute(release_seats_query, (booking_id,))

                    conn.commit()
                    return True
                except Exception as e:
                    print(f"An error occurred while cancelling a booking: {e}")

                    conn.rollback()
                    return False


    def customer_view_booking_list(self, user_id):
        with closing(self.db.get_connection()) as conn:
            with conn.cursor(dictionary=True) as cursor:
                try:
                    booking_query = """
                    SELECT * FROM Booking WHERE user_id = %s;
                    """
                    cursor.execute(booking_query, (user_id,))
                    bookings = cursor.fetchall()
                    return bookings
                except Exception as e:
                    print(f"An error occurred while fetching the booking list: {e}")
                    return []


    def customer_view_notifications(self, user_id):
        with closing(self.db.get_connection()) as conn:
            with conn.cursor(dictionary=True) as cursor:
                try:
                    notification_query = """
                    SELECT * FROM Notification WHERE user_id = %s ORDER BY created_on DESC;
                    """
                    cursor.execute(notification_query, (user_id,))
                    notifications = cursor.fetchall()
                    return notifications
                except Exception as e:
                    print(f"An error occurred while fetching notifications: {e}")
                    return []

    
    
# controller = GuestController()
# result = controller.general.search_movie_by_search_term(search_term="the")
# print(result)
# print("Before calling view_movie_details")
# a = controller.view_movie_details("the")
# print("After calling view_movie_details")
# print(a)

