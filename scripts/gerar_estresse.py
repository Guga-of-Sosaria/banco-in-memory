from json import dump
from random import randint, sample

#Guardará as operações criadas
operations = []
#Serve para criar números aleatórios para as operações insert
samples = sample(range(100000), 100000)

print("Criando inputs para teste de estresse...")

#Cria algumas operações INSERT
for i in range(100000):
    operations.append({ "op": "INSERT", "key":samples[i], "value": str(samples[i]) })

#Cria algumas operações RANGE
for i in range(5000):
    #Acho que até 5000 já deve ser um número alto bom
    a = randint(1, 5000)
    b = randint(1, 5000)
    operations.append({ "op": "RANGE", "min": min(a,b), "max": max(a,b) })

#Escreve as operações criadas no arquivo JSON
with open(r'../data/input_estresse.json', 'w', encoding="utf-8") as file:
    dump({"operations":operations}, file, ensure_ascii=False, indent=2)

print("Inputs criados com sucesso! Bom teste! :)")
