#importação das bibliotecas necessárias
from audioop import rms
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

#leitura do arquivo de áudio e cálculo do intervalo de amostragem
xt, fs = sf.read('waterpump.wav')
xt = xt[:,0]
t = np.linspace(0,(len(xt)-1)/fs,len(xt))  #vetor temporal

print('A frequência de amostragem é de ' + str(fs) +' Hertz.')
print('O período de amostragem é de '+ str(1/fs) +' segundos.')

#Cálculo do valor médio, RMS, e nível do sinal
xm = np.mean(xt)
xRMS = np.sqrt(np.mean(xt**2))
Lxt = 20*np.log10(xRMS/1)

print('O valor médio do sinal é ' + str(np.round(xm,4)) + '.')
print('O valor RMS do sinal é '+ str(np.round(xRMS,4)) +'.')
print('O nível do sinal é ' + str(np.round(Lxt,4)) +' dB.')

#Divisão do sinal em seções de 1000 amostras.
num_sec = len(xt)//1000  #número de seções em que o sinal será dividido.
matriz_sec = np.array_split(xt,num_sec)  #atriz contendo todas as seções do sinal dividido.
media_sec = np.empty(0)  #inicializa um vetor vazio para armazenar a média de cada seção
rms_sec = np.empty(0)    #inicializa um vetor vazio para armazenar o valor RMS de cada seção

#Cálculo do valor médio e RMS de cada seção
for i in matriz_sec:
    media_sec = np.append(media_sec,np.mean(i)*np.ones(len(i)))
    rms_sec = np.append(rms_sec,(np.ones(len(i)))*(np.sqrt(np.mean(i**2))))

#Gráficos
#plot do sinal, com seu valor médio e RMS
plt.figure(figsize=(12,8))

plt.subplot(2,1,1)
plt.title('Sinal waterpump.wav')
plt.plot(t, xt)
plt.plot(t, xm*np.ones(len(t)), label = "Valor Médio")     #Aqui o valor médio e o RMS precisam ser vetorizados para plotar
plt.plot(t, xRMS*np.ones(len(t)), label = "Valor RMS")
plt.grid(linestyle = '--', which='both')     
plt.legend(loc = 'upper right')
plt.ylabel('Amplitude (V)')

#Valores médio e RMS calculados por seção de 1000 amostras
plt.subplot(2,1,2)
plt.title('Sinal waterpump.wav com valores médio e RMS calculados por seção de 1000 amostras.')
plt.plot(t, media_sec, label = "Valor médio")     #Aqui o valor médio e o RMS precisam ser vetorizados para plotar
plt.plot(t, rms_sec, label = "Valor RMS")
plt.grid(linestyle = '--', which='both')     
plt.legend(loc = 'upper right')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')

plt.show()
