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
                self.controller.frames[SearchResultPage].display_results(result)  # 显示结果
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
            self.controller.show_frame(SecondPage)
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

class SecondPage(tk.Frame):
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

        Label = tk.Label(self, text="Second Page", font=("Arial Bold", 30))
        Label.place(x=230, y=230)

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
                self.controller.frames[SearchResultPage].display_results(result)  # 显示结果
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

        Button = tk.Button(self, text="Back", font=("Arial",15), command = lambda:controller.show_frame(SecondPage))
        Button.place(x=100, y=450)

class SearchResultPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        Button = tk.Button(self, text="Back", font=("Arial",13), command = lambda:controller.show_frame(SecondPage))
        Button.place(x=710, y=37)
        
        self.title_label = tk.Label(self, text="Movie Search Results", font=("Arial", 18))
        self.title_label.pack(side="top", fill="x", pady=10)
        
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side="right", fill="y")
        
        self.results_listbox = tk.Listbox(self, height=20, width=50, yscrollcommand=self.scrollbar.set, font=('Arial', 12))
        self.results_listbox.pack(pady=(20, 0), padx=20, fill='both', expand=True)
        self.scrollbar.config(command=self.results_listbox.yview)

    def display_results(self, results):
        self.results_listbox.delete(0, tk.END)  # 清空结果列表
        for result in results:
            self.results_listbox.insert(tk.END, result)  # 添加结果到列表


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage, SearchResultPage):
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


