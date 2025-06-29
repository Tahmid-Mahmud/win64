import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Create app window
app = ctk.CTk()
app.geometry("500x400")
app.title("App with Footer")

# ------- Main content frame --------
main_frame = ctk.CTkFrame(master=app)
main_frame.pack(expand=True, fill="both", padx=20, pady=(20, 40))  # leave bottom space for footer

label = ctk.CTkLabel(main_frame, text="Main Content Here", font=("Arial", 20))
label.pack(pady=20)

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
