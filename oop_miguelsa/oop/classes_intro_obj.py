#Importar as classes do outro programa para este
from classes_intro_blueprints import Pessoa
from classes_intro_blueprints import Carro
 

#Instanciação das classes no ficheiro 
pessoa = Pessoa("João", 16)
carro = Carro("Tesla", "Model 3")
 
 
#Chamar a função da classe, utilizando os dados que eu atribui na instanciação
print(pessoa.saudacao())
print(carro.informacao_do_carro())