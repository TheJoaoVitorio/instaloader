import instaloader
import os
from colorama import Fore, Style, init

init()

def menu():
    while True:
        try:
            print('O que deseja?\n1 - Baixar fotos do Instagram\n2 - Sair')
            op = int(input('-> '))
            clear_terminal()

            if op in [1, 2]:
                return op
            else:
                print("Escolha inválida. Por favor, digite 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux e macOS
        os.system('clear')
    

def instaDownload(L,nomePerfil):
    try:
        perfil = instaloader.Profile.from_username(L.context, nomePerfil)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"O perfil '{nomePerfil}' não foi encontrado. ")
        exit()
        

    for post in perfil.get_posts():
        if post.typename == 'GraphImage':
            L.download_post(post, target=nomePerfil)
            print(f"Baixando: {post.url} ")
    print('Download  concluido. ')


def instaLoad():
    print(' ')
    print(Fore.MAGENTA+"""\
ooooo ooooo      ooo  .oooooo..o ooooooooooooo       .o.       ooooo          .oooooo.         .o.       oooooooooo.   oooooooooooo ooooooooo.   
`888' `888b.     `8' d8P'    `Y8 8'   888   `8      .888.      `888'         d8P'  `Y8b       .888.      `888'   `Y8b  `888'     `8 `888   `Y88. 
 888   8 `88b.    8  Y88bo.           888          .8"888.      888         888      888     .8"888.      888      888  888          888   .d88' 
 888   8   `88b.  8   `"Y8888o.       888         .8' `888.     888         888      888    .8' `888.     888      888  888oooo8     888ooo88P'  
 888   8     `88b.8       `"Y88b      888        .88ooo8888.    888         888      888   .88ooo8888.    888      888  888    "     888`88b.    
 888   8       `888  oo     .d8P      888       .8'     `888.   888       o `88b    d88'  .8'     `888.   888     d88'  888       o  888  `88b.  
o888o o8o        `8  8""88888P'      o888o     o88o     o8888o o888ooooood8  `Y8bood8P'  o88o     o8888o o888bood8P'   o888ooooood8 o888o  o888o 
                                                                                                                                                 
                                                                                                                                                 
                                                                                                                                                 """)

    opcao = menu()

    while opcao != 2:
        L = instaloader.Instaloader()

        nomePerfil = input('Digite o nome do perfil: ')
        instaDownload(L,nomePerfil)
        opcao = menu()
    

instaLoad()