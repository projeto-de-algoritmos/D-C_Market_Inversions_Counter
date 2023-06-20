import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# separar por datas 
# parametriza pela alta do preço 
# fazer calculo de correlação

dfABEV3 = pd.read_csv('abev3.csv')
dfBBAS3 = pd.read_csv('bbas3.csv')
dfBBDC4 = pd.read_csv('bbdc4.csv')
dfB3SA3 = pd.read_csv('b3sa3.csv')
dfITUB4 = pd.read_csv('itub4.csv')
dfIREN3 = pd.read_csv('lren3.csv')  
dfMGLU3 = pd.read_csv('mglu3.csv')
dfNTCO3 = pd.read_csv('ntco3.csv')
dfPETR4 = pd.read_csv('petr4.csv')
dfVALE3 = pd.read_csv('vale3.csv')


# encontrar menor data conjunta
dfABEV3[['datetime']] = dfABEV3[['datetime']].apply(pd.to_datetime)

menorData = dfABEV3["datetime"].iloc[0]
maiorData = dfABEV3["datetime"].iloc[-1]

menorPreco = dfABEV3['close'].min()
maiorPreco = dfABEV3['close'].max()


dataList = dfBBAS3['close'].to_list()

# aplicar algoritmo aqui
# contar inversões 

# def merge():


def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        # merge()
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


mergeSort(dataList)

# print(dataList)
# Criar figura e eixos
fig, ax = plt.subplots()

# Plotar os dados
ax.plot(range(len(dataList)), dataList, label='VALE5')
ax.plot(range(len(dataList)), dfBBAS3['close'].to_list(), label='VALE5')


# Mostrar os rótulos dos eixos e a legenda do gráfico
ax.set_xlabel('Dia')
ax.set_ylabel('Preço (R$)')
ax.legend()

# Exibir o gráfico pronto
# plt.show()


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        opcao_selecionada = request.form['opcao']
        # Faça algo com a opção selecionada
        return print({'mensagem': f"A opção selecionada foi: {opcao_selecionada}"})
    return render_template('index.html')

@app.route('/selecionar', methods=['POST'])
def processar():
    
    opcao_selecionada = request.form['opcao']
    # Faça algo com a opção selecionada
    return print(f"A opção selecionada foi: {opcao_selecionada}")


if __name__ == '__main__':
    # gerar_grafico()  # Gerar o gráfico antes de iniciar o aplicativo
    app.run()