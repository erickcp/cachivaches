# import matplotlib.pyplot as plt
# from matplotlib_venn import venn3

# # ==========================================
# # APLICACIÓN 3 - DIAGRAMA DE VENN CORREGIDO
# # ==========================================

# # Conjuntos:
# # A = análisis de datos
# # M = modelación de procesos
# # T = entornos técnicos

# # ------------------------------------------
# # REGIONES DEL DIAGRAMA (ya calculadas)
# # ------------------------------------------

# solo_A = 368
# solo_M = 490
# solo_T = 184

# A_M_solo = 156
# A_T_solo = 72
# M_T_solo = 174

# triple = 118

# ninguno = 1438
# total = 3000

# # ------------------------------------------
# # VERIFICACIÓN
# # ------------------------------------------

# suma_total = (
#     solo_A +
#     solo_M +
#     solo_T +
#     A_M_solo +
#     A_T_solo +
#     M_T_solo +
#     triple +
#     ninguno
# )

# print("Verificación total:", suma_total)

# # ------------------------------------------
# # CREAR GRÁFICO
# # Orden venn3:
# # (100,010,110,001,101,011,111)
# # A solo, M solo, A∩M,
# # T solo, A∩T, M∩T, triple
# # ------------------------------------------

# plt.figure(figsize=(12,10))

# venn = venn3(
#     subsets=(
#         solo_A,
#         solo_M,
#         A_M_solo,
#         solo_T,
#         A_T_solo,
#         M_T_solo,
#         triple
#     ),
#     set_labels=("A\nAnálisis", "M\nModelación", "T\nEntornos")
# )

# # ------------------------------------------
# # PERSONALIZAR COLORES
# # ------------------------------------------

# venn.get_patch_by_id('100').set_color('#4A90E2')
# venn.get_patch_by_id('010').set_color('#50C878')
# venn.get_patch_by_id('001').set_color('#B565D9')

# # ------------------------------------------
# # TÍTULO
# # ------------------------------------------

# plt.title(
#     "Aplicación 3 - Herramientas utilizadas por estudiantes\n"
#     f"Total = {total} | Ninguno = {ninguno}",
#     fontsize=14,
#     weight='bold'
# )

# # ------------------------------------------
# # RESULTADOS PREGUNTA 8 y 9
# # ------------------------------------------

# A_union_T = (
#     solo_A +
#     A_M_solo +
#     A_T_solo +
#     triple +
#     solo_T +
#     M_T_solo
# )

# A_inter_T_solo = A_T_solo

# texto = (
#     f"Pregunta 8: A ∪ T = {A_union_T}\n"
#     f"Pregunta 9: A ∩ T sin M = {A_inter_T_solo}"
# )

# plt.figtext(
#     0.5,
#     0.02,
#     texto,
#     ha="center",
#     fontsize=12,
#     bbox=dict(facecolor="lightyellow", edgecolor="black")
# )

# # ------------------------------------------
# # GUARDAR
# # ------------------------------------------

# plt.tight_layout()
# plt.savefig("diagrama_venn_aplicacion3.png", dpi=300)
# plt.show()


import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# ==========================================
# APLICACIÓN 3 - DIAGRAMA DE VENN MEJORADO
# ==========================================

# Conjuntos:
# A = análisis de datos
# M = modelación de procesos
# T = entornos técnicos especializados

# ------------------------------------------
# REGIONES
# ------------------------------------------

solo_A = 368
solo_M = 490
solo_T = 184

A_M_solo = 156
A_T_solo = 72
M_T_solo = 174

triple = 118

ninguno = 1438
total = 3000

# ------------------------------------------
# VERIFICACIÓN
# ------------------------------------------

suma_total = (
    solo_A + solo_M + solo_T +
    A_M_solo + A_T_solo + M_T_solo +
    triple + ninguno
)

print("Verificación =", suma_total)

# ------------------------------------------
# CREAR DIAGRAMA
# Orden venn3:
# (100,010,110,001,101,011,111)
# ------------------------------------------

plt.figure(figsize=(14,10))

venn = venn3(
    subsets=(
        solo_A,
        solo_M,
        A_M_solo,
        solo_T,
        A_T_solo,
        M_T_solo,
        triple
    ),
    set_labels=(
        "A\nAnálisis de datos",
        "M\nModelación",
        "T\nEntornos técnicos"
    )
)

# ------------------------------------------
# COLORES
# ------------------------------------------

venn.get_patch_by_id('100').set_color("#4A90E2")
venn.get_patch_by_id('010').set_color("#50C878")
venn.get_patch_by_id('001').set_color("#B565D9")

# ------------------------------------------
# ETIQUETAS INTERNAS CON DESCRIPCIÓN
# ------------------------------------------

labels = {
    '100': f"{solo_A}\nSolo A",
    '010': f"{solo_M}\nSolo M",
    '001': f"{solo_T}\nSolo T",
    '110': f"{A_M_solo}\nA ∩ M",
    '101': f"{A_T_solo}\nA ∩ T",
    '011': f"{M_T_solo}\nM ∩ T",
    '111': f"{triple}\nA ∩ M ∩ T"
}

for region_id, text in labels.items():
    label = venn.get_label_by_id(region_id)
    if label:
        label.set_text(text)
        label.set_fontsize(11)

# ------------------------------------------
# RESULTADOS PREGUNTAS
# ------------------------------------------

A_union_T = (
    solo_A +
    A_M_solo +
    A_T_solo +
    triple +
    solo_T +
    M_T_solo
)

A_inter_T_solo = A_T_solo

# ------------------------------------------
# TÍTULO
# ------------------------------------------

plt.title(
    "Aplicación 3 - Uso de herramientas por estudiantes\n"
    f"Total: {total} | Ninguno: {ninguno}",
    fontsize=15,
    weight="bold"
)

# ------------------------------------------
# TEXTO INFERIOR
# ------------------------------------------

texto = (
    f"Pregunta 8: A ∪ T = {A_union_T} estudiantes\n"
    f"Pregunta 9: A ∩ T sin M = {A_inter_T_solo} estudiantes"
)

plt.figtext(
    0.5,
    0.02,
    texto,
    ha="center",
    fontsize=12,
    bbox=dict(facecolor="lightyellow", edgecolor="black")
)

# ------------------------------------------
# GUARDAR
# ------------------------------------------

plt.tight_layout()
plt.savefig("diagrama_venn_aplicacion3_mejorado.png", dpi=300)
plt.show()