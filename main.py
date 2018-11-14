import requests
from modelo.pais import Pais

paises = {}

def getPais(nome):
    if not (nome in paises):
        pais = Pais(nome)
        paises[nome]=pais
    return paises[nome]
        

def getIndicador(indicador,nome=''):
    print("Get indicador: "+indicador)
    url = 'http://api.worldbank.org/v2/countries/all/indicators/'+indicador+'?date=2015:2015&per_page=400&format=json'
    response = requests.get(url)
    dados = response.json()[1]

    for dado in dados:
        pais = getPais(dado['country']['value'])
        
        chave = nome
        if not nome:
            chave = dado['indicator']['value']
            
        pais.dados[chave]=dado['value']

        
def lerArquivo(nomeArquivo='indicadores.txt'):
    with open(nomeArquivo, 'r') as arquivo:  
        linha = arquivo.readline()   
        while linha:
            if '=' in linha:
                (codigo,nome) = linha.strip().split('=')
            else:
                codigo = linha.strip()
                nome = ''
            getIndicador(codigo,nome)
            linha = arquivo.readline()

def salvarArquivo(csvString, nomeArquivo='dados.csv'):
    with open(nomeArquivo, 'w') as arquivo:  
        arquivo.write(csvString)

def toCsvString():
    chave = list(paises.keys())[0]
    tail = ";".join(paises[chave].dados.keys())
    csvString = 'Country; '+tail
    #print(csvString)
    for k,pais in paises.items():        
        lista = []
        lista.append(pais.nome)
        for k, v in pais.dados.items():
            valor = str(v)
            if v is None:
                valor = ""
            lista.append(valor)
        #print(";".join(lista))
        csvString = csvString + "\n" + ";".join(lista)
    return csvString


def executar():
    lerArquivo('indicadores_novo.txt')
    csv = toCsvString()
    #print(csv)
    salvarArquivo(csv)


if __name__ == '__main__':
    executar()
    