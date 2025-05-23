import customtkinter as ctk
from tkinter import messagebox


def signup_screen():
    # Initialize customtkinter
    ctk.set_appearance_mode("Dark") 
    ctk.set_default_color_theme("dark-blue") 

    # App window
    app = ctk.CTk()
    app.geometry("300x350")
    app.title("Login")
    app.resizable(width=False, height=False)
    app.eval('tk::PlaceWindow . center')

    # Widgets
    label_title1 = ctk.CTkLabel(app, text="Cadastro", font=ctk.CTkFont(size=20, weight="bold"))
    label_title1.pack(pady=30)

    entry_name = ctk.CTkEntry(app, placeholder_text="Por Favor, Insira seu Nome",width=172)
    entry_name.pack(pady=10)

    entry_email = ctk.CTkEntry(app, placeholder_text="Por Favor, Insira seu Email",width=172)
    entry_email.pack(pady=10)

    entry_password = ctk.CTkEntry(app, placeholder_text="Por Favor, Insira sua Senha", show="*",width=172)
    entry_password.pack(pady=10)

    button_submit = ctk.CTkButton(app, text="Cadastrar", command=submit(entry_name,entry_email,entry_password),width=172,fg_color="#023020")
    button_submit.pack(pady=10)

    # Run the app
    app.mainloop()
   
# Functions
def submit(entry_name,entry_email,entry_password):
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    messagebox.showinfo("Form Submitted", f"Name:{name}\n Email: {email}\nPassword: {'*' * len(password)}")
