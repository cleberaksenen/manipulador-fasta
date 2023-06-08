from colorama import Fore, Style

#Função para selecionar FASTAS
def select_virus(planilha='input.csv', input='sequencias.fasta'):
    with open(planilha) as file:
        arquivo = file.readlines()
    with open(input,'r') as inp:
        fastas = inp.readlines()
    output = "select_" + input
    with open(output, 'w') as outp:
        for idx,fasta in enumerate(fastas):
            for nome in arquivo:
                if fasta.strip(">").strip("\n") == nome.strip("\n"):
                    outp.write(">" + nome)
                    outp.write(fastas[idx+1])
    with open(output, 'r') as file_outp:
        final = file_outp.readlines()

    numero_inicial = int(len(fastas) / 2)
    numero_inicial_azul = Style.BRIGHT + Fore.BLUE + str(numero_inicial) + Style.RESET_ALL
    numero_final = int((len(final) / 2))
    numero_final_azul = Style.BRIGHT + Fore.BLUE + str(numero_final) + Style.RESET_ALL

    print(f"Inicio: {numero_inicial_azul} arquivos FASTA\nFinal: {numero_final_azul} arquivos FASTA")

#----------------------------------------------------
#Função para renomear FASTAS
def rename_virus(planilha='input.csv', input='sequencias.fasta'):
    with open(planilha) as file:
        arquivo = file.readlines()
        for nome in arquivo[1:]:
            nome.split(";")

    with open(input,'r') as file:
        fastas = file.readlines()

    output = "renamed_" + input
    with open(output, 'w') as outp:
        for c in fastas:
            if c.startswith(">"): 
                for nome in arquivo[1:]:
                    if c.strip(">").strip("\n") == nome.split(";")[0].strip("\t"):
                        outp.write(">" + nome.split(";")[1])
            else:
                output.write(c)

    with open(output, 'r') as file_outp:
        final = file_outp.readlines()

    numero_inicial = int(len(fastas) / 2)
    numero_inicial_azul = Style.BRIGHT + Fore.BLUE + str(numero_inicial) + Style.RESET_ALL
    numero_final = int((len(final) / 2))
    numero_final_azul = Style.BRIGHT + Fore.BLUE + str(numero_final) + Style.RESET_ALL

    print(f"Inicio: {numero_inicial_azul} arquivos FASTA\nFinal: {numero_final_azul} arquivos FASTA")
#----------------------------------------------------
#Função para arrumar FASTAS
def desbug_virus(input='sequencias.fasta'):
    with open(input,'r') as file:
        fastas = file.readlines()

    output = "desbug_" + input
    with open(output, 'w') as outp:
        for fasta in fastas:
            if fasta.startswith(">"):
                outp.write("\n" + fasta)
            else:
                outp.write(fasta.strip("\n"))

    with open(output, 'r') as file_outp:
        final = file_outp.readlines()

    numero_inicial = int(len(fastas) / 2)
    numero_inicial_azul = Style.BRIGHT + Fore.BLUE + str(numero_inicial) + Style.RESET_ALL
    numero_final = int((len(final) / 2) - 0.5)
    numero_final_azul = Style.BRIGHT + Fore.BLUE + str(numero_final) + Style.RESET_ALL

    print(f"Inicio: {numero_inicial_azul} arquivos FASTA\nFinal: {numero_final_azul} arquivos FASTA")

