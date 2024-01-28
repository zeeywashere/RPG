class Personagem:
    def __init__(self, nome, raca, vida, ataque, defesa, especializacao=None, magia=None, explicacao=None):
        # Inicializa as propriedades do personagem
        self.nome = nome
        self.raca = raca
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.especializacao = especializacao
        self.magia = magia
        self.explicacao = explicacao

def criar_personagem():
    # Solicita informações do usuário para criar um personagem
    nome = input("Digite o nome do seu personagem: ")
    print("Escolha sua raça:")
    print("1. Humano")
    print("2. Mago")
    print("3. Fada")
    opcao_raca = input("Escolha 1, 2 ou 3: ")

    especializacao = None
    magia = None
    explicacao = None

    if opcao_raca == "1":
        # Configurações para a raça Humano
        raca = "Humano"
        vida = 130
        ataque = 100
        defesa = 30
        print("Você quer ser ferreiro ou espadachin?")
        especializacao_opcao = input("Digite 1 para ferreiro ou 2 para espadachin: ")
        if especializacao_opcao == "1":
            especializacao = "Ferreiro"
            explicacao = "Ferreiros são habilidosos na criação de armas e armaduras, sendo essenciais para equipar a si mesmos e seus aliados."
        elif especializacao_opcao == "2":
            especializacao = "Espadachin"
            explicacao = "Espadachins são guerreiros habilidosos no combate corpo a corpo, demonstrando grande destreza com suas lâminas e grande poderes de cortar tudo."
        else:
            print("Opção inválida. Escolha novamente.")
            return criar_personagem()
    elif opcao_raca == "2":
        # Configurações para a raça Mago
        raca = "Mago"
        vida = 80
        ataque = 50
        defesa = 20
        print("Escolha sua magia:")
        print("1. Deus do Sol")
        print("2. Escuridão Profunda")
        print("3. Dragon")
        opcao_magia = input("Escolha 1, 2 ou 3: ")
        if opcao_magia == "1":
            magia = "Deus do Sol"
            explicacao = "Deus do Sol: Permite ao usuário se transformar no lendário Deus do sol  transformando o seu corpo em borracha, possui varios poderes sendo eles:  O usuário pode esticar e retrair partes de seus corpos como se fossem de borracha real, Toque Puro: Tudo que ele tocar transforma em borracha "
        elif opcao_magia == "2":
            magia = "Tempestade"
            explicacao = "Escuridão profunda: Permite o usuario ter a magia de total controle sobre a escuridão, com vairos poderes sendo eles: Caminho do Buraco Negro: Espalha sua escuridao por uma grande area e engole tudo que escolhe, Espiral Negra: Tem o poder da gravidade de suas trevas, puxando o alvo para o seu alcance."
        elif opcao_magia == "3":
            magia = "Dragon"
            explicacao = "Dragon: Permite ao usuário se transformar em uma forma híbrida de dragão, com varios poderes sendo eles: Bafo de Calor: ,  Em sua boca cria uma enorme e cônica explosão em direção ao alvo e tendo seu voo super rapido. "
        else:
            print("Opção inválida. Escolha novamente.")
            return criar_personagem()
        especializacao = "Mago"
    elif opcao_raca == "3":
        # Configurações para a raça Fada
        raca = "Fada"
        vida = 150
        ataque = 5
        defesa = 30
        especializacao = "Assistente"
        magia = "Cura"
        explicacao = "As fadas são seres mágicos que são para assistência. Elas têm a habilidade natural de curar pessoas e jogar flechas no alvo, tornando-as valiosas em situações de grupo e suporte."
    else:
        # Trata opção inválida
        print("Opção inválida. Escolha novamente.")
        return criar_personagem()

    # Exibe informações sobre a escolha do jogador
    print(f"\n{explicacao}\n")
    return Personagem(nome, raca, vida, ataque, defesa, especializacao, magia, explicacao)

if __name__ == "__main__":
    # Início do programa
    print("Olá, Bem-vindo ao Infinity At online\n")

    # Cria um personagem
    jogador = criar_personagem()

    # Exibe informações sobre o personagem criado
    print(f"\nPersonagem criado:\nNome: {jogador.nome}\nRaça: {jogador.raca}\nVida: {jogador.vida}\nAtaque: {jogador.ataque}\nDefesa: {jogador.defesa}")

    # Exibe informações específicas com base na raça escolhida
    if jogador.raca == "Humano":
        print(f"Especialização: {jogador.especializacao}")
        print(f"Informações sobre a especialização: {jogador.explicacao}")
        print("Ponto fraco: Os humanos são fracos em combate a distância")
        print("Ponto forte: Os humanos são fortes em combate a mano a mano")
        
        # Informação sobre o mago
        
    elif jogador.raca == "Mago":
        print(f"Magia escolhida: {jogador.magia}")
        print(f"Informações sobre a magia: {jogador.explicacao}")
        print("Ponto fraco: Os magos não possui tanta stamina então cansam mais rapido a cada magia.")
        print("Ponto forte: A cada magia que é usada o poder fica mais forte.")
        
        # Informação sobre a Fada
        
    elif jogador.raca == "Fada":
        print("Especialização: Assistente (pode curar pessoas)")
        print(f"Informações sobre a especialização: {jogador.explicacao}")
        print("Ponto fraco: Sem Ponto Fraco")
        print("Ponto forte: São fortes em combate a longa distância, jogando flechas no alvo e cura ate 10 de HP do aliado a cada 20 segundos")
        


