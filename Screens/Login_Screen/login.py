import customtkinter as ctk
from tkinter import messagebox
from Screens.Signup_Screen import Signup as sign


def login_screen():
    
    def login_screen_switch():
        app.destroy()
    # Initialize customtkinter
    ctk.set_appearance_mode("Light")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (default), "green", "dark-blue"

    # App window
    app = ctk.CTk()
    app.geometry("300x400")
    app.title("Login")
    app.resizable(width=False, height=False)
    app.eval('tk::PlaceWindow . center')

    # Widgets
    label_title = ctk.CTkLabel(app, text="Bem-Vindo", font=ctk.CTkFont(size=20, weight="bold"))
    label_title.pack(pady=40)

    entry_email = ctk.CTkEntry(app, placeholder_text="Por Favor, Insira seu Email",width=172)
    entry_email.pack(pady=10)

    entry_password = ctk.CTkEntry(app, placeholder_text="Por Favor, Insira sua Senha", show="*",width=172)
    entry_password.pack(pady=10)

    button_submit = ctk.CTkButton(app, text="Entrar",  command=lambda: submit(entry_email, entry_password),width=172)
    button_submit.pack(pady=10)

    button_clear = ctk.CTkButton(app, text="Não possui cadastro?", command=lambda: (login_screen_switch(),signUp_button()), fg_color="#333333",width=172)
    button_clear.pack(pady=5)

    # Run the app
    app.mainloop()

# Functions
def submit(entry_email,entry_password):
    email = entry_email.get()
    password = entry_password.get()
    if email != "" or password != "":
        messagebox.showinfo("Form Submitted", f"Email: {email}\nPassword: {'*' * len(password)}")
    else:
        messagebox.showinfo("Error", f"Digite uma login, porfavor")

def signUp_button():
    sign.signup_screen()

