import tkinter as tk
from tkinter import messagebox

usuarios_pendentes = []

def adicionar_usuario_para_aprovacao(usuario, senha):
    """
    Adiciona um usuário e sua senha à lista de pendentes para aprovação.
    :param usuario: Nome do usuário a ser adicionado.
    :param senha: Senha do usuário a ser adicionado.
    """
    usuarios_pendentes.append((usuario, senha))

def aprovar_usuario():
    """
    Aprova o usuário selecionado na lista de pendentes.
    Remove o usuário da lista de pendentes e exibe uma mensagem de sucesso.
    Se nenhum usuário estiver selecionado, exibe uma mensagem de erro.
    """
    selecionado = lista_usuarios.curselection()
    if selecionado:
        usuario_aprovado = usuarios_pendentes.pop(selecionado[0])
        atualizar_lista_usuarios()
        messagebox.showinfo("Sucesso", f"Usuário '{usuario_aprovado[0]}' aprovado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, selecione um usuário para aprovar.")

def rejeitar_usuario():
    """
    Rejeita o usuário selecionado na lista de pendentes.
    Remove o usuário da lista de pendentes e exibe uma mensagem de sucesso.
    Se nenhum usuário estiver selecionado, exibe uma mensagem de erro.
    """
    selecionado = lista_usuarios.curselection()
    if selecionado:
        usuario_rejeitado = usuarios_pendentes.pop(selecionado[0])
        atualizar_lista_usuarios()
        messagebox.showinfo("Sucesso", f"Usuário '{usuario_rejeitado[0]}' rejeitado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, selecione um usuário para rejeitar.")

def atualizar_lista_usuarios():
    """
    Atualiza a lista de usuários exibida na interface gráfica.
    Remove todos os itens da lista e insere novamente os usuários pendentes.
    """
    lista_usuarios.delete(0, tk.END)
    for usuario in usuarios_pendentes:
        lista_usuarios.insert(tk.END, f"Usuário: {usuario[0]}")

def aprovacao_usuario():
    """
    Cria uma nova janela para aprovação de usuários.
    Configura a interface gráfica com lista de usuários pendentes e botões de aprovar e rejeitar.
    """
    janela = tk.Toplevel()
    janela.title("Aprovação de Usuário")
    
    frame = tk.Frame(janela)
    frame.pack(pady=20, padx=20)
    
    label = tk.Label(frame, text="Usuários Pendentes de Aprovação")
    label.pack()
    
    global lista_usuarios
    lista_usuarios = tk.Listbox(frame, width=50)
    lista_usuarios.pack(pady=10)
    
    button_aprovar = tk.Button(frame, text="Aprovar Usuário", command=aprovar_usuario)
    button_aprovar.pack(pady=10)
    
    button_rejeitar = tk.Button(frame, text="Rejeitar Usuário", command=rejeitar_usuario)
    button_rejeitar.pack(pady=10)
    
    atualizar_lista_usuarios()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() 
    aprovacao_usuario()
    root.mainloop()