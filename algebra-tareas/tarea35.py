import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Ellipse
import numpy as np

# Configuración general de estilo
plt.style.use('bmh')

# 1. Gráfico de la Rueda de la Fortuna (Circunferencia)
fig1, ax1 = plt.subplots(figsize=(6, 6))
rueda = Circle((20, 30), 100, color='blue', fill=False, linewidth=2, label='Rueda de la Fortuna')
ax1.add_patch(rueda)
ax1.plot(20, 30, 'bo') # Centro
ax1.text(25, 30, 'C(20, 30)', color='blue')
ax1.set_xlim(-100, 140)
ax1.set_ylim(-90, 150)
ax1.set_aspect('equal')
ax1.set_title('Pregunta 8: Rueda de la Fortuna')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)
plt.savefig('rueda_fortuna.png', bbox_inches='tight')
plt.close(fig1)

# 2. Gráfico de los Juegos Mecánicos (Línea Recta)
fig2, ax2 = plt.subplots(figsize=(6, 6))
x_line = np.linspace(-20, 50, 100)
y_line = 2 * x_line + 10
ax2.plot(x_line, y_line, color='orange', linewidth=2, label='Juegos Mecánicos (y=2x+10)')
ax2.plot(0, 10, 'ko') # Intersección y
ax2.text(2, 10, '(0, 10)')
ax2.plot(-5, 0, 'ko') # Intersección x
ax2.text(-15, 2, '(-5, 0)')
ax2.set_xlim(-20, 50)
ax2.set_ylim(-30, 110)
ax2.set_title('Pregunta 9: Juegos Mecánicos')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.grid(True)
plt.savefig('juegos_mecanicos.png', bbox_inches='tight')
plt.close(fig2)

# 3. Gráfico de las Tiendas de Souvenirs (Cuadrado)
fig3, ax3 = plt.subplots(figsize=(6, 6))
tiendas = Rectangle((40, 40), 50, 50, color='green', fill=False, linewidth=2, label='Tiendas Souvenirs')
ax3.add_patch(tiendas)
ax3.plot([40, 90, 90, 40], [40, 40, 90, 90], 'go') # Vértices
ax3.text(40, 35, 'A(40,40)', color='green', ha='center')
ax3.text(90, 35, 'B(90,40)', color='green', ha='center')
ax3.text(90, 93, 'C(90,90)', color='green', ha='center')
ax3.text(40, 93, 'D(40,90)', color='green', ha='center')
ax3.set_xlim(20, 110)
ax3.set_ylim(20, 110)
ax3.set_aspect('equal')
ax3.set_title('Pregunta 10: Tiendas de Souvenirs')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.grid(True)
plt.savefig('tiendas_souvenirs.png', bbox_inches='tight')
plt.close(fig3)

# 4. Gráfico de la Montaña Rusa (Elipse)
fig4, ax4 = plt.subplots(figsize=(6, 6))
montana = Ellipse((100, 100), 80, 40, color='red', fill=False, linewidth=2, label='Montaña Rusa')
ax4.add_patch(montana)
ax4.plot(100, 100, 'ro') # Centro
ax4.text(100, 103, 'C(100,100)', color='red', ha='center')
ax4.plot([60, 140], [100, 100], 'ro') # Vértices eje mayor
ax4.plot([100, 100], [80, 120], 'ro') # Vértices eje menor
ax4.set_xlim(50, 150)
ax4.set_ylim(70, 130)
ax4.set_aspect('equal')
ax4.set_title('Pregunta 11: Montaña Rusa')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.grid(True)
plt.savefig('montana_rusa.png', bbox_inches='tight')
plt.close(fig4)

# 5. Gráfico Completo del Parque Temático (Interacciones - Pregunta 12)
fig5, ax5 = plt.subplots(figsize=(10, 10))

# Agregar todas las formas
ax5.add_patch(Circle((20, 30), 100, color='blue', fill=False, linewidth=2, label='Rueda (Circunferencia)'))
ax5.add_patch(Rectangle((40, 40), 50, 50, color='green', fill=False, linewidth=2, label='Tiendas (Cuadrado)'))
ax5.add_patch(Ellipse((100, 100), 80, 40, color='red', fill=False, linewidth=2, label='Montaña Rusa (Elipse)'))

# Agregar línea
x_full = np.linspace(-80, 140, 100)
y_full = 2 * x_full + 10
ax5.plot(x_full, y_full, color='orange', linewidth=2, label='Juegos Mecánicos (Recta)')

# Marcar centros/vértices importantes
ax5.plot(20, 30, 'bo')
ax5.plot(100, 100, 'ro')

ax5.set_xlim(-90, 160)
ax5.set_ylim(-80, 200)
ax5.set_aspect('equal')
ax5.set_title('Pregunta 12: Diseño Completo del Parque Temático\nAnálisis de Solapamiento Espacial', fontsize=14)
ax5.set_xlabel('x')
ax5.set_ylabel('y')
ax5.legend(loc='upper left')
ax5.grid(True)

# Resaltar la zona de conflicto
conflicto = Circle((75, 75), 45, color='purple', fill=True, alpha=0.2, label='Zona de colisión crítica')
ax5.add_patch(conflicto)
ax5.legend(loc='upper left')

plt.savefig('parque_tematico_completo.png', bbox_inches='tight')
plt.close(fig5)

print("Imágenes generadas correctamente.")