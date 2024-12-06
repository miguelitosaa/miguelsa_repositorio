#Criação de uma classe "Futebol"
class Vestimenta:

    #Função para inicializar a classe
    def __init__(self, camisola, chuteira):
        self.camisola = camisola
        self.chuteira = chuteira
    #Função para fazer o output da classe
    def tamanho(self):
        return f"O tamanho da minha camisola é {self.camisola} e o número da chateira é {self.chuteira}."

#Criação de uma classe "Club"
class Club:
    #Função para inicializar a classe
    def __init__(self,clube,posicao):
        self.clube = clube
        self.posicao = posicao
    #Função para o output da classe Club
    def info(self):
        return f"O meu clube é {self.clube} e a minha posição em campo é {self.posicao}."

#Criação de uma classe "Estatisticas"
class Estatisticas:
    def __init__(self, golos, assistencias):
        self.golos = golos
        self.assistencias = assistencias

    def numero_de_golos_e_assistencias(self):
        return f"Golos: {self.golos} \nAssistencias:{self.assistencias}"