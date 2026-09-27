import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

# Configuración estética
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

COLOR_PRIMARY = '#007D40'  # Verde Institucional
COLOR_SECONDARY = '#4A5568'
COLOR_ACCENT = '#2B6CB0'

# ==========================================
# G1: Función de Log-Verosimilitud (Problema 1)
# ==========================================
p_vals = np.linspace(0.05, 0.95, 200)
# Asumiendo una muestra simulada donde x_bar = 2.5 => p_hat = 0.4
x_bar = 2.5
n = 10
log_lik = n * np.log(p_vals) - p_vals * (n * x_bar)

plt.figure(figsize=(7, 4.5))
plt.plot(p_vals, log_lik, color=COLOR_PRIMARY, linewidth=2.5, label='$\ln L(p)$')
plt.axvline(x=1/x_bar, color='red', linestyle='--', label=f'Máximo $\hat{{p}}_{{EMV}} = 1/\\bar{{X}} = {1/x_bar}$')
plt.title('Problema 1: Maximización de Log-Verosimilitud', fontsize=12, fontweight='bold')
plt.xlabel('Parámetro $p$', fontsize=10)
plt.ylabel('Log-Verosimilitud $\ln L(p)$', fontsize=10)
plt.legend()
plt.tight_layout()
plt.savefig('G1_Verosimilitud_P1.png', dpi=300)
plt.close()

# ==========================================
# G2: Intervalo de Confianza Dif. Medias (Problema 3)
# ==========================================
plt.figure(figsize=(7, 3.5))
li, ls, diff = -0.0985, 7.8985, 3.9
plt.errorbar(diff, 0, xerr=[[diff - li], [ls - diff]], fmt='o', color=COLOR_PRIMARY, 
             ecolor=COLOR_ACCENT, elinewidth=3, capsize=8, capthick=2, markersize=8, label='Diferencia Muestral (3.9)')
plt.axvline(x=0, color='red', linestyle='--', linewidth=1.5, label='Cero (Sin Diferencia: $\mu_1 = \mu_2$)')
plt.title('Problema 3: IC 95% para Diferencia de Medias (Parafina vs Petróleo)', fontsize=12, fontweight='bold')
plt.xlabel('Diferencia de Contaminación ($\mu_1 - \mu_2$)', fontsize=10)
plt.yticks([])
plt.xlim(-2, 10)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('G2_Intervalo_Medias_P3.png', dpi=300)
plt.close()

# ==========================================
# G3: Intervalo de Confianza Proporción (Problema 4)
# ==========================================
plt.figure(figsize=(7, 3.5))
li_p, ls_p, p_hat = 0.00, 0.4024, 0.20
plt.errorbar(p_hat, 0, xerr=[[p_hat - li_p], [ls_p - p_hat]], fmt='s', color=COLOR_PRIMARY, 
             ecolor=COLOR_SECONDARY, elinewidth=3, capsize=8, capthick=2, markersize=8, label='Proporción Muestral (20%)')
plt.axvline(x=0.20, color='gray', linestyle=':', label='Valor Histórico (20%)')
plt.title('Problema 4: IC 95% para Proporción de Mala Administración', fontsize=12, fontweight='bold')
plt.xlabel('Proporción de Sucursales ($p$)', fontsize=10)
plt.yticks([])
plt.xlim(-0.05, 0.50)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('G3_Intervalo_Proporcion_P4.png', dpi=300)
plt.close()

print("Gráficos generados correctamente.")