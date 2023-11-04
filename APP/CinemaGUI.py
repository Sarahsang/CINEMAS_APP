import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from controller import GuestController

class FirstPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.guest_controller = GuestController()
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
                messagebox.showinfo("Search Result", "\n".join(result))
                messagebox.showinfo("Test", "This is a message")
            else:
                messagebox.showinfo("Search Result", result)
                messagebox.showinfo("Test", "This is a test message")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

            
    def verify(self):
        uname = self.T1.get()
        pswd = self.T2.get()
        try:
            with open("APP\credential.txt", "r") as f:
                info = f.readlines()
                i = 0
                for e in info:
                    u,p = e.strip().split(",")
                    if u==uname and p==pswd:
                        controller.show_frame(SecondPage)
                        i = 1
                        break
                if i == 0:
                    messagebox.showinfo("Error", "Incorrect Username and Password")
        except:
            messagebox.showinfo("Error", "Incorrect Username and Password") 
            

    def register(self):
        window=tk.Toplevel()
        window.resizable(0,0)
        window.configure(bg="deep sky blue")
        window.title("Register")
        l1 = tk.Label(window, text="Username:", font=("Arial", 15), bg="deep sky blue")
        l1.place(x=10, y=10)
        t1 = tk.Entry(window, width=30, bd=5)
        t1.place(x=200, y=10)

        l2 = tk.Label(window, text="Password:", font=("Arial", 15), bg="deep sky blue")
        l2.place(x=10, y=60)
        t2 = tk.Entry(window, width=30, bd=5, show="*")
        t2.place(x=200, y=60)

        l3 = tk.Label(window, text="Confirm Password:", font=("Arial", 15), bg="deep sky blue")
        l3.place(x=10, y=110)
        t3 = tk.Entry(window, width=30, bd=5, show="*")
        t3.place(x=200, y=110)

        def check():
            if t1.get() != "" or t2.get() != "" or t3.get()!= "":
                if t2.get() == t3.get():
                    with open("APP\credential.txt", "a") as f:
                        f.write(t1.get()+","+t2.get()+"\n")
                        messagebox.showinfo("Welcome", "Successfully Registered")
                else:
                    messagebox.showinfo("Error", "Password did not match")

            else:
                messagebox.showinfo("Error", "Please complete all fields")

        b1 = tk.Button(window, text="Sign In", font=("Arial",15), bg="yellow", command = check)
        b1.place(x=170, y=150)

        window.geometry("479x220")
        window.mainloop()



class SecondPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)

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

class ThirdPage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)

        Label = tk.Label(self, text="Third Page", font=("Arial Bold", 30))
        Label.place(x=230, y=230)

        Button = tk.Button(self, text="Next", font=("Arial",15), command = lambda:controller.show_frame(FirstPage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial",15), command = lambda:controller.show_frame(SecondPage))
        Button.place(x=100, y=450)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky='nsew')
        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Sample Application")

app = Application()
app.maxsize(800,500)
app.mainloop()


