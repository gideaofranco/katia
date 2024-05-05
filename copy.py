import csv
with open('twitter-100-linhas.csv', 'r') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
        mylen=len(linha[7])
        mycount=linha[7].count(" ") + 1
        print(f"tamanho: {mylen}, palavras: {mycount}")
