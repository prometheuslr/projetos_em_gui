import csv
import tkinter as tk
from tkinter import messagebox
import os
def login(u,s):
    l =[]
    senha=[]
    usuario = []
    n = 'contas.csv'
    
    if not os.path.exists(n):
        messagebox.showinfo("Erro", "Nenhum arquivo csv encontrado.\n Registre uma conta")
    else:
        with open(n, 'r') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                l.append(linha)
        quant_l = len(l)
        for i in range(1,quant_l):
            s_l = l[i]
            usuario.append(s_l[0])
            senha.append(s_l[1])           
        user = u
        passworld = s
        senha_correta = None
        tem_usuario = None
        if user in usuario:
            tem_usuario = True
            posicao = usuario.index(user)
            if passworld != senha[posicao]:
                senha_correta = False
            else:
                senha_correta = True
        else:
            tem_usuario = False
            senha_correta = False
        if tem_usuario == None or senha_correta == None:
            messagebox.showinfo("Erro de Login", "Digite Nome de usuário ou senha incorretos!")
        if senha_correta == False or tem_usuario == False :
            messagebox.showinfo("Erro de Login", "Nome de usuário ou senha incorretos!")
        else:messagebox.showinfo("Login Sucesso", "Login realizado com sucesso!")

def register(u,s,c_s):
    nova_linha = []
    n = 'contas.csv'
    if not os.path.exists(n):       
        with open(n,mode='w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['user','passworld'])
    if s != c_s:
        print(s)
        print(c_s)
        messagebox.showinfo("Erro de Registro", "As senhas não são iguais")
    else:
        nova_linha.append(u)
        nova_linha.append(s)
        with open(n, mode='a', newline='\n') as arquivo_csv:
            writer = csv.writer(arquivo_csv)  
            writer.writerow(nova_linha)
        messagebox.showinfo("Registro Sucesso", "Registro realizado com sucesso!")