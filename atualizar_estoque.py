import tkinter as tk
from tkinter import messagebox
from cadastrar_produto import produtos

correcoes_estoque = []

def validar_numeros(entry_value):
    if entry_value.isdigit() or entry_value == "":
        return True
    else:
        messagebox.showerror("Erro", "Por favor, insira somente números")
        return False

def atualizar_quantidade():
    selecionado = lista_produtos.curselection()
    if selecionado:
        produto_selecionado = produtos[selecionado[0]]
        
        def salvar_quantidade():
            nova_quantidade = entry_nova_quantidade.get()
            motivo_correcao = entry_motivo.get()
            
            if nova_quantidade.isdigit() and motivo_correcao:
                correcoes_estoque.append({
                    "produto": produto_selecionado["nome"],
                    "quantidade_anterior": produto_selecionado["quantidade"],
                    "nova_quantidade": int(nova_quantidade),
                    "motivo": motivo_correcao
                })
                produto_selecionado["quantidade"] = int(nova_quantidade)
                atualizar_lista_produtos()
                messagebox.showinfo("Sucesso", f"Quantidade do produto '{produto_selecionado['nome']}' atualizada com sucesso!")
                janela_atualizar.destroy()
            else:
                messagebox.showerror("Erro", "Por favor, insira um valor numérico para a quantidade e o motivo da correção.")
        
        janela_atualizar = tk.Toplevel()
        janela_atualizar.title("Atualizar Quantidade")
        
        frame_atualizar = tk.Frame(janela_atualizar)
        frame_atualizar.pack(pady=20, padx=20)
        
        label_produto = tk.Label(frame_atualizar, text=f"Produto: {produto_selecionado['nome']}")
        label_produto.grid(row=0, column=0, pady=5)
        
        label_nova_quantidade = tk.Label(frame_atualizar, text="Nova Quantidade")
        label_nova_quantidade.grid(row=1, column=0, pady=5)
        
        entry_nova_quantidade = tk.Entry(frame_atualizar, validate="key")
        entry_nova_quantidade.grid(row=1, column=1, pady=5)
        
        label_motivo = tk.Label(frame_atualizar, text="Motivo da Correção")
        label_motivo.grid(row=2, column=0, pady=5)
        
        entry_motivo = tk.Entry(frame_atualizar)
        entry_motivo.grid(row=2, column=1, pady=5)
        
        validate_command = janela_atualizar.register(validar_numeros)
        entry_nova_quantidade.config(validatecommand=(validate_command, '%P'))
        
        button_salvar = tk.Button(frame_atualizar, text="Salvar", command=salvar_quantidade)
        button_salvar.grid(row=3, columnspan=2, pady=10)
    else:
        messagebox.showerror("Erro", "Por favor, selecione um produto para atualizar.")

def atualizar_lista_produtos():
    lista_produtos.delete(0, tk.END)
    for produto in produtos:
        lista_produtos.insert(tk.END, f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}, Fornecedor: {produto['fornecedor']}")

def atualizar_estoque():
    janela = tk.Toplevel()
    janela.title("Atualizar Estoque")
    
    frame = tk.Frame(janela)
    frame.pack(pady=20, padx=20)
    
    label = tk.Label(frame, text="Atualização de Estoque")
    label.pack()
    
    global lista_produtos
    lista_produtos = tk.Listbox(frame, width=50)
    lista_produtos.pack(pady=10)
    
    button_atualizar = tk.Button(frame, text="Atualizar Quantidade", command=atualizar_quantidade)
    button_atualizar.pack(pady=10)
    
    atualizar_lista_produtos()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    atualizar_estoque()
    root.mainloop()