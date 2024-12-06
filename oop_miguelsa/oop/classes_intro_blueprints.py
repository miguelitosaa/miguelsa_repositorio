#Criação de uma classe para uma pessoa
class Pessoa:

    #Função para inicializar a classe, declara também o nome e a idade
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    #Função para dar o output da classe Pessoa
    def saudacao(self):
        return f"O meu nome é {self.nome} e tenho {self.idade} anos."
    
#Criação da classe para um carro
class Carro:

    #Função para inicializar a classe, declara também a marca e o modelo do carro
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    #Função para dar o output da classe Carro    
    def informacao_do_carro(self):
        return f"Este é um {self.marca} {self.modelo}."