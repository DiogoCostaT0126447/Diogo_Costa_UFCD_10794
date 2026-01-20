"""
var
op com var

condições
loops

listas
dict
set

funções



"""

"""
#crie uma variável com um nome e mostre esse nome na consola

nome = "Diogo"

print(nome)

#Mostre a msg "Ola <nome>", utilize 3 opcoes para mostrar a msg

print("Olá", nome)
print(f"Olá {nome}")
print("Olá " + nome)


print("---------------------------------")

n1 = 10
n2 = 10.0

soma = n1 + n1
print(soma)

sub = n1 - n2
print(sub)

n1 = 10.5
n2 = 10.5

soma = n1 + n2
print(soma)


n1 = 10.5
n2 = 10.5
divi = n1 / n2
print(divi)


n1 = 10.5
n2 = 10.5
multi = n1 * n2
print(multi)


print(type(n1))
print(type(n2))
print("--------------------------------")

#condições

# if - elif - else

#match - case

# tendo o codigo:

idade = 18 

#verifique se a pessoa é adulta ou não (um adulto tem mais de 18 anos)

if idade >= 18:
    print("Maior de idade")

else:
    print("Menor de idade")
    
    

#verifique se a pessoa e
# - adulta(18+)
# - adolescente (12 a 18)
# - crianca (menos)

if idade > 18:
    print("A pessoa é adulta")
elif idade >= 12:
    print("A pessoa é adolescente")
else:
    print("A pessoa é criança")
    
    
#Crie uma app que receba 2 notas
# se as duas notas forem positivas (mais de 10) o aluno esta aprovado
# se apenas uma das notas for positiva pode fazer recuperação
# se as duas notas forem negativas o aluno esta reprovado

input_nota1 = input("Insira a primeira nota: ")
input_nota2 = input("Insira a segunda nota: ")

nota1 = float(input_nota1)
nota2 = float(input_nota2)

if nota1 >= 10 and nota2 >= 10:
    print("Aprovado")
elif nota1 >= 10 or nota2 >= 10:
    print("Recuperação")
else:
    print("Reprovado")
    
print("--------------------------------")

#Crie um menu com 3 opcoes:
# 1 - mostrar msg "Ola Mundo"
# 2 - mostrar msg "Bom Dia"
# 3 - mostrar msg "Boa Noite"
# se a opcao for invalida mostre "Opcao Invalida"

print("--- Menu ---")
print("Opt1 --- Ola Mundo")
print("Opt2 --- Bom Dia")
print("Opt3 --- Boa Noite")

opcao = input("Escolha uma opcao (1, 2, 3): ")

if opcao == "1":
    print("Ola Mundo")
elif opcao == "2":
    print("Bom Dia")
elif opcao == "3":
    print("Boa Noite")
else:
    print("Opcao Invalida")
    
print("--------------------------------")


#loops 

#Faça uma app que mostre o resultado da tabuada
#deve pedir o num da tabuada



while True:
    print("--- Tabuada ---")
    print("Escolha uma opção:")
    print("1 - Mostrar tabuada")
    print("0 - Sair")
    escolha = input("Opção: ")
    
    if escolha == "0":
        break
    elif escolha == "1":
        num = int(input("Insira o numero da tabuada: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    else:
        print("Opção invalida")
        
    print("--------------------------------")



#adapte o codigo para pedir sempre uma opção até que o usuario queira sair(valor 0)


while True:
    print("Menu:")
    print("1 - Olá Mundo")
    print("2 - Bom dia")
    print("3 - Boa noite")
    print("0 - Sair")

    escolha = int(input("Escolha uma opção: "))

    match escolha : 
        case 1:
            print("Olá Mundo")
        case 2:
            print("Bom dia")
        case 3:
            print("Boa noite")
        case 0:
            print("Saindo do programa.")
            break
        case default:
            print("Opção inválida")
            
print("--------------------------------")



"""


lst = ["elm1", "elm2", "elm3"]
print(lst)
lst.append("elm4")
print(lst)
lst.append(30)
print(lst)
lst.remove("elm4")
lst.pop(0)
print(lst)

cnt = lst.count("elm1")
print(cnt)

print(len(lst))
print(lst.__len__())

nome = "Joao"

print(nome.__len__())

"""
lst:
    add
    remover
    contar 
    
"""
# crie um programa que peça 5 nomes; mostre a lista dos nomes pedidos
"""
nomes = []
for i in range(5):
    nome = input("Insira um nome: ")
    nomes.append(nome)
print("Nomes inseridos:", nomes)
"""

#crie um programa que peça ao utilizador nomes ate ser inserido "0"
#e mostre a lista dos nomes pedidos, deve mostrar um nome por linha
"""
nomes = []
while True:
    nome = input("Digite um nome (ou 0 para sair): ")
    if nome == "0":
        break
    nomes.append(nome)
for nome in nomes:
    print(nome)
    
print("--------------------------------")

"""

for elm in lst.__reversed__():
    print(elm)
    
# dict

aluno = {
    "nome": "Diogo",
    "media": 18,
    "estado": "aprovado"}

print(aluno)

aluno["escola"] = "ATEC"

print(aluno)

aluno["escola"] = "IEFP"

print(aluno)

aluno.pop("escola")

print(aluno)

aluno.popitem()
print(aluno)

for keys in aluno():
    print(keys)
print("--------------------------------")
for values in aluno.keys():
    print(values)    
print("--------------------------------")
for keys, values in aluno.items():
    print(f"{keys: 10} : {values}")
    
    
def nome():
    print("antes")
    pass
    print("depois")
    
def soma(val1, val2):
    return val1 + val2

res = soma(12, 12)

print(res)

def soma2(val1: int, val2: int) -> int:
    return val1 + val2

res2 = soma2(125, 15)
print(res)

def demo(num1: int, num2):
    pass