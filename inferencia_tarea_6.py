import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración estética general (Estilo limpio y tipografía Arial)
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Dejavu Sans']

# Color principal institucional y complementarios
COLOR_PRIMARY = '#007D40'  # Verde Institucional
COLOR_SECONDARY = '#4A5568'  # Gris Oscuro
COLOR_ACCENT = '#2B6CB0'     # Azul Ejecutivo
COLOR_LIGHT = '#A0AEC0'      # Gris Claro

# ==========================================
# 📊 GRÁFICOS SEMANA 2: CASO "BANCO FELIZ"
# ==========================================

# Datos Población vs Muestra
categorias = ['Cuenta Empresa', 'Cuenta Personal']
poblacion = [3000, 6000]
muestra = [32, 63]

x = np.arange(len(categorias))
width = 0.35

# Gráfico 1: Población vs Muestra (Doble Eje)
fig, ax1 = plt.subplots(figsize=(8, 5))

bar1 = ax1.bar(x - width/2, poblacion, width, label='Población (N=9000)', color=COLOR_PRIMARY, alpha=0.9)
ax1.set_ylabel('Total Población', color=COLOR_PRIMARY, fontweight='bold')
ax1.tick_params(axis='y', labelcolor=COLOR_PRIMARY)
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, fontsize=11, fontweight='bold')

ax2 = ax1.twinx()
bar2 = ax2.bar(x + width/2, muestra, width, label='Muestra (n=95)', color=COLOR_SECONDARY, alpha=0.8)
ax2.set_ylabel('Total Muestra', color=COLOR_SECONDARY, fontweight='bold')
ax2.tick_params(axis='y', labelcolor=COLOR_SECONDARY)

# Añadir etiquetas de valor sobre las barras
ax1.bar_label(bar1, padding=3)
ax2.bar_label(bar2, padding=3)

plt.title('Representatividad de la Muestra por Estrato', fontsize=14, pad=15, fontweight='bold')
fig.tight_layout()
plt.savefig('G1_Poblacion_vs_Muestra.png', dpi=300)
plt.close()

# Gráfico 2: Composición Porcentual (Gráfico de Donut)
plt.figure(figsize=(6, 6))
colors = [COLOR_SECONDARY, COLOR_PRIMARY]
explode = (0.05, 0) 

plt.pie(poblacion, explode=explode, labels=categorias, colors=colors, 
        autopct='%1.1f%%', startangle=140, pctdistance=0.85,
        textprops={'fontsize': 12, 'fontweight': 'bold'})

# Dibujar el círculo central para transformarlo en donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Distribución Proporcional de los Estratos (33.3% vs 66.7%)', fontsize=13, pad=15, fontweight='bold')
plt.tight_layout()
plt.savefig('G2_Distribucion_Porcentual.png', dpi=300)
plt.close()


# ==========================================
# 📈 GRÁFICOS SEMANA 6: INFERENCIA ESTADÍSTICA
# ==========================================

# Datos de Edades (Muestra Problema 1)
edades = [25, 28, 30, 22, 24, 27, 29, 26, 31, 23, 25, 28, 30, 32, 27]
media_estimada = 27.13  # Calculada previamente

# Gráfico 3: Histograma de Edades con Línea de Media
plt.figure(figsize=(8, 5))
sns.histplot(edades, bins=5, kde=True, color=COLOR_PRIMARY, edgecolor='black', alpha=0.7)
plt.axvline(media_estimada, color='red', linestyle='--', linewidth=2, 
            label=fr'Media Estimada ($\overline{{x}}$) = {media_estimada} años')

plt.title('Distribución de Edades de la Muestra', fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Edad (Años)', fontsize=11)
plt.ylabel('Frecuencia (Clientes)', fontsize=11)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('G3_Histograma_Edades.png', dpi=300)
plt.close()

# Gráfico 4: Comportamiento de Consistencia (Problema 2b)
n_muestras = [10, 30, 100]
theta_1 = [95, 97, 100]
theta_2 = [100, 120, 120]
valor_real = 120

plt.figure(figsize=(8, 5))
plt.axhline(y=valor_real, color='red', linestyle='-', linewidth=1.5, label='Parámetro Real ($\\theta = 120$)')
plt.plot(n_muestras, theta_1, marker='o', color=COLOR_SECONDARY, linewidth=2, label='Estimador $\\hat{\\theta}_1$ (Sesgado/Inconsistente)')
plt.plot(n_muestras, theta_2, marker='s', color=COLOR_PRIMARY, linewidth=2, label='Estimador $\\hat{\\theta}_2$ (Consistente)')

plt.title('Demostración de Consistencia según Tamaño Muestral ($n$)', fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Tamaño de la Muestra ($n$)', fontsize=11)
plt.ylabel('Vida Útil Promedio (Horas)', fontsize=11)
plt.xticks(n_muestras)
plt.ylim(85, 130)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('G4_Consistencia_Estimadores.png', dpi=300)
plt.close()

# Gráfico 5: Comparación de Eficiencia (Curvas de Varianza Teórica)
plt.figure(figsize=(8, 5))
x_teorico = np.linspace(110, 130, 500)

# Distribución para Theta 3 (Varianza = 5.6 -> Desviación ~ 2.36)
y_theta3 = (1 / (np.sqrt(2 * np.pi * 5.6))) * np.exp(-0.5 * ((x_teorico - 120)**2 / 5.6))
# Distribución para Theta 4 (Varianza = 6.5 -> Desviación ~ 2.55)
y_theta4 = (1 / (np.sqrt(2 * np.pi * 6.5))) * np.exp(-0.5 * ((x_teorico - 120)**2 / 6.5))

plt.plot(x_teorico, y_theta3, color=COLOR_PRIMARY, linewidth=2.5, label='$\\hat{\\theta}_3$ (Menor Varianza = 5.6 -> Más Eficiente)')
plt.plot(x_teorico, y_theta4, color=COLOR_ACCENT, linewidth=1.5, linestyle='--', label='$\\hat{\\theta}_4$ (Mayor Varianza = 6.5 -> Menos Eficiente)')
plt.fill_between(x_teorico, y_theta3, alpha=0.1, color=COLOR_PRIMARY)

plt.title('Comparación de Eficiencia Teórica entre Estimadores Insesgados', fontsize=14, pad=15, fontweight='bold')
plt.xlabel('Valor del Estimador', fontsize=11)
plt.ylabel('Densidad de Probabilidad', fontsize=11)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('G5_Eficiencia_Estimadores.png', dpi=300)
plt.close()

print("¡Gráficos generados exitosamente en el directorio local!")