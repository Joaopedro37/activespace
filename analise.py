import re
import matplotlib.pyplot as plt
import numpy as np 


''' função para lista de valores de CPM médio no tempo de intervalo definido'''
def lista_cpm(lista, intervalo):

    minutos = 0
    cpm_medio = []
    valor = 0
    n_pulsos = 0
    
    for num in lista:
        n_pulsos += 1
        if num <= minutos + intervalo:
            valor += 1
            
        
        else:
            cpm_medio.append(valor/intervalo)
            while num - minutos > intervalo*2:
                cpm_medio.append(0)
                minutos += intervalo
            
            valor = 1
            minutos += intervalo
        
           
    cpm_medio.append(valor/intervalo)
    
    
    return cpm_medio



'''     Função que retorna um gráfico dos valores de CPM médio em intervalos de
     tempo definidos em função do tempo de medição em horas'''
     
def grafico_cpm(lista, intervalo, cor):

    tempo = []
    i = intervalo

    for w in lista:
        tempo.append(i)
        i += intervalo
        
    

    plt.figure(dpi=200)

    plt.plot(minutos_horas(tempo), lista, cor +'.--')


    plt.title("CPM médio de cada intervalo de " + str(intervalo) + " min em função do tempo de medição\n")
    plt.xlabel("Tempo (horas)")
    plt.ylabel("CPM médio")


    plt.xticks(np.arange(0, minutos_horas(tempo)[-1]+0.5 , 1), minor=False)
    plt.xticks(np.arange(0, minutos_horas(tempo)[-1]+0.5 , 1/(60/intervalo)), minor=True)


    plt.grid(True)
    plt.show()
    
    
    
'''     Função que faz um gráfico dos valores de CPM médio em intervalos de
     tempo definidos em função do tempo de medição em minutos'''
    
def grafico_cpm_minutos(lista, intervalo, cor):

    tempo = []
    i = intervalo

    for w in lista:
        tempo.append(i)
        i += intervalo
        
    

    plt.figure(dpi=200)

    plt.plot(tempo, lista, cor +'.--')


    plt.title("CPM médio de cada intervalo de " + str(intervalo) + " min em função do tempo de medição\n")
    plt.xlabel("Tempo (minutos)")
    plt.ylabel("CPM médio")


    plt.xticks(np.arange(0, tempo[-1]+30 , 10), minor=False)
    plt.xticks(np.arange(0, tempo[-1]+30 , intervalo), minor=True)


    plt.grid(True)
    plt.show()
    
    
    
'''     Função que retorna dois gráficos em forma de subplot dos valores de CPM médio em intervalos de
     tempo definidos em função do tempo de medição em horas para cada medição'''
    
def grafico_subplot(lista1, lista2, intervalo, cor):

    tempo1 = []
    i = intervalo

    for w in lista1:
        tempo1.append(i)
        i += intervalo
        
    tempo2 = []
    u = intervalo

    for z in lista2:
        tempo2.append(u)
        u += intervalo
        
    

    plt.figure(dpi=200)
    
    # Primeiro gráfico (2 linhas, 1 coluna, gráfico 1)
    plt.subplot(2, 1, 1)
    plt.plot(minutos_horas(tempo1), lista1, cor +'.--')
    plt.title("CPM médio de cada intervalo de " + str(intervalo) + " min em função do tempo de medição\n")
    plt.xlabel("Tempo (horas)")
    plt.ylabel("CPM médio")
    plt.xticks(np.arange(0, minutos_horas(tempo1)[-1]+0.5 , 1), minor=False)
    plt.xticks(np.arange(0, minutos_horas(tempo1)[-1]+0.5 , 1/(60/intervalo)), minor=True)
    
    plt.grid(True)
    
    
    # Segundo gráfico (2 linhas, 1 coluna, gráfico 2)
    plt.subplot(2, 1, 2)
    plt.plot(minutos_horas(tempo2), lista2, cor +'.--')
    plt.title("\n\nCPM médio de cada intervalo de " + str(intervalo) + " min em função do tempo de medição\n")
    plt.xlabel("Tempo (horas)")
    plt.ylabel("CPM médio")
    plt.xticks(np.arange(0, minutos_horas(tempo2)[-1]+0.5 , 1), minor=False)
    plt.xticks(np.arange(0, minutos_horas(tempo2)[-1]+0.5 , 1/(60/intervalo)), minor=True)
    
    plt.grid(True)
    
    # Mostra os gráficos
    
    plt.tight_layout()  # Ajusta o espaçamento entre os gráficos
    plt.show()

'''Função que retorna um gráfico dos pulsos detetados em função do tempo de medição em horas'''
    
def grafico_pulsos(lista):
   
    pulsos = []

    for i in lista:
        pulsos.append(1)
        
    tempo_pulsos_horas = minutos_horas(lista)

    plt.figure(dpi=200)

    plt.plot(tempo_pulsos_horas, pulsos, 'r.')


    plt.title("Pulsos detetados em função do tempo, em horas,\n durante a contagem\n")
    plt.xlabel("Tempo (horas)")
    plt.ylabel("Pulsos")

    plt.yticks([0, 1])
    plt.xticks(np.arange(0, tempo_pulsos_horas[-1]+0.5, 1), minor=False)
    plt.xticks(np.arange(0, tempo_pulsos_horas[-1]+0.5, 1/12), minor=True)


    plt.grid(True)
    plt.show()
    



'''Função que retorna um gráfico dos pulsos detetados em função do tempo de medição em minutos'''
def grafico_pulsos_minutos(lista):
   
    pulsos = []

    for i in lista:
        pulsos.append(1)


    plt.figure(dpi=200)

    plt.plot(lista, pulsos, 'r.')


    plt.title("Pulsos detetados em função do tempo, em minutos,\n durante a contagem\n")
    plt.xlabel("Tempo (minutos)")
    plt.ylabel("Pulsos")

    plt.yticks([0, 1])
    plt.xticks(np.arange(0, lista[-1]+30, 10), minor=False)
    plt.xticks(np.arange(0, lista[-1]+30, 1), minor=True)


    plt.grid(True)
    plt.show()
    
    
    

'''Função que retorna dois gráficos em forma de subplot
 dos pulsos detetados em função do tempo de medição em minutos'''    
def subplot_pulsos(lista1, lista2):
   
    pulsos1 = []

    for i in lista1:
        pulsos1.append(1)
        
    
    pulsos2 = []

    for i in lista2:
        pulsos2.append(1)
        

    plt.figure(dpi=200)

    # Primeiro gráfico (2 linhas, 1 coluna, gráfico 1)
    plt.subplot(2, 1, 1)
    plt.plot(lista1, pulsos1, 'r.')
    plt.title("Pulsos detetados em função do tempo, em minutos\n")
    plt.xlabel("Tempo (minutos)")
    plt.ylabel("Pulsos")
    plt.xticks(np.arange(0, lista1[-1]+30 , 60), minor=False)
    plt.xticks(np.arange(0, lista1[-1]+30 , 10), minor=True)
    plt.yticks([0, 1])
    plt.grid(True)
    
    
    # Segundo gráfico (2 linhas, 1 coluna, gráfico 2)
    plt.subplot(2, 1, 2)
    plt.plot(lista2, pulsos2, 'r.')
    plt.title("\n\nPulsos detetados em função do tempo, em minutos\n")
    plt.xlabel("Tempo (minutos)")
    plt.ylabel("Pulsos")
    plt.xticks(np.arange(0, lista2[-1]+30 , 10), minor=False)

    plt.yticks([0, 1])
    plt.grid(True)
    
    # Mostra os gráficos
    
    plt.tight_layout()  # Ajusta o espaçamento entre os gráficos
    plt.show()
    
    
    

'''Função que calcula o valor da dose de radiação em uSv/h.
    . Se quiser obter o valor de dose médio de toda a medição, 
    é só meter 0 no intervalo, no tempo_total e no valor_cpm.
    . Se quiser obter o valor de dose médio de toda a medição tendo sabendo quanto tempo é que levou a medição,
    tem que se meter 0 no intervalo e no valor_cpm.
    . Se quiser obter o valor de dose médio a partir do valor do médio de CPM da lista de valores de 
    CPM em intervalos de tempo conhecidos, tem de colocar 0 no valor_cpm e indicar o intervalo de tempo em
    que cada valor de CPM é determinado.
    . Se quiser determinar o valor de dose através de um valor de CPM conhecido é só indicar o valor de CPM.'''
def calcular_dose(lista, intervalo, tempo_total, valor_cpm):
    
    cpm = 0
    dose = 0
    
    if intervalo == 0 and tempo_total == 0 and valor_cpm == 0:
        cpm = len(lista)/lista[-1]
    elif intervalo == 0 and tempo_total != 0 and valor_cpm == 0:
        cpm = len(lista)/tempo_total
    elif valor_cpm != 0:
        cpm = valor_cpm
    elif intervalo != 0 and valor_cpm == 0: 
        for i in lista_cpm(lista, intervalo):
            cpm += i
            cpm = cpm/len(lista_cpm(lista, intervalo))
        
    dose = 2*10**(-21)*cpm**5-7*10**(-16)*cpm**4+8*10**(-11)*cpm**3-3*10**(-6)*cpm**2+0.2243*cpm
    
    return dose
    



'''Função que transforma uma lista de números em minutos para uma lista de números em horas'''
def minutos_horas(lista):
    
    horas = []
    
    for i in lista:
        horas.append(i/60)
    
    return horas


''' Função para ler os dados do arquivo e filtrar apenas valores numéricos'''
def ler_dados(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        dados = file.readlines()
    
    lista_dados = []
    for linha in dados:
        linha = linha.strip()  # Remove espaços em branco
        numeros = re.findall(r'\d+\.\d+|\d+', linha)  # Encontra todos os números na linha
        for numero in numeros:
            lista_dados.append(float(numero))
    return lista_dados

''' Função para ler os dados do arquivo e filtrar apenas valores numéricos (microsegundos)'''
def ler_dados_micros(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        dados = file.readlines()
    
    lista_dados = []
    lista_debounce = []

    
    for linha in dados:
        linha = linha.strip()  # Remove espaços em branco
        numeros = re.findall(r'\d+\.\d+|\d+', linha)  # Encontra todos os números na linha
        for numero in numeros:
            lista_dados.append(float(numero))      
            
    num_anterior = lista_dados[0]
    lista_debounce.append(num_anterior/60000000)        
    for num in lista_dados[1:]:
        if num - num_anterior > 100.00:
            lista_debounce.append(num/60000000)
            
        
        num_anterior = num
    
    
    return lista_debounce


dados_ficheiro1 = ler_dados('teste_dia2.txt')

dados_ficheiro2 = ler_dados('teste_dia_inteiro.txt')

dados_ficheiro3 = ler_dados('sala_betao_1.txt')

dados_ficheiro4 = ler_dados('sala_betao_2.txt')

dados_ficheiro5 = ler_dados('teste_caixa.txt')

dados_ficheiro6 = ler_dados('pecas_17h.txt')

tempo_pulsos6 = []

for i in dados_ficheiro6:
    if i > 900.00:
        tempo_pulsos6.append(i)
        
dados_ficheiro7 = ler_dados_micros('dentista_micros_analise.txt')    
    







grafico_cpm_minutos(lista_cpm(dados_ficheiro7, 5), 5, 'r')

