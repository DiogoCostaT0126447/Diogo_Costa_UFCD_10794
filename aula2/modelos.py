"""
    marca
    modelo
    ano
    num_km
"""

class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca.title()
        self.modelo = modelo.title()
        
        
#Crie a class livro (defina apenas os atributos)

class Livro:
    def __init__(self, titulo: str, autor: str, ano_publicacao: int, num_paginas: int):
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.ano_publicacao = ano_publicacao
        self.num_paginas = num_paginas