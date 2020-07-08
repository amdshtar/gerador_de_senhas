# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:09:03 2020

@author: amdsheran
"""

import random
from random import sample
from random import randint


def intercalar_com (lista, o_que):
    """Intercala cada elemento da lista com alguma coisa"""
    nova_lista = []
    
    for i, v in enumerate(lista):
        nova_lista.append(v)
        nova_lista.append(o_que)
    
    return nova_lista


def gerar_senha (num_palavras, separador):
    """Retorna a str de uma senha de num_palavras palavras intercaladas com um separador.
    """
    caminho_do_sistema = '<caminho>' # Substitua <caminho> pelo caminho do seu sistema até o dicionário de palavras.
    with open (caminho_do_sistema, 'r', encoding="utf8") as f:
        # Tranformamos o arquivo numa lista de palavras com determinado tamanho
        lista_de_palavras = [palavra[:-1] for palavra in f.readlines() if 9 > len(palavra) > 4]

    # Sorteamos n palavras da lista
    lista_escolhidas = sample (lista_de_palavras, num_palavras)

    senha = []
    for palavra in lista_escolhidas:
        senha.append(palavra)
        senha.append(separador)

    # Modificamos a senha
    del(senha[len(senha)-1]) # Retiramos o [ultimo separador, que n'ao separa coisa alguma]
    senha = ''.join(senha) # Transformamos de list para str, mas sem os parênteses e vírgulas

    return senha

print(
"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    *Programa feito por amdshtar*     ---     Seja bem vind@!
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
""")

def interação():
    print ("\n\nPodemos gerar uma senha de n palavras e escolher o que há entre elas. O módulo random está importado.")
    try:
        num_de_palavras = int(input("Digite o número de palavras: \n->"))
        separador_da_senha = input("\nDigite o separador entre as palavras (sem aspas): \n->")
    except ValueError:
        print("\nAlgo saiu errado... \nAtente-se às instruções de digitação da próxima vez.")
        return
    
    senha = gerar_senha(num_de_palavras, separador_da_senha)
    print(f"\nSua nova senha gerada é: \n>>>>  {senha}  <<<<\n")
    
    repetição = input("Deseja gerar uma nova senha? \nDigite <yes>/<y> para SIM ou <n>/<no> para sair: \n->")
    if repetição == 'y' or repetição == 'yes':
        interação()



interação()
