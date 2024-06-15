import tkinter as tk
from tkinter import messagebox
from cadastrar_produto import produtos
from gerenciar_clientes import clientes  
from gerenciar_fornecedores import fornecedores  
from gerenciar_pedidos import pedidos  
from atualizar_estoque import correcoes_estoque  

def gerar_relatorio():
    janela = tk.Toplevel()
    janela.title("Relatório de Produtos, Clientes, Fornecedores, Pedidos e Correções de Estoque")
    
    frame = tk.Frame(janela)
    frame.pack(pady=20, padx=20)
    
    label = tk.Label(frame, text="Relatório de Produtos, Clientes, Fornecedores, Pedidos e Correções de Estoque")
    label.pack()
    
    text_relatorio = tk.Text(frame, width=100, height=40)
    text_relatorio.pack(pady=10)
    
    relatorio = "Relatório de Produtos Adicionados\n"
    relatorio += "=" * 80 + "\n"
    
    if produtos:
        relatorio += "Produto\tQuantidade\tFornecedor\n"
        relatorio += "-" * 80 + "\n"
        
        for produto in produtos:
            relatorio += f"{produto['nome']}\t{produto['quantidade']}\t{produto['fornecedor']}\n"
            if produto['quantidade'] < 50:
                relatorio += f"*** Atenção: {produto['nome']} está com quantidade abaixo de 50! ***\n"
        relatorio += "\n"
    else:
        relatorio += "Nenhum produto adicionado.\n\n"
    
    relatorio += "Relatório de Clientes Adicionados\n"
    relatorio += "=" * 80 + "\n"
    
    if clientes:
        relatorio += "ID\tNome\tCPF/CNPJ\n"
        relatorio += "-" * 80 + "\n"
        
        for cliente in clientes:
            relatorio += f"{cliente['id']}\t{cliente['nome']}\t{cliente['cpf_cnpj']}\n"
    else:
        relatorio += "Nenhum cliente adicionado.\n"
    
    relatorio += "\nRelatório de Fornecedores Adicionados\n"
    relatorio += "=" * 80 + "\n"
    
    if fornecedores:
        relatorio += "Nome Completo\tCPF/CNPJ\tData de Nascimento\n"
        relatorio += "-" * 80 + "\n"
        
        for fornecedor in fornecedores:
            relatorio += f"{fornecedor['nome']}\t{fornecedor['cpf_cnpj']}\t{fornecedor['data_nascimento']}\n"
    else:
        relatorio += "Nenhum fornecedor adicionado.\n"

    relatorio += "\nRelatório de Pedidos Solicitados\n"
    relatorio += "=" * 80 + "\n"
    
    if pedidos:
        relatorio += "Produto\tQuantidade\tCliente\n"
        relatorio += "-" * 80 + "\n"
        
        for pedido in pedidos:
            relatorio += f"{pedido['produto']}\t{pedido['quantidade']}\t{pedido['cliente']}\n"
    else:
        relatorio += "Nenhum pedido solicitado.\n"
    
    relatorio += "\nRelatório de Correções de Estoque\n"
    relatorio += "=" * 80 + "\n"
    
    if correcoes_estoque:
        relatorio += "Produto\tQuantidade Anterior\tNova Quantidade\tMotivo\n"
        relatorio += "-" * 80 + "\n"
        
        for correcao in correcoes_estoque:
            relatorio += f"{correcao['produto']}\t{correcao['quantidade_anterior']}\t{correcao['nova_quantidade']}\t{correcao['motivo']}\n"
    else:
        relatorio += "Nenhuma correção de estoque realizada.\n"
    
    text_relatorio.insert(tk.END, relatorio)
    text_relatorio.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    gerar_relatorio()
    root.mainloop()