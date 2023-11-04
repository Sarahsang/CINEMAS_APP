from controller import GuestController
import tkinter as tk
from tkinter import Tk, Label, Button, Entry, Listbox, Scrollbar, Frame, Toplevel, messagebox

class MovieSearchApp:
    def __init__(self, root, guest_controller):
        self.guest_controller = guest_controller
        self.root = root
        self.root.title("Movie Search")
        
        self.search_entry = tk.Entry(root)
        self.search_entry.pack()

        self.search_button = tk.Button(root, text="Search", command=self.search_movies)
        self.search_button.pack()

    def search_movies(self):
        search_term = self.search_entry.get()

        if search_term:
            result = self.guest_controller.view_movie_details(search_term)
            if isinstance(result, list):
                messagebox.showinfo("Search Result", "\n".join(result))
            else:
                messagebox.showinfo("Search Result", result)
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def create_registration_form(self):
        # Create a new window for the registration form
        self.registration_window = tk.Toplevel(self.root)
        self.registration_window.title("Register")
        
        # Create and pack the registration form elements
        tk.Label(self.registration_window, text="Username").pack()
        self.username_entry = tk.Entry(self.registration_window)
        self.username_entry.pack()

        tk.Label(self.registration_window, text="Password").pack()
        self.password_entry = tk.Entry(self.registration_window, show="*")
        self.password_entry.pack()

        tk.Label(self.registration_window, text="Name").pack()
        self.name_entry = tk.Entry(self.registration_window)
        self.name_entry.pack()

        tk.Label(self.registration_window, text="Address").pack()
        self.address_entry = tk.Entry(self.registration_window)
        self.address_entry.pack()

        tk.Label(self.registration_window, text="Email").pack()
        self.email_entry = tk.Entry(self.registration_window)
        self.email_entry.pack()

        tk.Label(self.registration_window, text="Phone").pack()
        self.phone_entry = tk.Entry(self.registration_window)
        self.phone_entry.pack()

        # Create and pack the submit button
        submit_button = tk.Button(self.registration_window, text="Register", command=self.submit_registration)
        submit_button.pack()

    def submit_registration(self):
        # Get the values from the entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()
        name = self.name_entry.get()
        address = self.address_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        
        # Call the register_guest method from the controller
        registration_result = self.guest_controller.register_guest(username, password, name, address, email, phone)
        
        # Show the result in a message box
        messagebox.showinfo("Registration Result", registration_result)
        
        # Close the registration window if registration was successful
        if registration_result == "Registration successful!":
            self.registration_window.destroy()
            
            
if __name__ == "__main__":
    root = Tk()
    app = MovieSearchApp(root, GuestController())
    root.mainloop()