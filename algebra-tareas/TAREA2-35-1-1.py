import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Ellipse
import numpy as np

def configurar_grafico(ax, titulo, xlim, ylim):
    """Aplica configuraciones estándar de formato a cada gráfico."""
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal') # CRÍTICO: Mantiene la proporción geométrica real
    ax.set_title(titulo, fontsize=12, pad=15)
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.grid(True, linestyle='--', alpha=0.7)

# Configuración de estilo general
plt.style.use('bmh')

# ==========================================
# 1. Rueda de la Fortuna (Circunferencia)
# ==========================================
fig1, ax1 = plt.subplots(figsize=(7, 7))
rueda = Circle((20, 30), 100, color='#1f77b4', fill=False, linewidth=2.5)
ax1.add_patch(rueda)

# Puntos de referencia
ax1.plot(20, 30, 'ko') 
ax1.text(25, 30, 'Centro (20, 30)')
ax1.plot([20, 120], [30, 30], 'k--', alpha=0.5)
ax1.text(70, 35, 'r = 100')

configurar_grafico(ax1, 'Pregunta 8: Rueda de la Fortuna\n$(x-20)^2 + (y-30)^2 = 10.000$', (-90, 130), (-80, 140))
plt.savefig('01_rueda_fortuna.png', dpi=300, bbox_inches='tight')
plt.close(fig1)

# ==========================================
# 2. Juegos Mecánicos (Línea Recta)
# ==========================================
fig2, ax2 = plt.subplots(figsize=(7, 7))
x_line = np.linspace(-25, 45, 100)
y_line = 2 * x_line + 10

ax2.plot(x_line, y_line, color='#ff7f0e', linewidth=2.5, label='y = 2x + 10')

# Intersecciones y puntos de control
puntos_recta = [(0, 10), (-5, 0), (20, 50)]
textos_recta = ['Corte Y (0, 10)', 'Corte X (-5, 0)', 'Control (20, 50)']

for (px, py), texto in zip(puntos_recta, textos_recta):
    ax2.plot(px, py, 'ko')
    ax2.text(px + 2, py - 4, texto)

configurar_grafico(ax2, 'Pregunta 9: Juegos Mecánicos\nPendiente = 2', (-25, 45), (-30, 80))
ax2.legend()
plt.savefig('02_juegos_mecanicos.png', dpi=300, bbox_inches='tight')
plt.close(fig2)

# ==========================================
# 3. Tiendas de Souvenirs (Cuadrado)
# ==========================================
fig3, ax3 = plt.subplots(figsize=(7, 7))
tiendas = Rectangle((40, 40), 50, 50, color='#2ca02c', fill=True, alpha=0.2, linewidth=2.5)
borde_tiendas = Rectangle((40, 40), 50, 50, color='#2ca02c', fill=False, linewidth=2.5)
ax3.add_patch(tiendas)
ax3.add_patch(borde_tiendas)

# Vértices
ax3.plot([40, 90, 90, 40], [40, 40, 90, 90], 'ko')
ax3.text(40, 35, 'A(40, 40)', ha='center')
ax3.text(90, 35, 'B(90, 40)', ha='center')
ax3.text(90, 94, 'C(90, 90)', ha='center')
ax3.text(40, 94, 'D(40, 90)', ha='center')

configurar_grafico(ax3, 'Pregunta 10: Tiendas de Souvenirs\nLados de 50 unidades', (20, 110), (20, 110))
plt.savefig('03_tiendas_souvenirs.png', dpi=300, bbox_inches='tight')
plt.close(fig3)

# ==========================================
# 4. Montaña Rusa (Elipse)
# ==========================================
fig4, ax4 = plt.subplots(figsize=(7, 7))
# En Matplotlib, width y height son los ejes totales (2a y 2b)
montana = Ellipse((100, 100), 80, 40, color='#d62728', fill=False, linewidth=2.5)
ax4.add_patch(montana)

# Elementos de la elipse
ax4.plot(100, 100, 'ko') 
ax4.text(100, 104, 'C(100, 100)', ha='center')
ax4.plot([60, 140], [100, 100], 'ko') # Vértices principales
ax4.plot([100, 100], [80, 120], 'ko') # Vértices secundarios
ax4.plot([60, 140], [100, 100], 'k--', alpha=0.5) # Eje mayor
ax4.plot([100, 100], [80, 120], 'k--', alpha=0.5) # Eje menor

configurar_grafico(ax4, 'Pregunta 11: Montaña Rusa\nEje mayor=80, Eje menor=40', (50, 150), (70, 130))
plt.savefig('04_montana_rusa.png', dpi=300, bbox_inches='tight')
plt.close(fig4)

# ==========================================
# 5. Diseño Completo y Análisis (Solapamiento)
# ==========================================
fig5, ax5 = plt.subplots(figsize=(12, 12))

# Agregar todas las formas al plano principal
ax5.add_patch(Circle((20, 30), 100, color='#1f77b4', fill=False, linewidth=2, label='Rueda de la Fortuna'))
ax5.add_patch(Rectangle((40, 40), 50, 50, color='#2ca02c', fill=True, alpha=0.3, label='Tiendas'))
ax5.add_patch(Ellipse((100, 100), 80, 40, color='#d62728', fill=False, linewidth=2, label='Montaña Rusa'))

x_full = np.linspace(-90, 150, 100)
y_full = 2 * x_full + 10
ax5.plot(x_full, y_full, color='#ff7f0e', linewidth=2, label='Juegos Mecánicos')

# Marcar centros de las atracciones
ax5.plot([20, 100], [30, 100], 'ko')

# Configuración final del plano completo
configurar_grafico(ax5, 'Pregunta 12: Diseño Completo del Parque Temático\nSe evidencia colisión geométrica entre atracciones', (-90, 160), (-80, 160))

# Resaltar la zona de conflicto
conflicto = Circle((75, 75), 45, color='purple', fill=True, alpha=0.15, label='Zona de Conflicto Espacial')
ax5.add_patch(conflicto)

ax5.legend(loc='upper left', fontsize=10, frameon=True, shadow=True)
plt.savefig('05_parque_tematico_analisis.png', dpi=300, bbox_inches='tight')
plt.close(fig5)

print("¡Proceso finalizado! Las 5 imágenes se han guardado en alta resolución.")