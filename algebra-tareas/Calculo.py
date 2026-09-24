import matplotlib.pyplot as plt
import numpy as np

# 1. Definir la función racional del límite
def f(x):
    numerador = 7*x**6 - 13*x**3 + 12*x + 2
    denominador = 4*x**6 - 5*x**2 + 4
    return numerador / denominador

# 2. Generar valores de x (desde 0.5 para evitar problemas cerca de x=0)
# Evaluamos hasta x = 15 para notar claramente la tendencia al infinito
x = np.linspace(0.5, 15, 500)
y = f(x)

# 3. Configurar el gráfico
plt.figure(figsize=(10, 6), facecolor='#ffffff')
ax = plt.axes()
ax.set_facecolor('#f8f9fa')

# Graficar la curva de la función
plt.plot(x, y, color='#007D40', linewidth=2.5, label=r'$f(x) = \frac{7x^6 - 13x^3 + 12x + 2}{4x^6 - 5x^2 + 4}$')

# Graficar la asíntota horizontal (el resultado del límite: 7/4 = 1.75)
limite_valor = 7 / 4
plt.axhline(y=limite_valor, color='#e63946', linestyle='--', linewidth=2, 
            label=f'Límite cuando $x \\to \\infty$ ($y = {limite_valor}$)')

# 4. Personalización y anotaciones
plt.title('Visualización de un Límite al Infinito', fontsize=14, pad=20, weight='bold', color='#1d3557')
plt.xlabel('Eje X ($x \\to \\infty$)', fontsize=11, labelpad=10)
plt.ylabel('Eje Y ($f(x)$)', fontsize=11, labelpad=10)

# Añadir una flecha y texto indicando la convergencia
plt.annotate('La curva se estabiliza en 1.75', 
             xy=(12, 1.76), 
             xytext=(8, 2.2),
             arrowprops=dict(facecolor='#2b2b2b', shrink=0.05, width=1, headwidth=6),
             fontsize=10, 
             weight='bold',
             color='#2b2b2b')

# Ajustar límites visuales para apreciar el comportamiento
plt.xlim(0.5, 15)
plt.ylim(0, 3.5)
plt.grid(True, linestyle=':', alpha=0.6, color='#cccccc')
plt.legend(loc='upper right', fontsize=10)

# 5. Mostrar el gráfico
plt.tight_layout()
plt.show()