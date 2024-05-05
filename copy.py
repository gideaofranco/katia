import csv
with open('twitter-100-linhas.csv', 'r') as ficheiro:
    reader = csv.reader(ficheiro)
    for linha in reader:
        print(linha)
