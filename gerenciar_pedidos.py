import tkinter as tk
from tkinter import messagebox, ttk
from cadastrar_produto import produtos, atualizar_lista_produtos
from gerenciar_clientes import obter_clientes 

pedidos = []

def validar_numeros(entry_value):
    """
    Valida se o valor inserido é numérico ou vazio.
    Exibe uma mensagem de erro se o valor não for numérico.
    :param entry_value: Valor do campo de entrada.
    :return: True se o valor for numérico ou vazio, False caso contrário.
    """
    if entry_value.isdigit() or entry_value == "":
        return True
    else:
        messagebox.showerror("Erro", "Por favor, insira somente números")
        return False

def adicionar_pedido(parent):
    """
    Abre uma janela para adicionar um novo pedido.
    Salva o pedido na lista de pedidos se todos os campos estiverem preenchidos corretamente.
    """
    def salvar_pedido():
        produto_selecionado = combobox_produto.get()
        quantidade_pedido = entry_quantidade_pedido.get()
        cliente_selecionado = combobox_cliente.get()
        
        if produto_selecionado and quantidade_pedido.isdigit() and cliente_selecionado:
            quantidade_pedido = int(quantidade_pedido)
            produto = next((p for p in produtos if p['nome'] == produto_selecionado), None)
            
            if produto and quantidade_pedido <= produto['quantidade']:
                pedidos.append({"produto": produto_selecionado, "quantidade": quantidade_pedido, "cliente": cliente_selecionado})
                produto['quantidade'] -= quantidade_pedido
                atualizar_lista_produtos()
                atualizar_lista_pedidos()
                messagebox.showinfo("Sucesso", "Seu pedido foi adicionado com sucesso!")
                janela_adicionar.destroy()
                parent.deiconify()
            else:
                messagebox.showerror("Erro", "Quantidade insuficiente no estoque.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
    
    parent.withdraw()
    janela_adicionar = tk.Toplevel()
    janela_adicionar.title("Adicionar Pedido")
    
    frame_adicionar = tk.Frame(janela_adicionar)
    frame_adicionar.pack(pady=20, padx=20)
    
    label_produto = tk.Label(frame_adicionar, text="Produto")
    label_produto.grid(row=0, column=0, pady=5)
    
    combobox_produto = ttk.Combobox(frame_adicionar, values=[produto['nome'] for produto in produtos])
    combobox_produto.grid(row=0, column=1, pady=5)
    
    label_quantidade_pedido = tk.Label(frame_adicionar, text="Quantidade")
    label_quantidade_pedido.grid(row=1, column=0, pady=5)
    
    entry_quantidade_pedido = tk.Entry(frame_adicionar, validate="key")
    entry_quantidade_pedido.grid(row=1, column=1, pady=5)

    label_cliente = tk.Label(frame_adicionar, text="Cliente")
    label_cliente.grid(row=2, column=0, pady=5)

    combobox_cliente = ttk.Combobox(frame_adicionar, values=obter_clientes())
    combobox_cliente.grid(row=2, column=1, pady=5)
    
    validate_command = janela_adicionar.register(validar_numeros)
    entry_quantidade_pedido.config(validatecommand=(validate_command, '%P'))
    
    button_salvar = tk.Button(frame_adicionar, text="Salvar", command=salvar_pedido)
    button_salvar.grid(row=3, columnspan=2, pady=10)

def remover_pedido():
    """
    Remove o pedido selecionado da lista de pedidos.
    Exibe uma mensagem de sucesso se o pedido for removido corretamente.
    Exibe uma mensagem de erro se nenhum pedido estiver selecionado.
    """
    selecionado = lista_pedidos.curselection()
    if selecionado:
        pedido_removido = pedidos.pop(selecionado[0])
        produto = next((p for p in produtos if p['nome'] == pedido_removido['produto']), None)
        if produto:
            produto['quantidade'] += pedido_removido['quantidade']
            atualizar_lista_produtos()
        atualizar_lista_pedidos()
        messagebox.showinfo("Sucesso", "Pedido removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, selecione um pedido para remover.")

def alterar_pedido():
    """
    Abre uma janela para alterar a quantidade de um pedido selecionado.
    Salva a alteração na lista de pedidos se a quantidade for válida e estiver disponível no estoque.
    """
    selecionado = lista_pedidos.curselection()
    if selecionado:
        pedido_selecionado = pedidos[selecionado[0]]
        
        def salvar_alteracao():
            nova_quantidade = entry_nova_quantidade.get()
            if nova_quantidade.isdigit():
                nova_quantidade = int(nova_quantidade)
                produto = next((p for p in produtos if p['nome'] == pedido_selecionado['produto']), None)
                
                if produto:
                    quantidade_disponivel = produto['quantidade'] + pedido_selecionado['quantidade']
                    if nova_quantidade <= quantidade_disponivel:
                        produto['quantidade'] = quantidade_disponivel - nova_quantidade
                        pedido_selecionado['quantidade'] = nova_quantidade
                        atualizar_lista_produtos()
                        atualizar_lista_pedidos()
                        messagebox.showinfo("Sucesso", f"Pedido de '{pedido_selecionado['produto']}' atualizado com sucesso!")
                        janela_alterar.destroy()
                    else:
                        messagebox.showerror("Erro", "Quantidade insuficiente no estoque.")
            else:
                messagebox.showerror("Erro", "Por favor, insira um valor numérico para a quantidade.")
        
        janela_alterar = tk.Toplevel()
        janela_alterar.title("Alterar Pedido")
        
        frame_alterar = tk.Frame(janela_alterar)
        frame_alterar.pack(pady=20, padx=20)
        
        label_produto = tk.Label(frame_alterar, text=f"Produto: {pedido_selecionado['produto']}")
        label_produto.grid(row=0, column=0, pady=5)
        
        label_nova_quantidade = tk.Label(frame_alterar, text="Nova Quantidade")
        label_nova_quantidade.grid(row=1, column=0, pady=5)
        
        entry_nova_quantidade = tk.Entry(frame_alterar, validate="key")
        entry_nova_quantidade.grid(row=1, column=1, pady=5)
        
        validate_command = janela_alterar.register(validar_numeros)
        entry_nova_quantidade.config(validatecommand=(validate_command, '%P'))
        
        button_salvar = tk.Button(frame_alterar, text="Salvar", command=salvar_alteracao)
        button_salvar.grid(row=2, columnspan=2, pady=10)
    else:
        messagebox.showerror("Erro", "Por favor, selecione um pedido para alterar.")

def atualizar_lista_pedidos():
    """
    Atualiza a lista de pedidos exibida na interface gráfica.
    Remove todos os itens da lista e insere novamente os pedidos com seus dados.
    """
    lista_pedidos.delete(0, tk.END)
    for pedido in pedidos:
        lista_pedidos.insert(tk.END, f"Produto: {pedido['produto']}, Quantidade: {pedido['quantidade']}, Cliente: {pedido['cliente']}")

def gerenciar_pedidos():
    """
    Cria uma nova janela para gerenciamento de pedidos.
    Configura a interface gráfica com opções para adicionar, remover e alterar pedidos, e uma lista de pedidos.
    """
    janela = tk.Toplevel()
    janela.title("Gerenciar Pedidos")
    
    frame = tk.Frame(janela)
    frame.pack(pady=20, padx=20)
    
    button_adicionar = tk.Button(frame, text="Adicionar Pedido", command=lambda: adicionar_pedido(janela))
    button_adicionar.pack(pady=10)
    
    button_remover = tk.Button(frame, text="Remover Pedido", command=remover_pedido)
    button_remover.pack(pady=10)
    
    button_alterar = tk.Button(frame, text="Alterar Pedido", command=alterar_pedido)
    button_alterar.pack(pady=10)
    
    global lista_pedidos
    lista_pedidos = tk.Listbox(frame, width=50)
    lista_pedidos.pack(pady=10)
    
    atualizar_lista_pedidos()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    gerenciar_pedidos()
    root.mainloop()