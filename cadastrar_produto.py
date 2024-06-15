import tkinter as tk
from tkinter import messagebox, ttk
from gerenciar_fornecedores import fornecedores

produtos = []

def adicionar_produto():
    def validar_quantidade(action, value_if_allowed, text):
        if action == '1':  # Inserção de texto
            if not text.isdigit():
                messagebox.showerror("Erro", "Por favor, insira somente números.")
                return False
        return True
    
    def salvar_produto():
        nome_produto = entry_nome_produto.get()
        quantidade = entry_quantidade.get()
        fornecedor = combobox_fornecedor.get()
        
        if nome_produto and quantidade.isdigit() and fornecedor:
            produtos.append({"nome": nome_produto, "quantidade": int(quantidade), "fornecedor": fornecedor})
            atualizar_lista_produtos()
            messagebox.showinfo("Sucesso", f"Produto '{nome_produto}' adicionado com sucesso!")
            janela_adicionar.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
    
    janela_adicionar = tk.Toplevel()
    janela_adicionar.title("Adicionar Produto")
    janela_adicionar.geometry("400x200")
    
    frame_adicionar = tk.Frame(janela_adicionar)
    frame_adicionar.pack(pady=20, padx=20)
    
    label_nome_produto = tk.Label(frame_adicionar, text="Nome do Produto")
    label_nome_produto.grid(row=0, column=0, pady=5)
    
    entry_nome_produto = tk.Entry(frame_adicionar)
    entry_nome_produto.grid(row=0, column=1, pady=5)
    
    label_quantidade = tk.Label(frame_adicionar, text="Quantidade")
    label_quantidade.grid(row=1, column=0, pady=5)
    
    validate_cmd = (janela_adicionar.register(validar_quantidade), '%d', '%P', '%S')
    entry_quantidade = tk.Entry(frame_adicionar, validate='key', validatecommand=validate_cmd)
    entry_quantidade.grid(row=1, column=1, pady=5)
    
    label_fornecedor = tk.Label(frame_adicionar, text="Fornecedor")
    label_fornecedor.grid(row=2, column=0, pady=5)
    
    combobox_fornecedor = ttk.Combobox(frame_adicionar, values=[f"{f['nome']} - {f['cpf_cnpj']} - {f['data_nascimento']}" for f in fornecedores])
    combobox_fornecedor.grid(row=2, column=1, pady=5)
    
    button_salvar = tk.Button(frame_adicionar, text="Salvar", command=salvar_produto)
    button_salvar.grid(row=3, columnspan=2, pady=10)

def remover_produto():
    selecionado = lista_produtos.curselection()
    if selecionado:
        produtos.pop(selecionado[0])
        atualizar_lista_produtos()
        messagebox.showinfo("Sucesso", "Produto removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, selecione um produto para remover.")

def atualizar_lista_produtos():
    lista_produtos.delete(0, tk.END)
    for produto in produtos:
        lista_produtos.insert(tk.END, f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}, Fornecedor: {produto['fornecedor']}")

def cadastrar_produto():
    janela = tk.Toplevel()
    janela.title("Cadastrar Produto")
    janela.geometry("600x400")
    
    frame = tk.Frame(janela)
    frame.pack(pady=20, padx=20)
    
    label = tk.Label(frame, text="Cadastro de Produto")
    label.pack()
    
    button_adicionar = tk.Button(frame, text="Adicionar Produto", command=adicionar_produto)
    button_adicionar.pack(pady=10)
    
    button_remover = tk.Button(frame, text="Remover Produto", command=remover_produto)
    button_remover.pack(pady=10)
    
    global lista_produtos
    lista_produtos = tk.Listbox(frame, width=80)
    lista_produtos.pack(pady=10)
    
    atualizar_lista_produtos()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    cadastrar_produto()
    root.mainloop()