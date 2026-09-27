# ==========================================
# 📈 CORRECCIÓN GRÁFICO 4: COMPORTAMIENTO DE CONSISTENCIA
# ==========================================
n_muestras = [10, 30, 100][cite: 2]
theta_1 = [95, 100, 97][cite: 2]  # <--- ¡CORREGIDO AQUÍ! (Antes decía 100 al final)
theta_2 = [100, 120, 120][cite: 2]
valor_real = 120[cite: 2]

plt.figure(figsize=(8, 5))
plt.axhline(y=valor_real, color='red', linestyle='-', linewidth=1.5, label='Parámetro Real ($\\theta = 120$)')[cite: 2]
plt.plot(n_muestras, theta_1, marker='o', color=COLOR_SECONDARY, linewidth=2, label='Estimador $\\hat{\\theta}_1$ (Sesgado/Inconsistente)')[cite: 2]
plt.plot(n_muestras, theta_2, marker='s', color=COLOR_PRIMARY, linewidth=2, label='Estimador $\\hat{\\theta}_2$ (Consistente)')[cite: 2]

plt.title('Demostración de Consistencia según Tamaño Muestral ($n$)', fontsize=14, pad=15, fontweight='bold')[cite: 2]
plt.xlabel('Tamaño de la Muestra ($n$)', fontsize=11)[cite: 2]
plt.ylabel('Vida Útil Promedio (Horas)', fontsize=11)[cite: 2]
plt.xticks(n_muestras)
plt.ylim(85, 130)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('G4_Consistencia_Estimadores.png', dpi=300)
plt.close()