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
        self.current_user = None  # 当前用户的用户对象
        self.is_logged_in = False  # 登录状态

    def login(self, username, password):
        # 验证用户名和密码
        user = User(username=username, password=password)  # 这里您可能需要传递一个连接或其他必需的参数来创建User对象
        login_result = user.login(username, password)
        if login_result == "Login successful!":
            self.current_user = user
            self.is_logged_in = True
            # 加载用户的其他详细信息
            self.load_user_details(username)
            return True
        else:
            return False

    def load_user_details(self, username):
        # 根据用户名加载用户的其他详细信息
        # 这可能会涉及到从数据库中查询并更新self.current_user对象的属性
        pass

    def logout(self):
        # 处理用户登出逻辑
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





































    # def close_database(self):
    #     # close the database connection using the close_connection method of the Database class
    #     self.db_instance.close_connection()



    def reset_password(self, user_id, old_password, new_password):
        # Logic for resetting password
        pass

    def admin_add_movie(self, title, lang, genre, rDate, duration, country, description):
        # Logic for admin to add a new movie
        pass

    def admin_add_screening(self, movie_id, screening_date, start_time, end_time, hall_id):
        # Logic for admin to add a new screening
        pass

    def admin_cancel_movie(self, movie_id):
        # Logic for admin to cancel a movie
        pass

    def admin_cancel_screening(self, screening_id):
        # Logic for admin to cancel a screening
        pass

    def staff_make_booking(self, user_id, screening_id, seat_ids):
        # Logic for front desk staff to make a booking
        pass

    def staff_cancel_booking(self, booking_id):
        # Logic for front desk staff to cancel a booking
        pass

    def customer_make_booking(self, user_id, screening_id, seat_ids):
        # Logic for customer to make a booking
        pass

    def customer_cancel_booking(self, booking_id):
        # Logic for customer to cancel a booking
        pass

    def customer_view_booking_list(self, user_id):
        # Logic for customer to view their booking list
        pass

    def customer_view_notifications(self, user_id):
        # Logic for customer to view their notifications
        pass
    
    
# controller = GuestController()
# result = controller.general.search_movie_by_search_term(search_term="the")
# print(result)
# print("Before calling view_movie_details")
# a = controller.view_movie_details("the")
# print("After calling view_movie_details")
# print(a)

