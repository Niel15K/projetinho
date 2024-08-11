import tkinter as tk
from tkinter import ttk, messagebox

class Item:
    def __init__(self, codigo, valor, nomeProduto):
        self.codigo = codigo
        self.valor = valor
        self.nomeProduto = nomeProduto

class Cliente:
    def __init__(self, nome):
        self.nome = nome

# Funções auxiliares
def cadastrar_item():
    codigo_do_item = codigo_var.get()
    valor_do_item = valor_var.get()
    nome_do_produto = nome_var.get()

    if not codigo_do_item or not valor_do_item or not nome_do_produto:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    try:
        valor_do_item = float(valor_do_item)
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números no campo de valor.")
        return

    item = Item(codigo_do_item, valor_do_item, nome_do_produto)
    carrinho_itens.append(item)
    atualizar_lista()

def atualizar_lista():
    carrinho_listbox.delete(0, tk.END)
    for item in carrinho_itens:
        carrinho_listbox.insert(tk.END, f"Nome: {item.nomeProduto} | Valor: R${item.valor:.2f}")

def remover_item():
    selecionado = carrinho_listbox.curselection()
    if selecionado:
        carrinho_itens.pop(selecionado[0])
        atualizar_lista()
    else:
        messagebox.showwarning("Atenção", "Selecione um item para remover.")

def finalizar_compra():
    if not carrinho_itens:
        messagebox.showwarning("Atenção", "O carrinho está vazio!")
        return

    soma = sum(item.valor for item in carrinho_itens)
    mensagem = f"Nome do cliente: {cliente.nome}\n"
    mensagem += "Lista de Produtos Comprados:\n"
    for item in carrinho_itens:
        mensagem += f"{item.nomeProduto} - R${item.valor:.2f}\n"
    mensagem += f"\nValor total da compra: R${soma:.2f}"
    messagebox.showinfo("Nota Fiscal", mensagem)
    carrinho_itens.clear()
    atualizar_lista()

def toggle_mode():
    if dark_mode.get():
        # Configurar tema escuro
        app.config(bg="#212529")  # Cor de fundo escura
        for frame in [frame_cliente, frame_itens, frame_carrinho, frame_acoes]:
            frame.config(style="Dark.TFrame")
        style.configure("TLabel", background="#212529", foreground="#f8f9fa")
        style.configure("TButton", background="#343a40", foreground="#000070")
        style.configure("TEntry", fieldbackground="#495057", foreground="#000070")
        toggle_btn.config(image=moon_image, bg="#212529", fg="#f8f9fa")
        dark_mode.set(False)
    else:
        # Configurar tema claro
        app.config(bg="#f8f9fa")  # Cor de fundo clara
        for frame in [frame_cliente, frame_itens, frame_carrinho, frame_acoes]:
            frame.config(style="TFrame")
        style.configure("TLabel", background="#f8f9fa", foreground="#212529")
        style.configure("TButton", background="#ffffff", foreground="#212529")
        style.configure("TEntry", fieldbackground="#ffffff", foreground="#212529")
        toggle_btn.config(image=sun_image, bg="#ffffff", fg="#212529")
        dark_mode.set(True)

# Interface Gráfica
app = tk.Tk()
app.title("Sistema de Vendas")
app.geometry("600x600")

# Centralizar a janela
app.update_idletasks()
window_width = app.winfo_width()
window_height = app.winfo_height()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
app.geometry(f'{window_width}x{window_height}+{x}+{y}')

dark_mode = tk.BooleanVar(value=True)  # Modo escuro por padrão

# Estilo ttk
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f8f9fa")  # Fonte menor
style.configure("TButton", font=("Arial", 12), padding=4)  # Fonte menor e padding reduzido
style.configure("TEntry", font=("Arial", 12), padding=4)  # Fonte menor e padding reduzido
style.configure("TFrame", background="#f8f9fa")
style.configure("Dark.TFrame", background="#212529")

# Frames para organização
frame_cliente = ttk.Frame(app, padding="10")
frame_cliente.grid(row=0, column=0, sticky="ew")

frame_itens = ttk.Frame(app, padding="10")
frame_itens.grid(row=1, column=0, sticky="ew")

frame_carrinho = ttk.Frame(app, padding="10")
frame_carrinho.grid(row=2, column=0, sticky="ew")

frame_acoes = ttk.Frame(app, padding="10")
frame_acoes.grid(row=3, column=0, sticky="ew")

# Cliente
cliente_nome = tk.StringVar()
ttk.Label(frame_cliente, text="Nome do Cliente:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame_cliente, textvariable=cliente_nome, width=25).grid(row=0, column=1, sticky="ew", padx=5, pady=5)

# Itens
codigo_var = tk.StringVar()
valor_var = tk.StringVar()
nome_var = tk.StringVar()

ttk.Label(frame_itens, text="Código do Item:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame_itens, textvariable=codigo_var, width=25).grid(row=1, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(frame_itens, text="Valor do Item:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame_itens, textvariable=valor_var, width=25).grid(row=2, column=1, sticky="ew", padx=5, pady=5)

ttk.Label(frame_itens, text="Nome do Produto:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(frame_itens, textvariable=nome_var, width=25).grid(row=3, column=1, sticky="ew", padx=5, pady=5)

ttk.Button(frame_itens, text="Adicionar ao Carrinho", command=cadastrar_item).grid(row=4, column=1, pady=10, padx=5)

# Lista de itens no carrinho
ttk.Label(frame_carrinho, text="Carrinho de Compras:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
carrinho_listbox = tk.Listbox(frame_carrinho, width=45, height=10, font=("Arial", 10))
carrinho_listbox.grid(row=6, column=0, columnspan=2, pady=5, padx=5)

# Ações
ttk.Button(frame_acoes, text="Remover Item", command=remover_item).grid(row=7, column=0, sticky="w", padx=5, pady=5)
ttk.Button(frame_acoes, text="Finalizar Compra", command=finalizar_compra).grid(row=7, column=1, sticky="e", padx=5, pady=5)

# Toggle de modo claro/escuro
toggle_frame = tk.Frame(app, bg="#f8f9fa")
toggle_frame.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

sun_image = tk.PhotoImage(file="sol.png").subsample(15, 15)
moon_image = tk.PhotoImage(file="lua.png").subsample(15, 15)

toggle_btn = tk.Button(toggle_frame, text="Modo Escuro", command=toggle_mode, bd=0)
toggle_btn.pack(side=tk.RIGHT)
toggle_btn.config(image=sun_image)

# Inicializa
cliente = Cliente(cliente_nome.get())
carrinho_itens = []

# Aplica o modo escuro ao iniciar
toggle_mode()

app.mainloop()
