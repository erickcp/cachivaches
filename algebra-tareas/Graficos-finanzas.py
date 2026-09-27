import matplotlib.pyplot as plt
import numpy as np

# Datos calculados de XYZ Corporation
anios = ["Año 1", "Año 2"]
margen_neto = [30.00, 15.56]
roa = [15.00, 7.37]
roe = [25.00, 13.21]

# Posiciones de las barras
x = np.arange(len(anios))
ancho = 0.22

# Creación del gráfico
fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    x - ancho,
    margen_neto,
    ancho,
    label="Margen neto",
    color="#79A941"
)

ax.bar(
    x,
    roa,
    ancho,
    label="ROA",
    color="#526D82"
)

ax.bar(
    x + ancho,
    roe,
    ancho,
    label="ROE",
    color="#A45A52"
)

# Etiquetas sobre las barras
for contenedor in ax.containers:
    ax.bar_label(
        contenedor,
        fmt="%.2f%%",
        padding=3,
        fontsize=9
    )

# Formato
ax.set_title(
    "Evolución de los indicadores de rentabilidad",
    fontsize=14,
    fontweight="bold"
)

ax.set_ylabel("Porcentaje")
ax.set_xticks(x)
ax.set_xticklabels(anios)
ax.set_ylim(0, 35)
ax.grid(axis="y", alpha=0.25)
ax.legend(ncol=3, frameon=False)

plt.tight_layout()

# Guardar imagen para incorporarla al informe
plt.savefig(
    "indicadores_rentabilidad_xyz.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()