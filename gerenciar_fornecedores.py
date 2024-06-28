import tkinter as tk
from tkinter import messagebox

fornecedores = []

def validar_entrada(entry_value):
    """
    Valida se o valor inserido é numérico, vazio ou contém o caractere '/'.
    Exibe uma mensagem de erro se o valor não for válido.
    
    :param entry_value: Valor do campo de entrada.
    :return: True se o valor for válido, False caso contrário.
    """
    if entry_value.isdigit() or entry_value == "" or "/" in entry_value:
        return True
    else:
        messagebox.showerror("Erro", "Por favor, insira somente números.")
        return False

def adicionar_fornecedor():
    """
    Abre uma janela para adicionar um novo fornecedor.
    Salva o fornecedor na lista de fornecedores se todos os campos estiverem preenchidos corretamente.
    """
    def salvar_fornecedor():
        nome_fornecedor = entry_nome_fornecedor.get()
        cpf_cnpj_fornecedor = entry_cpf_cnpj.get()
        data_nascimento_fornecedor = entry_data_nascimento.get()
        
        if nome_fornecedor and cpf_cnpj_fornecedor and data_nascimento_fornecedor:
            novo_fornecedor = {
                "nome": nome_fornecedor,
                "cpf_cnpj": cpf_cnpj_fornecedor,
                "data_nascimento": data_nascimento_fornecedor
            }
            fornecedores.append(novo_fornecedor)
            atualizar_lista_fornecedores()
            messagebox.showinfo("Sucesso", f"Fornecedor '{nome_fornecedor}' adicionado com sucesso!")
            janela_adicionar.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    
    janela_adicionar = tk.Toplevel()
    janela_adicionar.title("Adicionar Fornecedor")
    
    frame_adicionar = tk.Frame(janela_adicionar)
    frame_adicionar.pack(pady=20, padx=20)
    
    label_nome_fornecedor = tk.Label(frame_adicionar, text="Nome Completo")
    label_nome_fornecedor.grid(row=0, column=0, pady=5)
    
    entry_nome_fornecedor = tk.Entry(frame_adicionar)
    entry_nome_fornecedor.grid(row=0, column=1, pady=5)
    
    label_cpf_cnpj = tk.Label(frame_adicionar, text="CPF/CNPJ")
    label_cpf_cnpj.grid(row=1, column=0, pady=5)
    
    entry_cpf_cnpj = tk.Entry(frame_adicionar, validate="key")
    entry_cpf_cnpj.grid(row=1, column=1, pady=5)
    
    label_data_nascimento = tk.Label(frame_adicionar, text="Data de Nascimento")
    label_data_nascimento.grid(row=2, column=0, pady=5)
    
    entry_data_nascimento = tk.Entry(frame_adicionar, validate="key")
    entry_data_nascimento.grid(row=2, column=1, pady=5)
    
    validate_command = janela_adicionar.register(validar_entrada)
    entry_cpf_cnpj.config(validatecommand=(validate_command, '%P'))
    entry_data_nascimento.config(validatecommand=(validate_command, '%P'))
    
    button_salvar = tk.Button(frame_adicionar, text="Salvar", command=salvar_fornecedor)
    button_salvar.grid(row=3, columnspan=2, pady=10)

def remover_fornecedor():
    """
    Remove o fornecedor selecionado da lista de fornecedores.
    Exibe uma mensagem de sucesso se o fornecedor for removido corretamente.
    Exibe uma mensagem de erro se nenhum fornecedor estiver selecionado.
    """
    selecionado = lista_fornecedores.curselection()
    if selecionado:
        fornecedores.pop(selecionado[0])
        atualizar_lista_fornecedores()
        messagebox.showinfo("Sucesso", "Fornecedor removido com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, selecione um fornecedor para remover.")

def atualizar_lista_fornecedores():
    """
    Atualiza a lista de fornecedores exibida na interface gráfica.
    Remove todos os itens da lista e insere novamente os fornecedores com seus dados.
    """
    lista_fornecedores.delete(0, tk.END)
    for fornecedor in fornecedores:
        lista_fornecedores.insert(tk.END, f"Nome: {fornecedor['nome']}, CPF/CNPJ: {fornecedor['cpf_cnpj']}, Data de Nascimento: {fornecedor['data_nascimento']}")

def gerenciar_fornecedores():
    """
    Cria uma nova janela para gerenciamento de fornecedores.
    Configura a interface gráfica com opções para adicionar e remover fornecedores, e uma lista de fornecedores.
    """
    janela = tk.Toplevel()
    janela.title("Gerenciar Fornecedores")
    
    frame = tk.Frame(janela)
    frame.pack(pady=20, padx=20)
    
    label = tk.Label(frame, text="Gerenciamento de Fornecedores")
    label.pack()
    
    button_adicionar = tk.Button(frame, text="Adicionar Fornecedor", command=adicionar_fornecedor)
    button_adicionar.pack(pady=10)
    
    button_remover = tk.Button(frame, text="Remover Fornecedor", command=remover_fornecedor)
    button_remover.pack(pady=10)
    
    global lista_fornecedores
    lista_fornecedores = tk.Listbox(frame, width=80)
    lista_fornecedores.pack(pady=10)
    
    atualizar_lista_fornecedores()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  
    gerenciar_fornecedores()
    root.mainloop()