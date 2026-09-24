import matplotlib.pyplot as plt

# ---------------- DATOS DEL CASO ----------------
intervalos = ['50-59', '60-69', '70-79', '80-89', '90-99', '100-109']
frecuencias_absolutas = [5, 10, 20, 40, 15, 10]
frecuencias_acumuladas = [5, 15, 35, 75, 90, 100]

# Configuración de estilo global para un look ejecutivo
plt.style.use('seaborn-v0_8-whitegrid')

# ==============================================================================
# GRÁFICO 1: HISTOGRAMA + POLÍGONO DE FRECUENCIAS
# ==============================================================================
fig1, ax1 = plt.subplots(figsize=(10, 6))

# Histograma (Barras con ancho 1.0 para que estén juntas, color azul sobrio)
ax1.bar(intervalos, frecuencias_absolutas, width=1.0, color='#2C3E50', 
        edgecolor='white', alpha=0.8, label='Frecuencia Absoluta (Histograma)')

# Polígono de frecuencias (Línea naranja para contrastar)
ax1.plot(intervalos, frecuencias_absolutas, color='#E67E22', marker='o', 
         linewidth=2.5, markersize=8, label='Polígono de Frecuencias')

# Títulos y etiquetas
ax1.set_title('Distribución de Tiempos de Respuesta en Servidores', fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Intervalos de Tiempo (ms)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Cantidad de Solicitudes (Frecuencia)', fontsize=12, fontweight='bold')

# Detalles visuales
ax1.legend(loc='upper left')
plt.tight_layout()

# Guardar la imagen 1
plt.savefig('1_Histograma_Poligono.png', dpi=300, bbox_inches='tight')
plt.show()

# ==============================================================================
# GRÁFICO 2: LÍNEA DE FRECUENCIA ACUMULADA (OJIVA)
# ==============================================================================
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Gráfico de línea (Verde corporativo para representar acumulación/progreso)
ax2.plot(intervalos, frecuencias_acumuladas, color='#27AE60', marker='s', 
         linewidth=2.5, markersize=8, label='Frecuencia Acumulada')

# Línea punteada de referencia para el 100% (Límite máximo)
ax2.axhline(y=100, color='#7F8C8D', linestyle='--', linewidth=1.5, alpha=0.7)
ax2.text(x=0, y=102, s='100% Total Muestra', color='#7F8C8D', fontsize=10)

# Títulos y etiquetas
ax2.set_title('Proyección de Frecuencia Acumulada', fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel('Intervalos de Tiempo (ms)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Frecuencia Acumulada', fontsize=12, fontweight='bold')

# Detalles visuales
ax2.legend(loc='upper left')
plt.tight_layout()

# Guardar la imagen 2
plt.savefig('2_Frecuencia_Acumulada.png', dpi=300, bbox_inches='tight')
plt.show()

print("¡Gráficos generados y guardados con éxito en alta resolución (300 dpi)!")