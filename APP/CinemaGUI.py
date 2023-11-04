import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from controller import GuestController
from controller import UserController

class FirstPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.guest_controller = GuestController()
        self.user_controller = UserController()
        print("FirstPage initialized")
        
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
            print("Result:", result)  # 这会打印出 result 变量的内容

            if isinstance(result, list):
                print("search_movies in view is called")
                # messagebox.showinfo("Search Result", "\n".join(result))  # 删除这行
                self.controller.show_frame(SearchResultPage)  # 切换到搜索结果页面
                self.controller.frames[SearchResultPage].display_results(result, from_page="FirstPage")  # 显示结果
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

            # 确认密码是否匹配
            if password != confirm_password:
                messagebox.showinfo("Error", "Passwords do not match")
                return

            # 使用controller注册用户
            registration_result = self.guest_controller.register_guest(username, password, name, address, email, phone)
            
            # 根据注册结果显示消息
            if registration_result == "Registration successful!":
                messagebox.showinfo("Welcome", "Successfully Registered")
                window.destroy()  # 关闭注册窗口
            else:
                messagebox.showinfo("Error", registration_result) 

        b1 = tk.Button(window, text="Sign In", font=("Arial",15), bg="yellow", command = check)
        b1.place(x=170, y=410)

        window.geometry("479x600")
        window.mainloop()

class MainPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.guest_controller = GuestController()
        self.user_controller = UserController()

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
            result = self.guest_controller.view_movie_details(search_term)
            print("Result:", result)  # 这会打印出 result 变量的内容

            if isinstance(result, list):
                print("search_movies in view is called")
                # messagebox.showinfo("Search Result", "\n".join(result))  # 删除这行
                self.controller.show_frame(SearchResultPage)  # 切换到搜索结果页面
                self.controller.frames[SearchResultPage].display_results(result, from_page="MainPage")  # 显示结果
            else:
                messagebox.showinfo("Search Result", result)
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")
            
class ThirdPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)

        Label = tk.Label(self, text="Third Page", font=("Arial Bold", 30))
        Label.place(x=230, y=230)

        Button = tk.Button(self, text="Next", font=("Arial",15), command = lambda:controller.show_frame(FirstPage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial",15), command = lambda:controller.show_frame(MainPage))
        Button.place(x=100, y=450)

class SearchResultPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.from_page = None
        
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
        for result in results:
            self.results_listbox.insert(tk.END, result)

    def on_select(self, event):
        # 事件处理器，当用户选择一个结果时调用
        widget = event.widget
        index = int(widget.curselection()[0])  # 获取选中项的索引
        value = widget.get(index)  # 获取选中项的值

        # 切换到 BookingPage，并传递选中的电影信息
        if self.from_page == "FirstPage":
            messagebox.showinfo("Action Required", "Please register or login to book a movie.")
        elif self.from_page == "MainPage":
            booking_page = self.controller.frames[BookingPage]
            booking_page.get_movie_info(value)  # 需要在 BookingPage 中实现此方法
            self.controller.show_frame(BookingPage)

    def on_movie_selected(self, movie):
        booking_page = self.controller.frame(BookingPage)
        booking_page.set_movie_data(movie)
        self.controller.show_frame(BookingPage)


class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.movies = {}  # 这里应该填充从数据库获取的电影数据
        self.current_movie = None  # 当前选择的电影
        self.current_index = 0  # 当前日期索引

        # 页面布局代码...
        self.header_label = tk.Label(self, text="Make a Booking", font=("Arial", 24))
        self.header_label.pack(side="top", fill="x", pady=10)

        # 电影详细信息的标签
        self.movie_detail_label = tk.Label(self, text="", font=("Arial", 20))
        self.movie_detail_label.pack(side="top", fill="x", pady=20)
                # 初始化电影信息
        self.display_movie_details()

    def set_movie_data(self, movie):
        print("Setting movie data:", movie)
        self.movie = movie
        self.display_movie_details()

    def display_movie_details(self):
        if hasattr(self, 'movie'):
            print("Displaying movie details for:", self.movie.title)
            details = (
                f"Title: {self.movie.title}\n"
                f"Language: {self.movie.lang}\n"
                f"Genre: {self.movie.genre}\n"
                f"Release Date: {self.movie.rDate}\n"
                f"Duration: {self.movie.duration} mins\n"
                f"Country: {self.movie.country}\n"
                f"Description: {self.movie.description}"
            )
            self.movie_detail_label.config(text=details)
        else:
            print("No movie set to display")


        # 日期和场次的框架
        self.date_session_frame = tk.Frame(self)
        self.date_session_frame.pack(fill="both", expand=True)

        # 日期标签
        self.date_label = tk.Label(self.date_session_frame, text="", font=("Arial", 18))
        self.date_label.pack(side="top", pady=5)

        # 场次的框架
        self.session_frame = tk.Frame(self.date_session_frame)
        self.session_frame.pack(fill="both", expand=True)

        # 左右按钮
        self.left_button = tk.Button(self.date_session_frame, text="<", command=lambda: self.change_date(-1))
        self.left_button.pack(side="left", fill="y")

        self.right_button = tk.Button(self.date_session_frame, text=">", command=lambda: self.change_date(1))
        self.right_button.pack(side="right", fill="y")

        # 返回按钮
        self.back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(SearchResultPage))
        self.back_button.pack(side="bottom", fill="x", pady=10)

    def set_movie_data(self, movie_data):
        # 设置当前电影信息并更新显示
        self.current_movie = movie_data['title']
        self.movies[self.current_movie] = movie_data['sessions']  # 假设 sessions 是一个包含日期和场次信息的列表
        self.change_date(0)  # 初始化显示

    def update_sessions(self, date_sessions):
        # 更新场次信息的实现...
        pass

    def change_date(self, delta):
        # 更改日期的实现...
        pass

    def get_movie_info(self, movie_data):
            # 用于设置电影数据的方法
            # 这里可以更新页面上的标签或其他元素来显示电影数据
            print(movie_data)  # 作为示例，打印出电影数据

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, MainPage, ThirdPage, SearchResultPage, BookingPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky='nsew')
        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Cinema Application")

app = Application()
app.maxsize(800,500)
app.mainloop()


