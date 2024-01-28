# import habilidade
# from habilidade import exibir_informacoes_habilidade


class Personagem:
    def __init__(self, nome, raca, vida, ataque, defesa, especializacao=None, magia=None, explicacao=None):
        self.nome = nome
        self.raca = raca
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.especializacao = especializacao
        self.magia = magia
        self.explicacao = explicacao

nome = input("Digite o nome do seu personagem: ")
opcao_raca = input("Escolha 1, 2 ou 3: ")
raca = "elfo"
vida = 100
ataque = 1000
defesa = 195
personagem = Personagem(nome,raca,vida,ataque,defesa)





# def criar_personagem():
#     print("Escolha sua raça:")
#     print("1. Humano")
#     print("2. Mago")
#     print("3. Fada")

#     # Implemente o código de criação do personagem conforme necessário
print(personagem.nome)



# def exibir_informacoes_raca(personagem):
#     if personagem.raca == "Humano":
#         print(f"Especialização: {personagem.especializacao}")
#         print(f"Informações sobre a especialização: {personagem.explicacao}")
#         print("Ponto fraco: Os humanos são fracos em combate a distância")
#         print("Ponto forte: Os humanos são fortes em combate a mano a mano")
#     elif personagem.raca == "Mago":
#         print(f"Magia escolhida: {personagem.magia}")
#         print(f"Informações sobre a magia: {personagem.explicacao}")
#         print("Ponto fraco: Os magos não possuem tanta stamina, cansam mais rápido a cada magia.")
#         print("Ponto forte: A cada magia que é usada, o poder fica mais forte")
#     elif personagem.raca == "Fada":
#         print("Especialização: Assistente (pode curar pessoas)")
#         print(f"Informações sobre a especialização: {personagem.explicacao}")
#         print("Ponto fraco: Sem Ponto Fraco")
#         print("Ponto forte: São fortes em combate a longa distância, jogando flechas no alvo e curando até 10 de HP do aliado a cada 20 segundos")

# # Você pode adicionar mais lógica ou funções relacionadas às raças aqui, se necessário
