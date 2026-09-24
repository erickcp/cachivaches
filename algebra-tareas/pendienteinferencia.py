import matplotlib.pyplot as plt
import numpy as np

# 1. Definir los datos basados en la función V(t) = -200000*t + 12000000
# Graficaremos desde el año 0 hasta el año 35 para ver todo el panorama
t = np.linspace(0, 35, 100)
v = -200000 * t + 12000000

# 2. Configurar el gráfico (Estilo limpio y moderno)
plt.figure(figsize=(10, 6), facecolor='#ffffff')
ax = plt.axes()
ax.set_facecolor('#f8f9fa')

# Dibujar la línea de la función principal
plt.plot(t, v, color='#1d3557', linewidth=2.5, label='Valor de la camioneta V(t)')

# 3. Destacar los puntos clave del ejercicio
puntos_clave = [
    (0, 12000000, 'Valor Inicial\n$12M'),
    (4, 11200000, 'A los 4 años\n$11.2M'),
    (30, 6000000, 'A los 30 años\n$6M')
]

for t_p, v_p, texto in puntos_clave:
    # Dibujar el punto
    plt.scatter(t_p, v_p, color='#e63946', s=65, zorder=5)
    # Líneas de guía proyectadas hacia los ejes
    plt.axhline(y=v_p, xmin=0, xmax=t_p/35, color='#bdbdbd', linestyle='--', linewidth=0.8)
    plt.axvline(x=t_p, ymin=0, ymax=(v_p)/13000000, color='#bdbdbd', linestyle='--', linewidth=0.8)
    # Etiqueta de texto para cada punto
    plt.text(t_p + 0.8, v_p + 150000, texto, fontsize=9, color='#2b2b2b', weight='bold')

# 4. Personalización de etiquetas y formato
plt.title('Modelo de Depreciación Lineal (Pendiente Negativa)', fontsize=14, pad=20, weight='bold', color='#1d3557')
plt.xlabel('Tiempo transcurrido (Años)', fontsize=11, labelpad=10)
plt.ylabel('Valor comercial ($)', fontsize=11, labelpad=10)

# Dar formato numérico legible al eje Y (evitar notación científica)
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

plt.xlim(-1, 35)
plt.ylim(4000000, 13000000)
plt.grid(True, linestyle=':', alpha=0.6, color='#cccccc')
plt.legend(loc='upper right')

# 5. Desplegar el gráfico
plt.tight_layout()
plt.show()