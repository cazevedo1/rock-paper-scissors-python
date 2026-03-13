# --- JOGO PEDRA, PAPEL E TESOURA EM PYTHON (2 PLayers) ---

# --- Variavéis para Armazenamento de Dados (Opção Futura)
empates = 0
vitoria_player1 = 0
vitoria_player2 = 0

# --- 0. Função para executar o jogo
def jogo():

    # Variáveis Globais
    global empates, vitoria_player1, vitoria_player2

    # --- 0.1 Definindo as opções validas para escolha
    opcoes_validas = ("pedra", "papel", "tesoura")
    
    # --- 0.2 Coletando jogadas
    jogada_player1 = input(f"\nPlayer 1 ({username}) - Escolha sua jogada: (Pedra, Papel ou Tesoura)")
    jogada_player2 = input(f"\nPlayer 2 ({username2}) - Escolha sua jogada: (Pedra, Papel ou Tesoura)")

    # --- 0.3 Tratamento dos dados
        # 0.3.1 Retirando os espaços
    jogada_tratada_player1 = jogada_player1.strip().lower()
    jogada_tratada_player2 = jogada_player2.strip().lower()
    

    # --- 0.4 Imprimindo as jogadas
    print("-" * 30)
    print(f"O jogador 1 escolheu: {jogada_tratada_player1}")
    print(f"O jogador 2 escolheu: {jogada_tratada_player2}")
    print("-" * 30)

    # --- 0.5 Resultado Final do Jogo
        # 0.5.1 Verifica se as jogadas são válidas
    if jogada_tratada_player1 not in opcoes_validas or jogada_tratada_player2 not in opcoes_validas:
        print("Alguma jogada não foi inserida corretamente, volte e insira novamente as jogadas válidas!")
        print("-" * 60)
        return

        # 0.5.2 Verifica caso de Empate
    elif jogada_tratada_player1 == jogada_tratada_player2:
        print("Hm! Vocês empataram!")
        print("-" * 60)
        empates += 1

        # 0.5.3 Verifica condições de Vitórias do Player 1
    elif (jogada_tratada_player1 == "pedra" and jogada_tratada_player2 == "tesoura") or \
         (jogada_tratada_player1 == "papel" and jogada_tratada_player2 == "pedra") or \
         (jogada_tratada_player1 == "tesoura" and jogada_tratada_player2 == "papel"):
        print(f"Parabéns {username}! Você ganhou!")
        print("-" * 60)
        vitoria_player1 += 1

        # 0.5.4 Vitoria do Player 2
    else:
        print(f"Parabéns {username2}! Você ganhou!")
        vitoria_player2 += 1

# --- 1. Apresentando o jogo
print("--------------------------------------------")
print("---- Pedra, Papel e Tesoura (2 Players) ----")
print("--------------------------------------------")
print("-------- Olá! Bem vindos ao Jogo! ----------")

# --- 2. Coletando Nomes dos Player e Questionando as regras

 # 2.1 Coletando os nomes dos Players
username = input("\nQual seu nome? (Player 1) ")
username2 = input("\nQual seu nome? (Player 2) ")

 # 2.2 Questionando sobre o conhecimento das regras
while True:
    try:
        users_answer_regra = int(input(f"\n {username} e {username2}, vocês já sabem as regras? Escolha uma opção: \n  (1) Já sei as regras! \n  (2) Não sei as regras! "))
        print("-" * 60)
        
        # --- 3. Contando as regras em caso de não conhecimento e inicando o jogo
        if users_answer_regra == 2:
            print(f"As regras do jogo são: \n- Escolha entre Pedra, Papel ou Tesoura \n- No jogo as condições de vitória são: \n1. PEDRA quebra a Tesoura \n2. TESOURA corta o Papel \n3. PAPEL embrulha a Pedra \nEssas são as regras {username} e {username2}, agora bora jogar! \n")
            break
            
            # 3.1 Começando o Jogo
        elif users_answer_regra == 1:
            break
            
            # 3.2 Retornando um erro de entrada
        else:
            print("Insira um valor válido.")
            
    except ValueError:
        print("Digite apenas números!")
        

# --- 4. Perguntando se deseja jogar novamente (usando while para prender player até ele digitar um valor válido)
while True:
    jogo()
    
    while True: 
        play_again = input("\n Você deseja jogar Novamente? \n- (1) Sim, desejo \n- (2) Não, obrigado")
    
        # 4.1 Player deseja jogar novamente, rodando novamente o jogo
        if play_again == "1":
            break
    
        # 4.2 Player não deseja jogar, encerando o jogo e imprimindo um resultado final
        elif play_again == "2":
            print("-" * 60)
            print(f" O resultado final foi de: \n - Empates: {empates}\n - Vitórias do Player 1 ({username}): {vitoria_player1} \n - Vitórias do Player 1 ({username2}): {vitoria_player2}\n")
            print("-" * 60)
            empates, vitoria_player1, vitoria_player2 = 0, 0, 0
            exit()
    
        # 4.3 Player não digitou um valor válido
        else:
            print("Digite um valor válido! (1 ou 2) \n")