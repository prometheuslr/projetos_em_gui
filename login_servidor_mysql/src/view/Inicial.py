import customtkinter
import re
import tkinter as tk
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("750x650")
custom_font = ("ROboto", 24 )

    

def inicial_app():

    def mostra_tela_lg_server():
        frame_lg_server.pack()
        frame_login.pack_forget()
        frame_registra_usuario.pack_forget()
    def mostra_tela_login():
        frame_login.pack()
        frame_registra_usuario.pack_forget()
        frame_lg_server.pack_forget()

    def mostra_tela_registro():
        frame_login.pack_forget()
        frame_lg_server.pack_forget()
        frame_registra_usuario.pack()

    
    def is_valid_email(email):
    #validar o formato do email
        pattern = r'^\S+@\S+\.\S+$'
        return re.match(pattern, email) is not None

    def logar_conta():
        email_lg = entry_email_login.get()
        if not is_valid_email(email_lg):
            messagebox.showinfo("Erro", "Email invalido")
            entry_email_login.delete(0, 'end')

    #Frame login serve
    frame_lg_server = customtkinter.CTkFrame(master=root)
    frame_lg_server.pack(pady=100, padx=60, fill="both", expand=True)
    
    #Frame login
    frame_login = customtkinter.CTkFrame(master=root)
    frame_login.pack(pady=100,padx=60, fill="both", expand=True)
    
    #Frame registro
    frame_registra_usuario = customtkinter.CTkFrame(master=root)
    frame_registra_usuario.pack(pady=100, padx=60, fill="both", expand = True)
    frame_registra_usuario.pack_forget()
    
    #Login server label
    label_lg_server = customtkinter.CTkLabel(master=frame_lg_server, text="Login de servidor", font=custom_font)
    label_lg_server.pack(pady=12,padx=10)

    #login Label
    label_login = customtkinter.CTkLabel(master=frame_login,text="Login", font=custom_font)
    label_login.pack(pady=12, padx=10)

    #Registro Label
    label_registro = customtkinter.CTkLabel(master=frame_registra_usuario, text="Cadastra conta", font=custom_font)
    label_registro.pack(pady=12, padx=10)

    #Login server Entrys
    entry_server_host = customtkinter.CTkEntry(master=frame_lg_server, placeholder_text="Host")
    entry_server_host.pack(pady=12,padx=10)
    entry_server_user = customtkinter.CTkEntry(master=frame_lg_server, placeholder_text="User")
    entry_server_user.pack(pady=12, padx=10)
    entry_server_password = customtkinter.CTkEntry(master=frame_lg_server, placeholder_text="Password", show="*")
    entry_server_password.pack(pady=12, padx=10)
    entry_server_database = customtkinter.CTkEntry(master=frame_lg_server, placeholder_text="Data Base")
    entry_server_database.pack(pady=12, padx=10)

    #login Entrys
    entry_email_login = customtkinter.CTkEntry(master=frame_login, placeholder_text="Email")
    entry_email_login.pack(pady=12, padx=10)
    entry_senha_login = customtkinter.CTkEntry(master=frame_login, placeholder_text="Senha", show="*")
    entry_senha_login.pack(pady=12,padx=10)

    #Registro Entrys
    entry_nome_reg = customtkinter.CTkEntry(master=frame_registra_usuario, placeholder_text="Nome")
    entry_nome_reg.pack(pady=12, padx=10)
    entry_email_reg = customtkinter.CTkEntry(master=frame_registra_usuario, placeholder_text="Email")
    entry_email_reg.pack(pady=12,padx=10)
    entr_celular_reg = customtkinter.CTkEntry(master=frame_registra_usuario, placeholder_text="Celular")
    entr_celular_reg.pack(pady = 12, padx = 10)
    entry_senha_reg = customtkinter.CTkEntry(master=frame_registra_usuario, placeholder_text="Senha", show="*")
    entry_senha_reg.pack(pady=12, padx=10)

    #Botão de lg server
    button_lg_server = customtkinter.CTkButton(master=frame_lg_server, text="Entrar", command=mostra_tela_login)
    button_lg_server.pack(pady=12, padx=10)
    #Botões de login e cadastro
    submit_button = customtkinter.CTkButton(master=frame_login, text="Entrar", command=logar_conta)
    submit_button.pack(pady=12, padx=10)

    butto_registra = customtkinter.CTkButton(master=frame_login,text="Registra", hover_color="red", command=mostra_tela_registro)
    butto_registra.pack(pady=12, padx=10)

    #botões do para criar a conta e voltar para o login
    button_criar_conta = customtkinter.CTkButton(master=frame_registra_usuario,text="Criar conta", hover_color="green")
    button_criar_conta.pack(pady=12, padx=10)

    button_voltar = customtkinter.CTkButton(master=frame_registra_usuario, text="Voltar", hover_color="red", command=mostra_tela_login)
    button_voltar.pack(pady = 12, padx=10)
    
    




    

    
    