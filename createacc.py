import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Create app window
app = ctk.CTk()
app.geometry("400x300")
app.title("App with Footer")

# ------- Function to open subwindow --------
def open_subwindow():
    subwindow = ctk.CTkToplevel(app)
    subwindow.geometry("300x300")
    subwindow.title("Register User")

    subwindow.attributes("-topmost", True)  # Keep it above
    subwindow.focus_force()                 # Focus on popup
    subwindow.grab_set()                    # Optional: modal

    # Heading
    heading_label = ctk.CTkLabel(subwindow, text="Create New Account", font=("Arial", 18, "bold"))
    heading_label.pack(pady=(15, 10))

    # Username
    username_entry = ctk.CTkEntry(subwindow, placeholder_text="Username")
    username_entry.pack(pady=5)

    # Password
    password_entry = ctk.CTkEntry(subwindow, placeholder_text="Password", show="*")
    password_entry.pack(pady=5)

    # Confirm Password
    confirm_password_entry = ctk.CTkEntry(subwindow, placeholder_text="Confirm Password", show="*")
    confirm_password_entry.pack(pady=5)


    # Save Button
    def save_user():
        print(22)  # As requested

    save_button = ctk.CTkButton(subwindow, text="Save", command=save_user)
    save_button.pack(pady=20)

# ------- Main content frame --------
main_frame = ctk.CTkFrame(master=app)
main_frame.pack(expand=True, fill="both", padx=20, pady=(20, 40))  # leave bottom space for footer

main_button = ctk.CTkButton(main_frame, text="Main Content Here", font=("Arial", 20))
main_button.pack(pady=10)

# Add button to open subwindow
open_window_button = ctk.CTkButton(main_frame, text="Register User", command=open_subwindow)
open_window_button.pack(pady=10)

# ------- Footer Frame --------
footer_frame = ctk.CTkFrame(master=app, fg_color="transparent")
footer_frame.pack(side="bottom", fill="x", pady=10)

# Horizontal line (separator)
separator = ctk.CTkFrame(footer_frame, height=2, fg_color="#444444")
separator.pack(fill="x", pady=(10, 5))

# Copyright label
copyright_label = ctk.CTkLabel(
    footer_frame,
    text="© 2025 MyCompany. All rights reserved.",
    font=("Arial", 12),
    text_color="#888888"
)
copyright_label.pack()

# Start app
app.mainloop()
