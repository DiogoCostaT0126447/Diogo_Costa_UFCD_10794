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
#adapte o codigo para pedir sempre uma opção até que o usuario queira sair(valor 0)


while True:
    num = int(input("Escreve o numero da tabuada (1-10) ou 0 para sair: "))

    if num == 0:
        print("Programa terminado.")
        break
    elif num < 1 or num > 10:
        print("Numero invalido\n")
    else:
        for i in range(1, 11):
            resultado = num * i
            print(f"{num} x {i} = {resultado}")
        
        
    print("--------------------------------")


    