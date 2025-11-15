import tkinter as tk
from tkinter import messagebox
import re

class ModernApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Authentication System")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f172a")
        
        self.user_data = {}
        self.show_registration_page()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def create_gradient_frame(self, parent):
        frame = tk.Frame(parent, bg="#1e293b")
        return frame
    
    def show_registration_page(self):
        self.clear_window()
        
        # Header (Fixed at top)
        header_frame = tk.Frame(self.root, bg="#0f172a")
        header_frame.pack(side="top", fill="x", padx=40, pady=(30, 10))
        
        header = tk.Label(header_frame, text="Create Account", font=("Helvetica", 32, "bold"), 
                         fg="#f1f5f9", bg="#0f172a")
        header.pack()
        
        subtitle = tk.Label(header_frame, text="Join us today! Please fill in your details", 
                           font=("Helvetica", 11), fg="#94a3b8", bg="#0f172a")
        subtitle.pack(pady=(5, 0))
        
        # Button frame (Fixed at bottom)
        button_frame = tk.Frame(self.root, bg="#0f172a")
        button_frame.pack(side="bottom", fill="x", padx=40, pady=30)
        
        register_btn = tk.Button(button_frame, text="Register", font=("Helvetica", 14, "bold"),
                                bg="#3b82f6", fg="white", bd=0, padx=60, pady=14,
                                cursor="hand2", activebackground="#2563eb",
                                command=self.register_user)
        register_btn.pack()
        
        register_btn.bind("<Enter>", lambda e: register_btn.config(bg="#2563eb"))
        register_btn.bind("<Leave>", lambda e: register_btn.config(bg="#3b82f6"))
        
        # Scrollable middle section
        scroll_container = tk.Frame(self.root, bg="#0f172a")
        scroll_container.pack(side="top", fill="both", expand=True, padx=40, pady=10)
        
        canvas = tk.Canvas(scroll_container, bg="#0f172a", highlightthickness=0)
        scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=canvas.yview, 
                                bg="#1e293b", troughcolor="#0f172a", width=12)
        scrollable_frame = tk.Frame(canvas, bg="#0f172a")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=380)
        canvas.configure(yscrollcommand=scrollbar.set)
        
        def on_canvas_configure(event):
            canvas.itemconfig(canvas_window, width=event.width)
        canvas.bind("<Configure>", on_canvas_configure)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def bind_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        def unbind_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")
        
        canvas.bind("<Enter>", bind_mousewheel)
        canvas.bind("<Leave>", unbind_mousewheel)
        
        # Input frame inside scrollable area
        input_frame = self.create_gradient_frame(scrollable_frame)
        input_frame.pack(fill="both", expand=True, pady=20, padx=10)
        
        # Full Name
        self.create_input_field(input_frame, "Full Name", 0)
        self.full_name_entry = self.create_entry(input_frame, 1)
        
        # Email
        self.create_input_field(input_frame, "Email Address", 2)
        self.email_entry = self.create_entry(input_frame, 3)
        
        # Phone
        self.create_input_field(input_frame, "Phone Number", 4)
        self.phone_entry = self.create_entry(input_frame, 5)
        
        # Address
        self.create_input_field(input_frame, "Address", 6)
        self.address_entry = self.create_entry(input_frame, 7)
        
        # Password
        self.create_input_field(input_frame, "Password", 8)
        self.password_entry = self.create_entry(input_frame, 9, show="•")
        
        # Confirm Password
        self.create_input_field(input_frame, "Confirm Password", 10)
        self.confirm_password_entry = self.create_entry(input_frame, 11, show="•")
        
        # Add some bottom padding
        tk.Label(input_frame, text="", bg="#1e293b").grid(row=12, column=0, pady=10)
    
    def create_input_field(self, parent, text, row):
        label = tk.Label(parent, text=text, font=("Helvetica", 11, "bold"),
                        fg="#f1f5f9", bg="#1e293b", anchor="w")
        label.grid(row=row, column=0, sticky="w", padx=30, pady=(15, 5))
    
    def create_entry(self, parent, row, show=None):
        entry = tk.Entry(parent, font=("Helvetica", 12), bg="#334155", fg="white",
                        relief="flat", bd=0, insertbackground="white", show=show)
        entry.grid(row=row, column=0, sticky="ew", padx=30, pady=(0, 5), ipady=10)
        parent.grid_columnconfigure(0, weight=1)
        return entry
    
    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)
    
    def register_user(self):
        full_name = self.full_name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        # Validation
        if not all([full_name, email, phone, address, password, confirm_password]):
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address!")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters!")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        # Store user data
        self.user_data = {
            "full_name": full_name,
            "email": email.lower(),
            "phone": phone,
            "address": address,
            "password": password
        }
        
        messagebox.showinfo("Success", "✅ Registration successful!\nPlease login to continue.")
        self.show_login_page()
    
    def show_login_page(self):
        self.clear_window()
        
        # Main container
        container = tk.Frame(self.root, bg="#0f172a")
        container.pack(expand=True, fill="both", padx=40, pady=80)
        
        # Header
        header = tk.Label(container, text="Welcome Back", font=("Helvetica", 36, "bold"),
                         fg="#f1f5f9", bg="#0f172a")
        header.pack(pady=(0, 10))
        
        subtitle = tk.Label(container, text="Login to your account",
                           font=("Helvetica", 12), fg="#94a3b8", bg="#0f172a")
        subtitle.pack(pady=(0, 40))
        
        # Input frame
        input_frame = self.create_gradient_frame(container)
        input_frame.pack(fill="both", padx=20, pady=20)
        
        # Email
        self.create_input_field(input_frame, "Email Address", 0)
        self.login_email_entry = self.create_entry(input_frame, 1)
        
        # Password
        self.create_input_field(input_frame, "Password", 2)
        self.login_password_entry = self.create_entry(input_frame, 3, show="•")
        
        # Login Button
        login_btn = tk.Button(container, text="Login", font=("Helvetica", 14, "bold"),
                             bg="#10b981", fg="white", bd=0, padx=40, pady=12,
                             cursor="hand2", activebackground="#059669",
                             command=self.login_user)
        login_btn.pack(pady=(30, 10))
        
        # Hover effect
        login_btn.bind("<Enter>", lambda e: login_btn.config(bg="#059669"))
        login_btn.bind("<Leave>", lambda e: login_btn.config(bg="#10b981"))
        
        # Back to Register
        back_btn = tk.Button(container, text="← Back to Register", font=("Helvetica", 10),
                            fg="#94a3b8", bg="#0f172a", bd=0, cursor="hand2",
                            activeforeground="#f1f5f9", activebackground="#0f172a",
                            command=self.show_registration_page)
        back_btn.pack(pady=10)
    
    def login_user(self):
        email = self.login_email_entry.get().strip().lower()
        password = self.login_password_entry.get()
        
        if not self.user_data:
            messagebox.showerror("Error", "No registered user found! Please register first.")
            return
        
        if email == self.user_data["email"] and password == self.user_data["password"]:
            messagebox.showinfo("Success", f"✅ Login Successful!\n\nWelcome {self.user_data['full_name']}!")
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "❌ Login Failed!\nInvalid email or password.")
    
    def show_dashboard(self):
        self.clear_window()
        
        container = tk.Frame(self.root, bg="#0f172a")
        container.pack(expand=True, fill="both", padx=40, pady=40)
        
        # Welcome message
        welcome = tk.Label(container, text=f"Welcome, {self.user_data['full_name']}!",
                          font=("Helvetica", 28, "bold"), fg="#f1f5f9", bg="#0f172a")
        welcome.pack(pady=(20, 30))
        
        # User info frame
        info_frame = self.create_gradient_frame(container)
        info_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Display user information
        info_labels = [
            ("📧 Email:", self.user_data['email']),
            ("📱 Phone:", self.user_data['phone']),
            ("📍 Address:", self.user_data['address'])
        ]
        
        for i, (label_text, value) in enumerate(info_labels):
            label = tk.Label(info_frame, text=label_text, font=("Helvetica", 12, "bold"),
                           fg="#94a3b8", bg="#1e293b", anchor="w")
            label.grid(row=i, column=0, sticky="w", padx=30, pady=15)
            
            value_label = tk.Label(info_frame, text=value, font=("Helvetica", 12),
                                  fg="#f1f5f9", bg="#1e293b", anchor="w")
            value_label.grid(row=i, column=1, sticky="w", padx=10, pady=15)
        
        # Logout button
        logout_btn = tk.Button(container, text="Logout", font=("Helvetica", 12, "bold"),
                              bg="#ef4444", fg="white", bd=0, padx=30, pady=10,
                              cursor="hand2", activebackground="#dc2626",
                              command=self.show_login_page)
        logout_btn.pack(pady=(30, 10))
        
        logout_btn.bind("<Enter>", lambda e: logout_btn.config(bg="#dc2626"))
        logout_btn.bind("<Leave>", lambda e: logout_btn.config(bg="#ef4444"))

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernApp(root)
    root.mainloop()