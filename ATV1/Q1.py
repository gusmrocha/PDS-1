import numpy as np 
import matplotlib.pyplot as plt

dur = 1     #Duração do sinal (s)
fs = 2000   #Frequência amostral (Hz)

t = np.linspace(0,dur, fs*dur)    #Vetor temporal

A = 1       #Amplitude fundamental
A0 = 0.2      #Amplitude "offset"
freq = 2   #Frequência fundamental (Hz)

x1 = A*np.sin(2*np.pi*freq*t)      #Sinal do item (i)
x2 = A0 + A*np.sin(2*np.pi*freq*t) #Sinal do item (ii)

xm1 = np.mean(x1)  #Média do sinal do item (i)
xm2 = np.mean(x2)  #Média do sinal do item (ii)
rms1 = np.sqrt(np.mean(x1**2))     #RMS do sinal do item (i)
rms2 = np.sqrt(np.mean(x2**2))     #RMS do sinal do item (ii)

#impressão dos gráficos
plt.figure(figsize=(12,4))
#item (i)
plt.subplot(2,1,1)
plt.title('Sinal do item (i)')
plt.plot(t, x1)
plt.plot(t, xm1*np.ones(len(t)), label = "Valor Médio")     #Aqui o valor médio e o RMS precisam ser vetorizados para plotar
plt.plot(t, rms1*np.ones(len(t)), label = "Valor RMS")
plt.grid(linestyle = '--', which='both')     
plt.legend(loc = 'upper right')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.ylim((-1.5, 1.5)) #Este limite na escala foi aplicado para manter a escala entre os gráficos dos itens (i) e (ii)

#item (ii)
plt.subplot(2,1,2)
plt.title('Sinal do item (ii)')
plt.plot(t, x2)
plt.plot(t, xm2*np.ones(len(t)), label = "Valor Médio")     #Aqui o valor médio e o RMS precisam ser vetorizados para plotar
plt.plot(t, rms2*np.ones(len(t)), label = "Valor RMS")
plt.grid(linestyle = '--', which='both')      
plt.legend(loc = 'upper right')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.ylim((-1.5, 1.5))

plt.show()