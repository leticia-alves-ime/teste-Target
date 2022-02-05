
########### TESTE TARGET  #####################

# 2

# Sequência de Fibonacci


valor = int(input("Digite um valor e veremos se ele está na sequência de Fibonacci "))



    # Calculando a sequência

sequencia = [0, 1]

i = 1
while sequencia[i] < valor:
    elemento = sequencia[i] + sequencia[i-1]
    sequencia.append(elemento)
    i += 1
print(sequencia)

if valor in sequencia:
    print(f'O valor {valor}, pertence à sequência.')
else:
    print(f'O valor {valor}, não pertence à sequência.')
    
    
    
# 3 

# Faturamento anual    
    
import json
import numpy as np
arquivo = open('Dados_faturamento.json', 'r')
data = json.load(arquivo)


FAT_ANU = np.array(data)
FAT_LIQ = FAT_ANU.copy()

for j in range(len(FAT_ANU)):
    FAT_LIQ = np.setdiff1d(FAT_LIQ,0)


media = np.mean(FAT_LIQ)
menor = min(FAT_ANU)
maior = max(FAT_ANU)

sup = 0

for fatu in FAT_ANU:
    if fatu > media: sup += 1

print(f"Menor valor: {menor}, Maior valor {maior}, Quantidade de dias em que o faturamento diario foi superior a media anual :{sup}")



# 4

# Faturamento mensal

faturamento = dict(SP=67836.43, RJ=36678.66, MG=29229.88, ES=27165.48, Outros=19849.53)

total = sum(faturamento.values()) # Somar todos os valores

for valor in faturamento:
    percentual = ((faturamento[valor])/total)*100
    print(f"O percentual de contribuição de {valor} foi de {percentual:.2f}%")
        
        
        
# 5 inverter palavra

string = input(str("Digite uma palavra: "))
n = len(string)
stringR = string[n-1]

for i in range(n-2,-1,-1):
    stringR = stringR + string[i]
print(stringR)








        
        
        
        