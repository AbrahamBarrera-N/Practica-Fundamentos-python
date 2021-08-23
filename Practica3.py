# Libreria para generar datos aleatorios
import random

# Libreria para generar graficas
# Para instalar esto necesitas copiar y pegar en tu terminal
# python -m pip install -U pip
# python -m pip install -U matplotlib
import matplotlib.pyplot as plt

# Generar un numero aleatorio y lo imprime
print(random.randint(1, 20))

# Generar un numero aleatorio con paso que le damos y lo imprime
print(random.randrange(1, 100, 2))

# Genera una lista al azar, la imprime, la mezcla al azar y la imprime mezclada 
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original", lista)

random.shuffle(lista)
print("Lista mixeada", lista)

# Generar una grafica de camapana de GAUSS
# Genera los datos de la grafica
campana = [random.gauss(1,0.5) for i in range(1000)]
# Arma la grafica
plt.hist(campana, bins=15)
# Muestra la grafica 
plt.show()