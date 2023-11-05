import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from controller import GuestController
from controller import UserController, CustomerController
from models import General
import re
from db import Database

db = Database('localhost', 'root', 'root', 'online_booking_system_dbase')

customer_controller = CustomerController(db)


class FirstPage(tk.Frame):
    def __init__(self, parent, controller, guest_controller, user_controller, customer_controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.guest_controller = guest_controller
        self.user_controller = user_controller
        self.customer_controller = customer_controller
        
        load = Image.open("APP\imag1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0, y=0)
        
        self.search_entry = tk.Entry(self, width=20, font=('Arial Bold', 12))
        self.search_entry.place(x=20, y=30) 

        self.search_button = tk.Button(self, text="Search Movie", font=("Arial Bold", 8), bg='ivory',command=self.search_movies)
        self.search_button.place(x=220, y=30) 
        
        self.border = tk.LabelFrame(self, text="Login", bg='ivory', bd=10, font=('Arial, 20'))
        self.border.pack(fill="both", expand="yes", padx= 100, pady=150)

        self.L1 = tk.Label(self.border, text="Username", font=("Arial Bold", 15), bg='ivory')
        self.L1.place(x=50, y=20)
        self.T1 = tk.Entry(self.border, width=30, bd=5)
        self.T1.place(x=180, y=20)

        self.L2 = tk.Label(self.border, text="Password", font=("Arial Bold", 15), bg='ivory')
        self.L2.place(x=50, y=80)
        self.T2 = tk.Entry(self.border, width=30, show='*', bd=5)
        self.T2.place(x=180, y=80)

        self.B1 = tk.Button(self.border, text="Submit", font=("Arial", 15), command=self.verify)
        self.B1.place(x=320, y=115)
        
        self.B2 = tk.Button(self, text="Register", bg='dark orange', font=("Arial",15), command = self.register)
        self.B2.place(x=650, y=20)
        
    def search_movies(self):
        print("search_movies in view is called")
        search_term = self.search_entry.get()

        if search_term:
            result = self.guest_controller.view_movie_details(search_term)
            print("Result:", result)  

            if isinstance(result, list):
                print("search_movies in view is called")
                self.controller.show_frame(SearchResultPage)
                self.controller.frames[SearchResultPage].display_results(result, from_page="FirstPage")
            else:
                messagebox.showinfo("Search Result", result)
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")
         
    def verify(self):
        uname = self.T1.get()
        pswd = self.T2.get()
        if not uname or not pswd:
            messagebox.showwarning("Warning", "Please enter both username and password.")
            return
        
        if self.user_controller.login(uname, pswd):
            self.controller.show_frame(MainPage)
        else:
            messagebox.showinfo("Error", "Incorrect Username and Password")
            

    def register(self):
        window=tk.Toplevel()
        window.resizable(0,0)
        window.configure(bg="deep sky blue")
        window.title("Register")
        
        default_username = 'e.g., john_doe99'
        default_name = 'e.g., John Doe'
        default_address = 'e.g., 456 Oak St, Lincoln'
        default_email = 'e.g., john.doe@email.com'
        default_phone = 'e.g., 123-456-7892'
        
        l1 = tk.Label(window, text="Username:", font=("Arial", 15), bg="deep sky blue")
        l1.place(x=10, y=10)
        t1 = tk.Entry(window, width=30, bd=5, fg='grey')
        t1.insert(0, default_username)
        t1.place(x=200, y=10)

        l2 = tk.Label(window, text="Password:", font=("Arial", 15), bg="deep sky blue")
        l2.place(x=10, y=60)
        t2 = tk.Entry(window, width=30, bd=5, show="*")
        t2.place(x=200, y=60)

        l3 = tk.Label(window, text="Confirm Password:", font=("Arial", 15), bg="deep sky blue")
        l3.place(x=10, y=110)
        t3 = tk.Entry(window, width=30, bd=5, show="*")
        t3.place(x=200, y=110)
        
        l4 = tk.Label(window, text="name:", font=("Arial", 15), bg="deep sky blue")
        l4.place(x=10, y=160)
        t4 = tk.Entry(window, width=30, bd=5, fg='grey')
        t4.insert(0, default_name)
        t4.place(x=200, y=160)
        
        l5 = tk.Label(window, text="address", font=("Arial", 15), bg="deep sky blue")
        l5.place(x=10, y=210)
        t5 = tk.Entry(window, width=30, bd=5, fg='grey')
        t5.insert(0, default_address)
        t5.place(x=200, y=210)
        
        l6 = tk.Label(window, text="email:", font=("Arial", 15), bg="deep sky blue")
        l6.place(x=10, y=260)
        t6 = tk.Entry(window, width=30, bd=5, fg='grey')
        t6.insert(0, default_email)
        t6.place(x=200, y=260)
        
        l7 = tk.Label(window, text="phone", font=("Arial", 15), bg="deep sky blue")
        l7.place(x=10, y=310)
        t7 = tk.Entry(window, width=30, bd=5, fg='grey')
        t7.insert(0, default_phone)
        t7.place(x=200, y=310)

        def check():
            username = t1.get()
            password = t2.get()
            confirm_password = t3.get()
            name = t4.get()
            address = t5.get()
            email = t6.get()
            phone = t7.get()
            if not all([username, password, confirm_password, name, address, email, phone]):
                messagebox.showinfo("Error", "Please complete all fields")
                return
            if password != confirm_password:
                messagebox.showinfo("Error", "Passwords do not match")
                return

            registration_result = self.guest_controller.register_guest(username, password, name, address, email, phone)

            if registration_result == "Registration successful!":
                messagebox.showinfo("Welcome", "Successfully Registered")
                window.destroy() 
            else:
                messagebox.showinfo("Error", registration_result) 

        b1 = tk.Button(window, text="Sign In", font=("Arial",15), bg="yellow", command = check)
        b1.place(x=170, y=410)

        window.geometry("479x600")
        window.mainloop()

class MainPage(tk.Frame):
    def __init__(self, parent, controller, guest_controller, user_controller, customer_controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.guest_controller = guest_controller
        self.user_controller = user_controller
        self.customer_controller = customer_controller

        load = Image.open("APP\imag1.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0, y=0)

        Label = tk.Label(self, text="Welcome to Lincoln Cinemas", font=("Arial Bold", 30))
        Label.place(x=120, y=210)

        Button = tk.Button(self, text="Next", font=("Arial",15), command = lambda:controller.show_frame(ThirdPage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial",15), command = lambda:controller.show_frame(FirstPage))
        Button.place(x=100, y=450)

        self.search_entry = tk.Entry(self, width=20, font=('Arial Bold', 12))
        self.search_entry.place(x=20, y=30) 

        self.search_button = tk.Button(self, text="Search Movie", font=("Arial Bold", 8), bg='ivory',command=self.search_movies)
        self.search_button.place(x=220, y=30) 
        
    def search_movies(self):
        print("search_movies in view is called")
        search_term = self.search_entry.get()

        if search_term:
            result = self.customer_controller.view_movie_details(search_term)
            print("Result:", result)  

            if isinstance(result, list):
                print("search_movies in view is called")
                self.controller.show_frame(SearchResultPage)
                self.controller.frames[SearchResultPage].display_results(result, from_page="MainPage")
            else:
                messagebox.showinfo("Search Result", result)
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")
            
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller, guest_controller, user_controller, customer_controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.guest_controller = guest_controller
        self.user_controller = user_controller
        self.customer_controller = customer_controller

        Label = tk.Label(self, text="Third Page", font=("Arial Bold", 30))
        Label.place(x=230, y=230)

        Button = tk.Button(self, text="Next", font=("Arial",15), command = lambda:controller.show_frame(FirstPage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial",15), command = lambda:controller.show_frame(MainPage))
        Button.place(x=100, y=450)

class SearchResultPage(tk.Frame):
    def __init__(self, parent, controller, guest_controller, user_controller, customer_controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.guest_controller = guest_controller
        self.user_controller = user_controller
        self.customer_controller = customer_controller
        self.from_page = None
        self.movie_ids = []
        
        self.back_button = tk.Button(self, text="Back", font=("Arial",13), command=self.go_back)
        self.back_button.place(x=710, y=37)
        
        self.title_label = tk.Label(self, text="Movie Search Results", font=("Arial", 18))
        self.title_label.pack(side="top", fill="x", pady=10)
        
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side="right", fill="y")
        
        self.results_listbox = tk.Listbox(self, height=20, width=50, yscrollcommand=self.scrollbar.set, font=('Arial', 12))
        self.results_listbox.pack(pady=(20, 0), padx=20, fill='both', expand=True)
        self.scrollbar.config(command=self.results_listbox.yview)
        self.results_listbox.bind('<<ListboxSelect>>', self.on_select)
        
    def go_back(self):
            if self.from_page == "FirstPage":
                self.controller.show_frame(FirstPage)
            elif self.from_page == "MainPage":
                self.controller.show_frame(MainPage)

    def display_results(self, results, from_page):
        self.from_page = from_page
        self.results_listbox.delete(0, tk.END)
        self.movie_ids.clear()  
        print(f"Results type: {type(results)}")  
        if results:  
            print(f"First result type: {type(results[0])}")  
            print(f"First result content: {results}")  
        for movie_detail in results:
            movie_id_str, _, movie_info = movie_detail.partition(' ')  
            movie_id = int(movie_id_str)  
            self.results_listbox.insert(tk.END, movie_info)  
            self.movie_ids.append(movie_id) 
        print(f"movie_ids after search: {self.movie_ids}")

    def on_select(self, event):

        widget = event.widget
        selection = widget.curselection()
        print(f"Selection: {selection}")
        if selection:
            index = int(selection[0])  
            value = widget.get(index)  
            print(f"on_Selected: {value}")

            if index < len(self.movie_ids):
                movie_id = self.movie_ids[index]
                try:
                    movie_sessions = self.customer_controller.get_movie_sessions(movie_id)
                    
                    if self.from_page == "MainPage":
                        booking_page = self.controller.frames[BookingPage]
                        booking_page.set_movie_sessions(movie_sessions)
                        self.controller.show_frame(BookingPage)
                        
                except Exception as e:
                    print(f"An error occurred while fetching movie sessions: {e}")
            else:
                print(f"Error: index {index} is out of range.")
        else:
            print("No item selected.")

class BookingPage(tk.Frame):
    def __init__(self, parent, controller, guest_controller, user_controller, customer_controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 页面标题
        self.header_label = tk.Label(self, text="Make a Booking", font=("Arial", 24))
        self.header_label.pack(side="top", fill="x", pady=10)

        # 场次列表框
        self.session_listbox = tk.Listbox(self, height=10, width=50, font=('Arial', 12))
        self.session_listbox.pack(pady=20, padx=20, fill='both', expand=True)

        # 预订按钮
        self.book_button = tk.Button(self, text="Book Session", font=("Arial", 15), command=self.book_session)
        self.book_button.pack(side="bottom", pady=20)

        # 返回按钮
        self.back_button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SearchResultPage))
        self.back_button.pack(side="bottom", pady=10)

    def set_movie_sessions(self, movie_sessions):
        self.session_listbox.delete(0, tk.END)
        for session in movie_sessions:
            session_str = f"{session['screening_date']} - {session['start_time']} to {session['end_time']} in {session['hall_name']}"
            self.session_listbox.insert(tk.END, session_str)

    def book_session(self):
        try:
            selected_index = self.session_listbox.curselection()[0]
            selected_session = self.session_listbox.get(selected_index)
            hall_name = selected_session.split(' in ')[-1]
            # 现在我们跳转到选择座位的页面，并传递大厅名称
            select_seat_page = self.controller.frames[SelectSeatPage]
            select_seat_page.display_seats(hall_name)
            self.controller.show_frame(SelectSeatPage)
        except IndexError:
            tk.messagebox.showwarning("Selection Error", "Please select a session to book.")


    def get_movie_info(self, movie_id):
        print(f"Getting sessions for movie ID: {movie_id}")  # 调试打印
        sessions = self.customer_controller.get_movie_sessions(movie_id)
        if sessions:
            self.display_sessions(sessions)
        else:
            print("No sessions found for this movie.")  # 如果没有找到场次，打印提示

    def display_sessions(self, sessions):
        print(f"Displaying sessions: {sessions}")  # 调试打印
        self.session_listbox.delete(0, tk.END)  # 清空列表
        for session in sessions:
            self.session_listbox.insert(tk.END, f"{session['date']} - {session['time']} - Hall: {session['hall_name']}")


    def update_sessions(self, date_sessions):

        pass

        Button = tk.Button(self, text="Back", font=("Arial",15), command = lambda:controller.show_frame(SearchResultPage))
        Button.place(x=100, y=450)


class SelectSeatPage(tk.Frame):
    def __init__(self, parent, controller, guest_controller, user_controller, customer_controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.guest_controller = guest_controller
        self.user_controller = user_controller
        self.customer_controller = customer_controller

    def display_seats(self, hall_name):
        seats = self.customer_controller.get_hall_seats(hall_name)
        
        for seat in seats:
            button = tk.Button(self, text=f'{seat["seat_number"]}', bg='green' if not seat['is_reserved'] else 'red')
            button['command'] = lambda s=seat: self.select_seat(s) 
            button.grid(row=seat['seat_number'], column=seat['seat_column'])
            
        self.update_idletasks()

    def select_seat(self, seat):
        if seat['is_reserved']:
            messagebox.showwarning("Seat Selection", "This seat is already reserved.")
            return
        print(f"Seat {seat['seat_number']} selected.")


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        db = Database('localhost', 'root', 'root', 'online_booking_system_dbase')
        self.general = General()
        self.guest_controller = GuestController(db)
        self.user_controller = UserController(db)
        self.customer_controller = CustomerController(db)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, MainPage, ThirdPage, SearchResultPage, BookingPage, SelectSeatPage):
            frame = F(window, self, self.guest_controller, self.user_controller, self.customer_controller)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Cinema Application")

app = Application()
app.maxsize(800,500)
app.mainloop()


