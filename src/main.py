from controle_musica import Requisicao
import sys


def finalizar():
    sys.exit()

def menu():
    requisicao = Requisicao()
    
    
    opcoes = {
        "1": lambda: requisicao.mostrar_status(),
        "2": lambda: requisicao.pausar(),
        "3": lambda: requisicao.continuar(),
        "4": lambda: requisicao.proxima(),
        "5": lambda: requisicao.anterior(),
        "6": lambda: requisicao.buscar_musica(),
        "0": finalizar,
    }
    while True:
        print("\n=== Spotify CLI ===")
        print("1 - Mostrar música atual")
        print("2 - Pausar")
        print("3 - Continuar")
        print("4 - Próxima música")
        print("5 - Música anterior")
        print("6 - Buscar e tocar música")
        print("0 - Sair")
        escolha = input("Escolha: ")

        if escolha in opcoes:
            opcoes[escolha]()
            
            
if __name__ == "__main__":
    menu()
