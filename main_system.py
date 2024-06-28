import tkinter as tk
from cadastrar_produto import cadastrar_produto
from atualizar_estoque import atualizar_estoque
from gerar_relatorio import gerar_relatorio
from gerenciar_fornecedores import gerenciar_fornecedores
from gerenciar_pedidos import gerenciar_pedidos
from aprovacao_usuario import aprovacao_usuario
from gerenciar_clientes import gerenciar_clientes

def abrir_sistema(login_window):
    """
    Abre a janela principal do sistema de gerenciamento de estoque e fecha a janela de login.
    Configura a interface gráfica com as funcionalidades disponíveis.
    """
    login_window.destroy()
    
    sistema = tk.Tk()
    sistema.title("Sistema de Gerenciamento de Estoque")
    sistema.geometry("500x500")  
    
    label_bem_vindo = tk.Label(sistema, text="Bem Vindo ao Sistema!", font=("Helvetica", 30), fg="orange")
    label_bem_vindo.pack(pady=(20, 10))
    
    label_funcionalidades = tk.Label(sistema, text="Aqui Estão Algumas Funcionalidades Que Você Pode Usufruir!", font=("Helvetica", 14), fg="orange")
    label_funcionalidades.pack(pady=(0, 20))
    
    frame = tk.Frame(sistema)
    frame.pack(pady=20, padx=20)
    
    buttons = [
        ("Cadastrar Produto", cadastrar_produto),
        ("Correção De Estoque", atualizar_estoque),
        ("Gerar Relatório", gerar_relatorio),
        ("Gerenciar Fornecedores", gerenciar_fornecedores),
        ("Gerenciar Pedidos", gerenciar_pedidos),
        ("Gerenciar Clientes", gerenciar_clientes),
        ("Aprovação de Usuário", aprovacao_usuario),
    ]
    
    for i, (text, command) in enumerate(buttons):
        button = tk.Button(frame, text=text, command=command)
        button.grid(row=i, column=0, padx=10, pady=10)
    
    sistema.mainloop()