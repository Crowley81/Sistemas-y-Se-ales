# -*- coding: utf-8 -*-
"""parcial 1 SyS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/118lSM4HnyDmthwVvOHP27xLHiBnhB5Pf

**Punto 1**
Digitalizacion de la señal

x(t) = 0.3cos(1000πt-π/4)+0.6sen(2000πt)+0.1cos(11000πt - π)
"""

#Importar librerias a utilizar
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

# Función de cuantización
def my_cuantizador(yn, vq):
    dn = cdist(yn.reshape(-1, 1), vq.reshape(-1, 1))  # Distancia entre yn y vq
    ind = np.argmin(dn)
    return vq[ind]

# Parámetros de la señal
Fs = 22000  # Frecuencia de muestreo
Fo1 = 500  # Frecuencia componente 1
Fo2 = 1000  # Frecuencia componente 2
Fo3 = 5500  # Frecuencia componente 3
T = 1 / Fo1  # Periodo del componente de frecuencia más baja
duracion = 4 * T  # Duración de 4 ciclos
Ts = 1 / Fs  # Período de muestreo

# Parámetros de cuantización
nbits = 5  # Numero de bits
rmin = -3.3  # Rango minimo del conversor
rmax = 3.3  # Rango maximo del conversor
ve = np.linspace(rmin, rmax, 2**nbits)

# Vector de tiempo discreto
tv_disc = np.arange(0, duracion, Ts)

# Señal discretizada
xv_disc = 0.3 * np.cos(1000 * np.pi * tv_disc - np.pi / 4) + 0.6 * np.sin(2000 * np.pi * tv_disc) + 0.1 * np.cos(11000 * np.pi * tv_disc - np.pi)

# Cuantización
xv_cuant = []
for xv in xv_disc:
    cuantizado = my_cuantizador(np.array([xv]), ve)
    xv_cuant.append(cuantizado)

xv_cuant = np.array(xv_cuant) # Convertimos la lista a un array de numpy

# Graficar señal cuantizada

plt.figure(figsize=(12, 6))
plt.step(tv_disc, xv_cuant, label="Señal Cuantizada", color='b', where='post')
plt.title("Señal Cuantizada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud Cuantizada")
plt.grid()
plt.legend()
plt.show()

"""Para realizar este ejercicio se implento la ayuda de una IA para la parte final del codigo, la que se encarga de la grafica de la funcion, los prompts utilizados fueron:
* el codigo anterior hace parte de un ejercicio de la materia universitaria Sistemas y señales, este codigo hace parte de un ejercicio por el cual se toma una señal compuesta y es sometida a un proceso de discretizacion y cuantizacion, utilizando la informacion del codigo podrias ayudarme a crear una ultima seccion para el mismo, que se encargue de mostrar la señal cuantizada utilizando la libreria: matplotlib (antes de esta pregunta habia copiado y pegado el codigo para que la IA lo analice)

*Iteracion: solo necesito la grafica de la señal cuantizada
"""