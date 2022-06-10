'''
Nome: Joyce Mayara Gonçalves de Oliveira
E-mail: joymoliveirag@gmail.com
Curso: Análise e Desenvolvimento de Sistemas

'''
import time # para uso da função sleep()
from jogador import * # importa a classe jogador
from tubo import * # importa a classe tubo
from turno import * # importa a classe turno

# Prints.
def welcome():
    f = open("welcome.txt", "r", encoding="utf-8")
    print(f.read())

# Função para retornar um objeto jogador a partir de seu nome.
def buscaJogador(jogadores, nome):
    for j in jogadores:
        if j.nome == nome:
            return j 
    return None

# Função para reiniciar a pontuação dos jogadores.
def reinicializarPontos(jogadores):
    for j in jogadores:
        j.cerebros = 0

# Lê a quantidade de jogadores e retorna a quantidade.
def lerQtdJogadores():
    qtd_jogadores = 0
    # A quantidade deve ser entre 2 e 99.
    while qtd_jogadores < 2 or qtd_jogadores > 99:
        qtd_jogadores = input('Quantos jogadores irão jogar? ')
        if not qtd_jogadores.isdigit():
            qtd_jogadores = 0
            print ('Digite apenas números')
        else:
            qtd_jogadores = int(qtd_jogadores)
        if qtd_jogadores < 2 or qtd_jogadores > 99:
            print('A quantidade de jogadores deve ser entre 2 e 99')
    return qtd_jogadores

# Monta a lista de jogadores, perguntando o nome de cada um.
def montarListaJogadores(qtd):
    jogadores = []
    for i in range(qtd):
        nome = '' # Incia nome de string vazia para entrar no while.
        repetido = False
        while len(nome) < 1 or repetido: 
            nome = input(f"Digite o nome do {i+1}o jogador: ")
            nome = nome.strip() # Remove espaços em branco.
            if len(nome) < 1: 
                print('O nome deve ter pelo menos 1 caractere.')
            elif buscaJogador(jogadores, nome): # Testa se o jogador já existe na lista com aquele nome.
                print('Nome repetido, digite novamente')
                repetido = True

        # Cria objeto jogador e o adiciona na lista.    
        jogador = Jogador (nome)
        jogadores.append (jogador)
    return jogadores

# Obtém o objeto jogador que irá iniciar o jogo pela primeira vez.
def obterJogadorInicial(jogadores):
    nome_inicial = input("Digite o nome do jogador que falou 'Cérebro' da maneira mais zumbi: ")
    nome_inicial = nome_inicial.strip() # Strip retira os espaços do começo e do final.
    jogador_inicial = buscaJogador(jogadores, nome_inicial)
    # Verifica se o jogador existe senão pergunta novamente.
    while not jogador_inicial:
        nome_inicial = input('Jogador inexistente, digite novamente: ')
        jogador_inicial = buscaJogador(jogadores, nome_inicial)
    return jogador_inicial

# Refaz a lista de jogadores deixando o jogador_inicial como o primeiro da lista.
def reordenarJogadores(jogadores, jogador_inicial):
    indice = jogadores.index(jogador_inicial) # Obtém o índice do jogador inicial na lista de jogadores.
    # Se o índice do jogador inicial for zero, não entra no if.
    if indice > 0: 
        # Cria uma nova lista do jogador inicial até o último jogador.
        inicial = jogadores[indice:len(jogadores)] 
        # Cria uma nova lista do primeiro jogador até o jogador anterior ao inicial.
        final = jogadores[0:indice]
        # Monta a primeira parte da nova lista reordenada.
        jogadores = inicial
        # Adiciona a segunda parte da lista reordenada.
        for j in final:
            jogadores.append(j)
    return jogadores

# Obtém a lista de jogadores com maior pontuação obtida.
def obterVencedores(jogadores):
    vencedores = []
    # Descobre qual a maior pontuação.
    maior_pontuacao = 0
    for j in jogadores:
        if j.cerebros > maior_pontuacao:
            maior_pontuacao = j.cerebros
    # Adiciona na lista vencedores o(s) jogador(es) com a maior pontuação.
    for j in jogadores:
        if j.cerebros == maior_pontuacao:
            vencedores.append(j)
    return vencedores

# Função para perguntas do tipo S/N.
def confirmar(mensagem):
    resposta = ''
    while resposta != 'S' and resposta != 'N':
        resposta = input(mensagem)
        resposta = resposta.upper()
    return resposta == 'S'

# Turno de um jogador
def jogarTurno(jogador):
    # incializa tubo
    tubo = Tubo()
    turno = Turno() # Cria classe para armazenar as informações do turno.
    continuar = True
    while continuar and turno.tiros < 3:
        # Joga os dados e armazena informações no objeto turno.
        turno.jogarDados(tubo)
        # Se for 3 tiros, retorna sem somar cerebros.
        if turno.tiros >= 3:
            print ("Atingiu 3 tiros, passou a vez")
            time.sleep(1)
        else:
            print(f"Você está com {turno.cerebros} cérebro(s) nesse turno, {jogador.cerebros + turno.cerebros} cérebro(s) no total, {len(turno.dadosPassos)} passo(s) e {turno.tiros} tiro(s).")
            time.sleep(1)
            continuar = confirmar("Deseja jogar mais 3 dados S/N? ")
            # Se escolheu parar, contabiliza os cérebros.
            if not continuar:
                jogador.cerebros += turno.cerebros

# Função para um jogo inteiro, até terminar, ou seja, haver um único vencedor
def jogarPartida(jogador_inicial, jogadores):
    # Reordena a lista para que o jogador inicial seja o primeiro da lista.
    jogadores = reordenarJogadores(jogadores, jogador_inicial)
    # Inicializações de variáveis.
    vencedor = None
    turno_final = False
    vencedores = []
    # Enquanto não houver um e somente um vencedor.
    while not vencedor:
        # Joga um turno para cada jogador
        for jogador in jogadores: 
            print("\nVez do jogador", jogador.nome)
            time.sleep(1)
            jogarTurno(jogador)
            print(f"{jogador.nome} está com {jogador.cerebros} cérebro(s)")
            time.sleep(1)
            # Se fez mais que 13 pontos, informa que será o turno final.
            if jogador.cerebros >= 13:
                print (f"Atingiu {jogador.cerebros} cérebros.")
                if not turno_final:
                    print("Esse será o turno final.")
                    time.sleep(1)
                    turno_final = True
        # Se é o turno final, verifica se tem somente um vencedor ou se precisará de desempate.
        if turno_final:
            # Obtém a lista de jogadores com maior pontuação obtida.
            vencedores = obterVencedores(jogadores)
            # Se só houver um vencedor, preenche o vencedor e sai.
            if len(vencedores) == 1: 
                vencedor = vencedores[0]
                print("\nO vencedor foi", vencedor.nome) 
                time.sleep(1)
            else: # Se houve vencedores empatados, atualiza a lista de jogadores com esses vencedores para jogar turno de desempate.
                jogadores = vencedores 
                print("\nHouve mais de um vencedor. São eles:")
                for v in vencedores:
                    print(v.nome)
                print("\nTurno de desempate!")
                time.sleep(1)
    # Retorna o vencedor.
    return vencedor

# Aqui começa o programa.
welcome()
# Pergunta a quantidade de jogadores.
qtd = lerQtdJogadores()
# Pergunta o nome dos jogadores e recebe a lista.
jogadores = montarListaJogadores(qtd)
# Pergunta qual jogador falou 'Cérebro' da maneira mais zumbi para começar o jogo.
jogador_inicial = obterJogadorInicial(jogadores)

# Loop principal do programa.
novo_jogo = True
while novo_jogo:
    # Executa um jogo inteiro até haver um vencedor.
    vencedor = jogarPartida(jogador_inicial, jogadores)
    # Pergunta se quer inciar um novo jogo.
    novo_jogo = confirmar('\n\nDeseja iniciar um novo jogo com os mesmos participantes S/N? ')
    # Se escolheu jogar novamente, o jogador inicial será o que venceu o último jogo.
    if novo_jogo:
        jogador_inicial = vencedor 
        reinicializarPontos(jogadores) # Zera os pontos dos jogadores.

print('\n\nFim!')