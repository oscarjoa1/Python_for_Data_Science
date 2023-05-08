
# import
import random
from os import name, system

# 1. funcao para limpar a cada execucao
def limpa_tela():
    
    #window
    if name == "nt":
        _=system("cls")   # descartar o resultado da funcao executada no shell do system uma vez executada
       
    # Mac ou linux
    else:
        _= sytem("clear") # descartar o resultado da funcao executada no shell do system uma vez executada


# 2. funcao game
def game():
    
    limpa_tela()
    
    print("\n Bem-vindo(a) ao jogo da forca")
    print("Adivinhe a palavra a baixo: \n")
    
    # lista de palavras
    palavra = ["banana", "Morango", "melancia", "garrafa", "livro", "arcoiris", "natureza", "limao"]
    
    # escolher a palavra de forma aleatória
    palavra = random.choice(palavra)
    
    # lista comprehension
    letras_descobertas = ["_" for letra in palavra]
    
    #numero de chances
    chances = 10
    
    # listas erradas
    letras_erradas = []
    
    # loops
    
    for t in list(range(0, chances)):
    
        #print inicial do games
        print("".join(letras_descobertas))
        print("\nChances restantes", (chances - t))
        print("Letras erradas:", ".join(letras_erradas)")
        
        # tentativas
        tentativa = input("\nDigite uma letra:").lower()
        
        # Condicional
        if tentativa in palavra:
            index = 0 
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = tentativa
                index += 1
                
        # condicional
        if "_" not in letras_descobertas:
            print("\nVocê Venceu, a palavra era:", palavra)
            break
            
    # condicional
    if "_" in letras_descobertas:
        print("\n Vocês Perdeu a palavra era:", palavra)
  
# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns você está aprendendo a programar em Python. :)")
    
    
    
        
        
        
        
    
    