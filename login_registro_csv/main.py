import customtkinter
from Def import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x400")

def lg():
    login(entry1.get(), entry2.get())
    entry1.delete(0,'end')
    entry2.delete(0,'end')

def rg():
    register(entry_user_registro.get(),entry_senha_registro.get(),entry_conferi_senha_registro.get())
    entry_user_registro.delete(0,'end')
    entry_senha_registro.delete(0,'end')
    entry_conferi_senha_registro.delete(0,'end')

def mostrar_tela_login():
    frame_login.pack()
    frame_registro.pack_forget()

def mostrar_tela_registro():
    frame_login.pack_forget()
    frame_registro.pack()

frame_login = customtkinter.CTkFrame(master=root)
frame_login.pack(pady=20, padx=60, fill="both", expand=True)

custom_font = ("Roboto", 24)

frame_registro = customtkinter.CTkFrame(master=root)
frame_registro.pack(pady=20, padx=60, fill="both", expand=True)
frame_registro.pack_forget()  

label_login = customtkinter.CTkLabel(master=frame_login, text="Login System", font=custom_font)
label_login.pack(pady=12, padx=10)

label_registro = customtkinter.CTkLabel(master=frame_registro, text="Registro", font=custom_font)
label_registro.pack(pady=12, padx=10)

entry_user_registro = customtkinter.CTkEntry(master=frame_registro, placeholder_text="Nome do Usuario")
entry_user_registro.pack(pady=12, padx=10)

entry_senha_registro = customtkinter.CTkEntry(master=frame_registro, placeholder_text="Digite a senha", show="*")
entry_senha_registro.pack(pady=12, padx=10)

entry_conferi_senha_registro = customtkinter.CTkEntry(master=frame_registro, placeholder_text="Confirme a senha", show="*")
entry_conferi_senha_registro.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame_login, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame_login, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)


button_login = customtkinter.CTkButton(master=frame_login, text="Login", command=lg)
button_login.pack(pady=12, padx=10)

button_registro = customtkinter.CTkButton(master=frame_login, text="Cadastrar", hover_color="red", command=mostrar_tela_registro)
button_registro.pack(pady=12, padx=10)

button_voltar = customtkinter.CTkButton(master=frame_registro, text="Voltar", hover_color="red", command=mostrar_tela_login)
button_voltar.pack(pady=12, padx=10)

button_cadastrar = customtkinter.CTkButton(master=frame_registro, text="Cadastrar", hover_color="red", command=rg)
button_cadastrar.pack(pady=12, padx=10)

mostrar_tela_login()

root.mainloop()

