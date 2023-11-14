from algoritmos import select_virus, rename_virus, desbug_virus
from colorama import Fore, Style


espaco = Style.BRIGHT + Fore.BLUE + "#######################" + Style.RESET_ALL
imagem = Style.BRIGHT + Fore.BLUE + ("░░█▀▀░█▀█░█▀▀░▀█▀░█▀█░░\n"
                                     "░░█▀▀░█▀█░▀▀█░░█░░█▀█░░\n"
                                     "░░▀░░░▀░▀░▀▀▀░░▀░░▀░▀░░") + Style.RESET_ALL 
print(espaco)
print(imagem)
print(espaco)
#--------------------------------------------------------------------------------------------

planilha = str(input("Digite o arquivo .csv com o nome das sequências (ex. planilha.csv): "))
entrada = str(input("Digite o arquivo fasta (ex. sequencias.fasta): "))


decisao = str(input("O que você deseja fazer?\n[1]Selecionar FASTAS\n[2]Renomear FASTAS\n[3]Arrumar FASTAS\nDigite o que deseja fazer: "))

while True:
    if decisao == "1":
        select_virus(planilha=planilha, input=entrada)
        break
    elif decisao == "2":
        rename_virus(planilha=planilha, input=entrada)
        break
    elif decisao == "3":
        desbug_virus(planilha=planilha, input=entrada)
        break
    else:
        break
    


