import tkinter as tk
from tkinter import messagebox, simpledialog
from user import authenticate_user
from patient import PatientManager
from note import NoteManager
from stats import StatsGenerator
from utils import log_usage

class HospitalUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hospital Clinical Data Warehouse")
        self.patient_manager = PatientManager()
        self.note_manager = NoteManager()
        self.stats_generator = StatsGenerator()
        self.user = None

    def run(self):
        self.show_login()
        self.root.mainloop()

    def show_login(self):
        self.clear_window()
        tk.Label(self.root, text="Username").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        password_entry = tk.Entry(self.root, show='*')
        password_entry.pack()

        def attempt_login():
            user = authenticate_user(username_entry.get(), password_entry.get())
            if user:
                self.user = user
                log_usage(user.username, user.role, "Login")
                self.show_menu()
            else:
                log_usage(username_entry.get(), "Unknown", "Failed login")
                messagebox.showerror("Login Failed", "Invalid credentials.")

        tk.Button(self.root, text="Login", command=attempt_login).pack()

    def show_menu(self):
        self.clear_window()
        tk.Label(self.root, text=f"Welcome {self.user.username}! Role: {self.user.role}").pack()

        role = self.user.role
        actions = {
            "admin": ["Count Visits", "Exit"],
            "management": ["Generate Statistics", "Exit"],
            "nurse": ["Retrieve Patient", "Add Patient", "Remove Patient", "Count Visits", "View Note", "Exit"],
            "clinician": ["Retrieve Patient", "Add Patient", "Remove Patient", "Count Visits", "View Note", "Exit"]
        }

        for action in actions[role]:
            tk.Button(self.root, text=action, command=lambda a=action: self.handle_action(a)).pack(pady=5)

    def handle_action(self, action):
        role = self.user.role
        log_usage(self.user.username, role, action)

        if action == "Add Patient":
            self.patient_manager.add_patient()
        elif action == "Remove Patient":
            self.patient_manager.remove_patient()
        elif action == "Retrieve Patient":
            self.patient_manager.retrieve_patient()
        elif action == "Count Visits":
            date = simpledialog.askstring("Input", "Enter date (YYYY-MM-DD):")
            if date:
                self.patient_manager.count_visits(date)
        elif action == "View Note":
            date = simpledialog.askstring("Input", "Enter date (YYYY-MM-DD):")
            if date:
                self.note_manager.view_notes(date)
        elif action == "Generate Statistics":
            self.stats_generator.generate_all_stats()
            messagebox.showinfo("Done", "Statistics generated and saved.")
        elif action == "Exit":
            self.root.destroy()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
