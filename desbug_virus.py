#Função para arrumar FASTAS
with open("sequencias.fasta",'r') as file:
    fastas = file.readlines()
with open("sequencias_desbug.fasta", 'w') as output:
    for fasta in fastas:
        if fasta.startswith(">"):
            output.write("\n" + fasta)
        else:
            output.write(fasta.strip("\n"))

with open("sequencias_desbug.fasta", 'r') as file_outp:
    final = file_outp.readlines()

numero_inicial = int(len(fastas) / 2)
numero_final = int((len(final) / 2) - 0.5)
print(f"Inicio: {numero_inicial} arquivos FASTA\nFinal: {numero_final} arquivos FASTA")