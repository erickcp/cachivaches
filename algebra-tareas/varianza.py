import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def graficar_normal(mu, sigma, limite, titulo, archivo):
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y = norm.pdf(x, mu, sigma)

    plt.figure(figsize=(9, 5))
    plt.plot(x, y, linewidth=2)

    # Área sombreada P(X > limite)
    x_fill = np.linspace(limite, mu + 4*sigma, 500)
    y_fill = norm.pdf(x_fill, mu, sigma)
    plt.fill_between(x_fill, y_fill, alpha=0.35)

    # Líneas de referencia
    plt.axvline(mu, linestyle="--", linewidth=2, label=f"Media μ = {mu}")
    plt.axvline(limite, linestyle="--", linewidth=2, label=f"Límite = {limite}")

    prob = 1 - norm.cdf(limite, mu, sigma)

    plt.title(titulo)
    plt.xlabel("Horas")
    plt.ylabel("Densidad de probabilidad")
    plt.legend()
    plt.grid(alpha=0.3)

    plt.text(
        limite + sigma * 0.2,
        max(y) * 0.55,
        f"P(X > {limite}) = {prob:.4f}\n{prob*100:.2f}%",
        fontsize=11
    )

    plt.tight_layout()
    plt.savefig(archivo, dpi=300)
    plt.show()


# Pregunta 1
graficar_normal(
    mu=40,
    sigma=8,
    limite=50,
    titulo="Pregunta 1: Probabilidad de que un módulo requiera más de 50 horas de prueba",
    archivo="pregunta_1_normal.png"
)

# Pregunta 3
graficar_normal(
    mu=60,
    sigma=10,
    limite=50,
    titulo="Pregunta 3: Probabilidad de que un error crítico cause más de 50 horas de inactividad",
    archivo="pregunta_3_normal.png"
)