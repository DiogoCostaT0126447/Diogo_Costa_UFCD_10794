class Pessoa:
    def __init__(self, nome:str, altura:float,peso:float, idade:int = 0):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.energia = 1
        self.acordado = True
        
     #por cada coisa que comer engorda 0.1 de peso    
    def comer (self, alimento: list[str]):
        for item in alimento:
            self.peso += (100 * alimento.__len__())
        
    
    def falar(self):
        return "Bla bla bla"
    
    def andar(self):
        return "A pessoa está a andar"
    
      
    def crescer(self, cm: float = 2.5):
        self.altura += cm 
        
    #até aos 21 anos a pessoa cresce 2.5 cm por ano
    def envelhecer(self, anos: int = 1):
        if self.idade < 21:
           self.crescer
        
        self.idade += anos
        
        print(f"A pessoa {self.nome} tem {self.idade} anos e {self.altura:.2f}m de altura.")
       
  
    
    def dormir(self):
        if self.acordado:
            self.acordado = False
            self.energia = 100
    
    #crie um metodo para accordar, garanta q so acorda se estiver a dormir
    def acordar(self):
        if self.energia == 0:
            self.energia = 100
            
    def __gt__ (self, other):
        return self.idade > other.idade 
    
    def __str__(self):
        return "class"
    
    
    
       

    