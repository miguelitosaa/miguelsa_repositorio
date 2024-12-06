#Importar as classes do ficheiro que tem as classes
from classe_sobre_futebol import Vestimenta
from classe_sobre_futebol import Club
from classe_sobre_futebol import Estatisticas

#Instanciação das classes
vestimenta = Vestimenta("L", 46)
club = Club("Águia Desnutridas", "extremo")
Estatisticas = Estatisticas(20, 13)

#Chamar a função da classe, utilizando os dados que eu atribui na instanciação
print(vestimenta.tamanho())
print(club.info())
print(Estatisticas.numero_de_golos_e_assistencias())