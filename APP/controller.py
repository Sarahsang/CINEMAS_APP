from models import General, Guest, Movie

class GuestController:
    def __init__(self):
        self.general = General()
        self.guest = Guest()
        # self.Movie = movie()

    def search_movies(self, title=None, lang=None, genre=None, rDate=None):
        print(f"search_movies in controller is called with title={title}, lang={lang}, genre={genre}, rDate={rDate}")
        movies = []
        if title:
            movies = self.general.search_movie_by_title(title)
        elif lang:
            movies = self.general.search_movie_by_lang(lang)
        elif genre:
            movies = self.general.search_movie_by_genre(genre)
        elif rDate:
            movies = self.general.search_movie_by_date(rDate)
        print(f"search_movies returning: {movies}")
        return movies

    def view_movie_details(self, title=None, lang=None, genre=None, rDate=None):
        print(f"view_movie_details is called with title={title}, lang={lang}, genre={genre}, rDate={rDate}")
        movies = self.search_movies(title, lang, genre, rDate)
        print(f"view_movie_details found: {movies}")
        if movies:
            for movie in movies:
                print(str(movie))
            return [str(movie) for movie in movies]
        else:
            return "No movies found with the specified criteria."
        
    def register_guest(self, username, password, name, address, email, phone):
        return self.guest.register(username, password, name, address, email, phone)









































    def close_database(self):
        # close the database connection using the close_connection method of the Database class
        self.db_instance.close_connection()

    def search_movie_by_title(self, title):
        # Logic to search for movie by title
        pass

    def search_movie_by_lang(self, lang):
        # Logic to search for movie by language
        pass

    def search_movie_by_genre(self, genre):
        # Logic to search for movie by genre
        pass

    def search_movie_by_date(self, rDate):
        # Logic to search for movie by release date
        pass

    def view_movie_details(self, movie_id):
        # Logic to view details for a specific movie
        pass

    def guest_register(self, username, password, name, address, email, phone):
        # Logic for guest to register
        pass

    def user_login(self, username, password):
        # Logic for user login
        pass

    def user_logout(self, user_id):
        # Logic for user logout
        pass

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
    
    
controller = GuestController()
result = controller.search_movies(title="the")
print(result)
