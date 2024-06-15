import tkinter as tk
from tkinter import messagebox


clientes = []

def obter_clientes():
    return [cliente['nome'] for cliente in clientes]

def validar_numeros(entry_value):
    if entry_value.isdigit() or entry_value == "":
        return True
    else:
        messagebox.showerror("Erro", "Por favor, insira somente números")
        return False

def adicionar_cliente():
    def salvar_cliente():
        nome_cliente = entry_nome.get()
        cpf_cnpj_cliente = entry_cpf_cnpj.get()
        
        if nome_cliente and cpf_cnpj_cliente:
            clientes.append({"id": len(clientes) + 1, "nome": nome_cliente, "cpf_cnpj": cpf_cnpj_cliente})
            messagebox.showinfo("Sucesso", f"Cliente '{nome_cliente}' adicionado com sucesso!")
            janela_adicionar.destroy()
            atualizar_lista_clientes()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    
    janela_adicionar = tk.Toplevel()
    janela_adicionar.title("Adicionar Cliente")
    
    frame_adicionar = tk.Frame(janela_adicionar)
    frame_adicionar.pack(pady=20, padx=20)
    
    label_nome = tk.Label(frame_adicionar, text="Nome")
    label_nome.grid(row=0, column=0, pady=5)
    
    entry_nome = tk.Entry(frame_adicionar)
    entry_nome.grid(row=0, column=1, pady=5)
    
    label_cpf_cnpj = tk.Label(frame_adicionar, text="CPF/CNPJ")
    label_cpf_cnpj.grid(row=1, column=0, pady=5)
    
    entry_cpf_cnpj = tk.Entry(frame_adicionar, validate="key")
    entry_cpf_cnpj.grid(row=1, column=1, pady=5)
    
    validate_command = janela_adicionar.register(validar_numeros)
    entry_cpf_cnpj.config(validatecommand=(validate_command, '%P'))
    
    button_salvar = tk.Button(frame_adicionar, text="Salvar", command=salvar_cliente)
    button_salvar.grid(row=2, columnspan=2, pady=10)

def remover_cliente():
    selecionado = lista_clientes.curselection()
    if selecionado:
        cliente_removido = lista_clientes.get(selecionado)
        cliente_id = int(cliente_removido.split(' ')[0])
        clientes[:] = [cliente for cliente in clientes if cliente['id'] != cliente_id]
        messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
        atualizar_lista_clientes()
    else:
        messagebox.showerror("Erro", "Por favor, selecione um cliente para remover.")

def atualizar_lista_clientes():
    lista_clientes.delete(0, tk.END)
    for cliente in clientes:
        lista_clientes.insert(tk.END, f"{cliente['id']} - Nome: {cliente['nome']}, CPF/CNPJ: {cliente['cpf_cnpj']}")

def gerenciar_clientes():
    janela = tk.Toplevel()
    janela.title("Gerenciar Clientes")
    
    frame = tk.Frame(janela)
    frame.pack(pady=20, padx=20)
    
    label = tk.Label(frame, text="Sistema de Gerenciamento de Clientes")
    label.pack()
    
    button_adicionar = tk.Button(frame, text="Adicionar Cliente", command=adicionar_cliente)
    button_adicionar.pack(pady=10)
    
    button_remover = tk.Button(frame, text="Remover Cliente", command=remover_cliente)
    button_remover.pack(pady=10)
    
    global lista_clientes
    lista_clientes = tk.Listbox(frame, width=50)
    lista_clientes.pack(pady=10)
    
    atualizar_lista_clientes()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    gerenciar_clientes()
    root.mainloop()