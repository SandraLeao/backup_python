# Jogo da Forca
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.palavraSecreta = word
        # print('Palavra secreta: ' + self.palavraSecreta + ' ' + str(len(self.palavraSecreta)))
        self.palavraFormada = []
        self.palavraFormadaString = ''
        for i in range(0, len(self.palavraSecreta)):
            self.palavraFormada.append('_')
            # self.palavraFormadaString = self.palavraFormadaString + '_'
        # print('Palavra formada string: ' + self.palavraFormadaString + ' ' + str(len(self.palavraFormadaString)))

        self.letrasErradas = 0

    # Método para adivinhar a letra
    # def guess(self, letter):

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.letrasErradas >= 6 or self.hangman_won() == True:
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if str(self.palavraFormadaString) == self.palavraSecreta:
            return True
        else:
            return False

    # Método para não mostrar a letra no board
    # def hide_word(self):

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        if self.letrasErradas <= 6:
            print(board[self.letrasErradas])
        if len(self.palavraFormadaString) == 0:
            esbocoPalavra = ''
            for i in range(0, len(self.palavraSecreta)):
                esbocoPalavra = esbocoPalavra + '_'
            print(esbocoPalavra)
        else:
            print(self.palavraFormadaString)


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    try:
        with open("palavras.txt", "rt") as f:
            bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip().upper()
    except:
        # retornar uma palavra default para o jogo iniciar
        return 'ESPONJA'


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        # Verifica o status do jogo
        game.print_game_status()
        letra = input("Informe uma letra: ").upper()
        encontrouLetra = False
        for indice, valor in enumerate(game.palavraSecreta):
            if valor == letra:
                game.palavraFormada[indice] = letra
                encontrouLetra = True
        if not encontrouLetra:
            game.letrasErradas += 1
        game.palavraFormadaString = ''
        for i in game.palavraFormada:
            game.palavraFormadaString = game.palavraFormadaString + i

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        game.print_game_status()
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavraSecreta)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
