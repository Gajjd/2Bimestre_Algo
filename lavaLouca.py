import time

ligado = False
temperatura = 0
tempo = 0

def ligar(novoTempo, novaTemperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado = True 
        tempo = novoTempo
        temperatura = novaTemperatura
        print(f"Lava louças ligada por {tempo} segundos na temperatura {temperatura} °C")
        iniciarCronometro(tempo)
        desligar()
    else:
        print("Lava louças já está ligada")
           
def desligar():
    global ligado
    if ligado: 
        ligado = False
        print("Lava louças desligada")
    else:
        print("Lava louças já está desligada")

def iniciarCronometro(segundos):
    while segundos >= 0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1
    print("\n Tempo esgotado")
        
# Predefinições do microondas:

def vidro():
    ligar(120, 100)
    
def plastico():
    ligar(60, 21)
    
def metal():
    ligar(120, 30)
        
# Rodar a função:
sair = False
while sair == False:
    opcao = input("Escolha uma funcao (vidro, plastico, metal): ").lower()
    
    if opcao =="vidro":
        vidro()
    elif opcao =="plastico":
        plastico()      
    elif opcao =="metal":
        metal()     
    else:
        print("Escreva uma das opções exatamente como está no texto a cima")
    
    opcaoSair = input("Deseja sair? (1 = Sim) (Qualquer tecla = Não): ")
    if opcaoSair == "1":
        sair == True
    