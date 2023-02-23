
class Item:
    def __init__(self, codigo, valor, nomeProduto):
        self.codigo = codigo
        self.valor = valor
        self.nomeProduto = nomeProduto

def cadastrar_item():
    print("Chamando cadastrar item()")
    codigo_do_item = input("Digite o codigo do item: ")
    valor_do_item = float(input("Digite o valor do item: "))
    nome_do_produto = input("Digite o nome do item:  ")
    item = Item(codigo_do_item, valor_do_item, nome_do_produto)
    return item


def carrinho(item):
    print("Adicionando item ao carrinho:", item.nomeProduto)

import os

def limpar_prompt():
    os.system("cls")


def NotaFiscal(cliente, carrinho_itens):
    print(f" Nota Fiscal\n Nome do cliente: {cliente.nome}")
    print("Lista de Produtos Comprados: ")
    for item in carrinho_itens:
        print(f"Nome do produto: {item.nomeProduto} | Valor: R${item.valor}")
    soma = 0
    for item in carrinho_itens:
        soma += item.valor
    print(f"Valor total da compra: {soma}")
    print("Obrigado por comprar com nosso sistema de automação de vendas\n --------Volte sempre--------")
#soma = 0
#or item in carrinho_itens:
#    soma += item.valor
#print(f"Valor total dos itens: {soma}")
