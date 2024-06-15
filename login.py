import tkinter as tk
from tkinter import messagebox
from main_system import abrir_sistema
from aprovacao_usuario import adicionar_usuario_para_aprovacao

usuarios_pendentes = []

def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuario == "admin" and senha == "admin123":
        abrir_sistema(login_window)
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos")

def registrar_usuario():
    def salvar_registro():
        novo_usuario = entry_novo_usuario.get()
        nova_senha = entry_nova_senha.get()
        
        if novo_usuario and nova_senha:
            adicionar_usuario_para_aprovacao(novo_usuario, nova_senha)
            messagebox.showinfo("Sucesso", f"Usuário '{novo_usuario}' registrado com sucesso! Aguarde aprovação do administrador.")
            janela_registrar.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    
    janela_registrar = tk.Toplevel()
    janela_registrar.title("Registrar Usuário")
    janela_registrar.geometry("400x200")
    
    frame_registrar = tk.Frame(janela_registrar)
    frame_registrar.pack(expand=True, fill=tk.BOTH, pady=20, padx=20)
    
    label_novo_usuario = tk.Label(frame_registrar, text="Novo Usuário")
    label_novo_usuario.grid(row=0, column=0, pady=5, sticky="e")
    
    entry_novo_usuario = tk.Entry(frame_registrar)
    entry_novo_usuario.grid(row=0, column=1, pady=5, sticky="we")
    
    label_nova_senha = tk.Label(frame_registrar, text="Nova Senha")
    label_nova_senha.grid(row=1, column=0, pady=5, sticky="e")
    
    entry_nova_senha = tk.Entry(frame_registrar, show="*")
    entry_nova_senha.grid(row=1, column=1, pady=5, sticky="we")
    
    button_salvar_registro = tk.Button(frame_registrar, text="Salvar Registro", command=salvar_registro)
    button_salvar_registro.grid(row=2, columnspan=2, pady=10)

    frame_registrar.columnconfigure(1, weight=1)

login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("500x200")

frame = tk.Frame(login_window)
frame.pack(expand=True, fill=tk.BOTH, pady=20, padx=20)

label_usuario = tk.Label(frame, text="Usuário")
label_usuario.grid(row=0, column=0, pady=5, sticky="e")

entry_usuario = tk.Entry(frame)
entry_usuario.grid(row=0, column=1, pady=5, sticky="we")

label_senha = tk.Label(frame, text="Senha")
label_senha.grid(row=1, column=0, pady=5, sticky="e")

entry_senha = tk.Entry(frame, show="*")
entry_senha.grid(row=1, column=1, pady=5, sticky="we")

button_login = tk.Button(frame, text="Login", command=fazer_login)
button_login.grid(row=2, columnspan=2, pady=10)

button_registrar = tk.Button(frame, text="Registrar", command=registrar_usuario)
button_registrar.grid(row=3, columnspan=2, pady=10)

frame.columnconfigure(1, weight=1)

login_window.mainloop()