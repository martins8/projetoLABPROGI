from time import time
from random import randint


# FUNÇÃO que armazena uma lista de questões e retorna um elemento da lista de acordo com o parâmetro passado,
# o qual será obtido de maneira aleatória pelo randint.
def questions(nmr):
    expressions = ['(15+5)/(1+3)',
                   '*sqrt = RAIZ QUADRADA*\n sqrt[81]',
                   '(1/3) + (2/3)',
                   '55 + 99',
                   '47 * 3',
                   'se x=2, então x+(x/2) é?',
                   '36 / 6',
                   '47 + 3 + 10 - (5 * 2)',
                   '5 / (1/2)',
                   '10 / (1/2)',
                   '*sqrt = RAIZ QUADRADA*\n sqrt[25]',
                   'se x=3 e y=4, então x * y + 5 é?',
                   'qualquer número elevado a 0 é igual a?',
                   '*sqrt =  RAIZ QUADRADA* \n sqrt[100 + 21]',
                   '(28-1) / (2+1)',
                   '((50 * 2) - 100 + 50) * 2',
                   '((47 - 2) / 5) + 25',
                   'fatorial de 3 é?',
                   '(55 + 77) * (41 + 66) * (24 - 87) * (25 - 25)']
    return print(f'\033[34m{expressions[nmr]}\033[m')


# Lista que armazena as respostas, sendo ligadas pelo mesmo indíce que as perguntas.
answers = ['5',
           '9',
           '1',
           '154',
           '141',
           '3',
           '6',
           '50',
           '10',
           '20',
           '5',
           '17',
           '1',
           '11',
           '9',
           '100',
           '34',
           '6',
           '0']


# FUNÇÃO que registra o usuário e armazena em um arquivo.
def user_register():
    global username
    print(f'\nOlá seja BEM VINDO AO QUIZ DE MATEMÁTICA, vejo que é\n'
          f'sua primeira vez nesse QUIZ. Logo, registre um '
          f'nome de\nusuário para que você consiga visualizar seu score depois.\n')
    username = str(input('USERNAME: ')).strip()


# FUNÇÃO do menu
def menu():
    print(f'{"-" * 56}\n'
          f'{" QUIZ DE MATEMÁTICA".center(56)}\n'
          f'{"-" * 56}\n'
          f'{"escolha alguma opção digitando o número referente a ela:".center(56)}\n\n'
          f' [1] INICIAR QUIZ\t\t\t\t\t[2] FINALIZAR PROGRAMA\n\n'
          f' [3] SCORES\t\t\t\t\t\t\t[4] SAIBA MAIS\n')


# FUNÇÃO da interface de escolha do usuário.
def options(number):
    if number == 1:
        print(f'QUIZ INICIADO, TENHA UMA BOA JOGATINA!\n'
              f'Responda as questõs em, no máximo, 10 segundos para obter pontuação.\n'
              f'Caso erre, perderá uma vida\n'
              f'{"-" * 56}')
        game()
    elif number == 2:
        print(f'{"-" * 56}')
        print(f'PROGRAMA FINALIZADO, VOLTE SEMPRE!\n')
        quit()
    elif number == 3:
        print(f'{"-" * 56}')
        f = open("userScores.txt", "r")
        print(f.read())
        print(f'\n[1] VOLTAR AO MENU PRINCIPAL      [2] FINALIZAR PROGRAMA')
        option3 = int(input('Sua opção: '))
        if option3 == 1:
            menu()
            your_option3 = int(input('Sua opção: '))
            print(f'{"-" * 56}')
            options(your_option3)
        else:
            print(f'QUIZ FINALIZADO, VOLTE SEMPRE!')
    elif number == 4:
        print(f'\n Esse QUIZ DE MATEMÁTICA, irá lhe desafiar com cálculos\n básicos, os quais deverão ser resolvidos em'
              f' um intervalo\n de 10 SEGUNDOS, senão, a questão será desconsiderada e\n você continuará a jogar.'
              f' Quando você acertar alguma questão\n você receberá uma pontuação e ao errar, perderá uma vida.'
              f' \n O jogador terá 2 vidas iniciais, ao perdê-las, o\n quiz será finalizado e sua pontuação será'
              f' registrada\n MECÂNICA DE JOGO IMPORTANTE: ao acertar 5 perguntas\n seguidas,'
              f' você adiciona uma vida a si mesmo.\n\n'
              f'[1] VOLTAR AO MENU PRINCIPAL      [2] FINALIZAR PROGRAMA')
        option4 = int(input('Sua opção: '))
        if option4 == 1:
            menu()
            your_option4 = int(input('Sua opção: '))
            options(your_option4)
        else:
            print(f'QUIZ FINALIZADO, VOLTE SEMPRE!')


# FUNÇÃO do quiz em si, nela estará todas as funcionalidades do quiz
def game():

    # Variáveis de vida, score e vitórias consecutivas
    score = 0
    life = 2
    win_streak = 0

    # iteração do jogo
    while life > 0:
        if win_streak == 5:
            life += 1
            win_streak -= 5

        # variável de medição de tempo, e a váriavel indice que servirá para trazer uma questão aleatória e, também,
        # dizer se a resposta dada condiz com a resposta do indíce da lista answers.
        start = time()
        indice = randint(0, 18)
        print(f'\033[32mVIDAS: {life}        ACERTOS CONSECUTIVOS: {win_streak}\033[m')
        questions(indice)
        your_answer = str(input('Sua resposta: ')).strip()

        # Condicional do acerto/erro do usuário
        if your_answer == answers[indice]:
            end = time()
            if end - start > 10:
                print(f'\nVocê acertou a questão, porém, ultrapassou o limite de tempo. Logo você\n '
                      f'não será pontuado por essa questão'
                      f'\n Seu tempo de resposta: {end - start:.2f} segundos.')
                print(f'{"-" * 56}')
                win_streak -= win_streak
            elif end - start < 10:
                print(f'\nParabéns, você acertou a questão!\n')
                score += 1
                win_streak += 1
                print(f'{"-" * 56}')
        elif your_answer != answers[indice]:
            print(f'\nInfelizmente, você errou :(!\n')
            print(f'{"-" * 56}')
            life -= 1
            win_streak -= win_streak

    f = open("userScores.txt", "a")
    f.write(f'{username} - {score}\n')
    f.close()

    menu()
    your_option_game = int(input('Sua opção: '))
    options(your_option_game)
