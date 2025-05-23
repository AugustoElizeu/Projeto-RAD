import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
    
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("600x500")
app.title("Agenda")
app.resizable(width=False, height=False)
app.eval('tk::PlaceWindow . center')

# Top Frame
top_frame = ctk.CTkFrame(app)
top_frame.pack(fill="x", pady=10)

label_welcome = ctk.CTkLabel(top_frame, text="Bem-vindo, ming!", font=ctk.CTkFont(size=14, weight="bold"))
label_welcome.pack(side="left", padx=10)

image = Image.open("exit.png")

exit_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(20, 20))

btn_exit = ctk.CTkButton(top_frame, text="", image=exit_icon, fg_color="white", width=5)
btn_exit.pack(side="right", padx=5)

btn_edit = ctk.CTkButton(top_frame, text="Editar Perfil", fg_color="#1B03A3")
btn_edit.pack(side="right", padx=5)


# Container principal
container_frame = ctk.CTkFrame(app)
container_frame.pack(pady=10)

# Form Frame
form_frame = ctk.CTkFrame(container_frame)
form_frame.grid(row=0, column=0, padx=10)

# Data
label_data = ctk.CTkLabel(form_frame, text="Data (DD-MM-YYYY):")
label_data.grid(row=0, column=0, sticky="w", pady=5, padx=5)
entry_data = ctk.CTkEntry(form_frame, width=200)
entry_data.grid(row=0, column=1, pady=5, padx=5)

# Horário
label_horario = ctk.CTkLabel(form_frame, text="Horário (HH:MM):")
label_horario.grid(row=1, column=0, sticky="w", pady=5, padx=5)
entry_horario = ctk.CTkEntry(form_frame, width=200)
entry_horario.grid(row=1, column=1, pady=5, padx=5)

# Aluno
label_prof = ctk.CTkLabel(form_frame, text="Nome do Aluno:")
label_prof.grid(row=2, column=0, sticky="w", pady=5, padx=5)
entry_prof = ctk.CTkEntry(form_frame, width=200)
entry_prof.grid(row=2, column=1, pady=5, padx=5)

# Buttons Frame
btn_frame = ctk.CTkFrame(container_frame)
btn_frame.grid(row=0, column=1, padx=10)

btn_salvar = ctk.CTkButton(btn_frame, text="Salvar", fg_color="green")
btn_salvar.pack(pady=5)

btn_atualizar = ctk.CTkButton(btn_frame, text="Atualizar", fg_color="yellow", text_color="black")
btn_atualizar.pack(pady=5)

btn_deletar = ctk.CTkButton(btn_frame, text="Deletar", fg_color="red")
btn_deletar.pack(pady=5)

# Tabela
table_frame = ctk.CTkFrame(app)
table_frame.pack(pady=10, fill="both", expand=True)

columns = ("Data", "Horário", "Aluno")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(fill="both", expand=True)

app.mainloop()