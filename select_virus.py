#Função para selecionar FASTAS
with open("nomes.csv") as file:
    arquivo = file.readlines()
with open("sequencias.fasta",'r') as inp:
    fastas = inp.readlines()
with open("sequencias_select.fasta", 'w') as output:
    for idx,fasta in enumerate(fastas):
        for nome in arquivo:
            if fasta.strip(">").strip("\n") == nome.strip("\n"):
                output.write(">" + nome)
                output.write(fastas[idx+1])
    with open("sequencias_select.fasta", 'r') as file_outp:
        final = file_outp.readlines()

numero_inicial = int(len(fastas) / 2)
numero_final = int((len(final) / 2))

print(f"Inicio: {numero_inicial} arquivos FASTA\nFinal: {numero_final} arquivos FASTA")