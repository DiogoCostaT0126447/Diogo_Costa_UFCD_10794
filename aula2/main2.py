from Pessoa import Pessoa

p = Pessoa("João", 1.75, 70, 20)
p1 = Pessoa("Maria", 1.65, 60, 22)

print(p.nome)

str_p = str(p)

print(str_p)

"""
    (int ) "10"; --> 10
"""

print(p > p1)