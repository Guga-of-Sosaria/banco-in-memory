from src.io.input_parse import load_input
from src.io.output_writer import write_output
import json

#Teste 1: input básico
def teste_basico():
    #Carrega os conteúdos do json contendo o output esperado
    output_esperado = []
    with open(r"../data/output_esperado_basico.json", encoding="utf-8") as f:
        output_esperado = json.load(f)
    
    #realiza o teste
    write_output("../data/output_basico.json", load_input("..data/input_basico.json"))

    #carrega o conteúdo do json contendo o output gerado no teste
    output_gerado = []
    with open(r"../data/output_basico.json", encoding="utf-8") as f:
        output_gerado = json.load(f)

    #Compara os dois outputs
    assert output_gerado == output_esperado

#Teste 2: input avançado
def teste_avancado():
    #Carrega os conteúdos do json contendo o output esperado
    output_esperado = []
    with open(r"../data/output_esperado_avancado.json", encoding="utf-8") as f:
        output_esperado = json.load(f)
    
    #realiza o teste
    write_output("../data/output_avancado.json", load_input("..data/input_avancado.json"))

    #carrega o conteúdo do json contendo o output gerado no teste
    output_gerado = []
    with open(r"../data/output_avancado.json", encoding="utf-8") as f:
        output_gerado = json.load(f)

    #Compara os dois outputs
    assert output_gerado == output_esperado

#Teste 3: input de estresse
def teste_estresse():
    #Carrega os conteúdos do json contendo o conteúdo esperado
    output_esperado = []
    with open(r"../data/output_esperado_estresse.json", encoding= "utf-8") as f:
        output_esperado = json.load(f)

    #Realiza o teste
    write_output("...data/output_estresse.json", load_input("..data/input_estresse.json"))

    #Carrega o conteúdo do json contendo o output gerado no teste
    with open(r"../data/output_estresse.json", encoding="utf-8") as f:
        output_gerado = json.load(f)

    #Compara os dois outputs
    assert output_gerado == output_esperado