import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x150")
app.title("CTkEntry with Icon")

# ---------- Load the icon ----------
# Make sure you have a small icon image like 'key.png'
# Resize it to fit the button

key_icon = ctk.CTkImage(
    light_image=Image.open("key.png"),
    dark_image=Image.open("key.png"),
    size=(20, 20)
)

# ---------- Entry + Icon container ----------
entry_container = ctk.CTkFrame(app, fg_color="transparent")
entry_container.pack(pady=40)

# CTkEntry
entry = ctk.CTkEntry(entry_container, width=200)
entry.pack(side="left", padx=(0, 5))

# Icon Button
def on_icon_click():
    print(22)

icon_button = ctk.CTkButton(
    entry_container,
    image=key_icon,
    text="",
    width=30,
    command=on_icon_click,
    fg_color="transparent",
    hover_color="#2a2a2a"
)
icon_button.pack(side="left")

# Run the app
app.mainloop()
