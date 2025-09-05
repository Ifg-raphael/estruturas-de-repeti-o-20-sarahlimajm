# Sua solução aqui
#Importação da biblioteca intertools para a utilização da função "count".
import itertools
#Definição das constantes e da variável, sendo esta "Float", pois as entradas poderam ser valores fracionários.
massa_inicial = float(input(" "))
MEIO_PERIODO = 50
massa = massa_inicial
tempo_segundos = 0
#Utlização da estrutura de repetição "For", juntamente com a função "count" que cria um contador infinito, gerando uma sequência de números começando de um valor inicial e incrementando de um em um. 
for i in itertools.count():
#Determinação de uma condição para que o programa/ laço se encerre.    
    if massa < 0.5:
         break
#Caso a condição acima não for satisfeita a variável "massa" será atribuida à massa e dividida por dois.   
    else:
        massa /= 2
    tempo_segundos += MEIO_PERIODO
#Transformação das unidades de tempo.
horas = tempo_segundos // 3600
minutos = (tempo_segundos % 3600) // 60
segundos = tempo_segundos % 60
#Imprime o valor do tempo.
print(f"Tempo decorrido: {horas} h {minutos} m {segundos} s")
