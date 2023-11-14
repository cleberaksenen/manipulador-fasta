#Função para renomear FASTAS
with open("nomes.csv") as file:
    arquivo = file.readlines()
with open("sequencias.fasta",'r') as file:
    fastas = file.readlines()
with open("sequencias_renamed.fasta", 'w') as output:
        for fasta in fastas:
            if fasta.startswith(">"): 
                for nome in arquivo[1:]:
                    if fasta.strip(">").strip("\n") == nome.split(";")[0].strip("\t"):
                        output.write(">" + nome.split(";")[1])
            else:
                output.write(fasta)

with open("sequencias_renamed.fasta", 'r') as file_outp:
    final = file_outp.readlines()

numero_inicial = int(len(fastas) / 2)
numero_final = int((len(final) / 2))
print(f"Inicio: {numero_inicial} arquivos FASTA\nFinal: {numero_final} arquivos FASTA")