import matplotlib.pyplot as plt
from matplotlib_venn import venn3

def resolver_encuesta():
    # Datos del problema
    total_estudiantes = 100
    python_total = 60
    java_total = 40
    cpp_total = 20
    python_java = 25
    java_cpp = 10
    python_cpp = 8
    los_tres = 5

    # -------------------------------
    # 1. Cálculo de regiones exclusivas
    # -------------------------------

    # Intersección triple
    solo_p_j_c = los_tres

    # Intersecciones dobles exclusivas
    solo_p_j = python_java - los_tres
    solo_j_c = java_cpp - los_tres
    solo_p_c = python_cpp - los_tres

    # Regiones de un solo lenguaje
    solo_python = python_total - solo_p_j - solo_p_c - solo_p_j_c
    solo_java = java_total - solo_p_j - solo_j_c - solo_p_j_c
    solo_cpp = cpp_total - solo_p_c - solo_j_c - solo_p_j_c

    # Total que conoce al menos un lenguaje
    al_menos_uno = (
        solo_python + solo_java + solo_cpp +
        solo_p_j + solo_j_c + solo_p_c + solo_p_j_c
    )

    # Ninguno
    ninguno = total_estudiantes - al_menos_uno

    # Python o Java, pero no C++
    python_o_java_no_cpp = solo_python + solo_java + solo_p_j

    # -------------------------------
    # 2. Mostrar resultados
    # -------------------------------
    print("\n--- RESOLUCIÓN DEL PROBLEMA ---\n")

    print("Regiones exclusivas del diagrama de Venn:")
    print(f"Solo Python: {solo_python}")
    print(f"Solo Java: {solo_java}")
    print(f"Solo C++: {solo_cpp}")
    print(f"Solo Python y Java: {solo_p_j}")
    print(f"Solo Python y C++: {solo_p_c}")
    print(f"Solo Java y C++: {solo_j_c}")
    print(f"Python, Java y C++: {solo_p_j_c}")

    print("\nPreguntas solicitadas:")
    print(f"2. Solo Python: {solo_python} estudiantes")
    print(f"3. Python o Java, pero no C++: {python_o_java_no_cpp} estudiantes")
    print(f"4. Ninguno de los tres lenguajes: {ninguno} estudiantes")

    # -------------------------------
    # 3. Generación del diagrama
    # -------------------------------
    plt.figure(figsize=(10, 8))
    plt.title("Preferencias de Lenguajes de Programación\nTotal encuestados: 100")

    # Orden de venn3:
    # (100, 010, 110, 001, 101, 011, 111)
    venn = venn3(
        subsets=(
            solo_python,  # 100
            solo_java,    # 010
            solo_p_j,     # 110
            solo_cpp,     # 001
            solo_p_c,     # 101
            solo_j_c,     # 011
            solo_p_j_c    # 111
        ),
        set_labels=("Python", "Java", "C++")
    )

    plt.tight_layout()
    plt.savefig("diagrama_encuesta.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

    print("\n✓ Diagrama guardado como 'diagrama_encuesta.png'")

if __name__ == "__main__":
    resolver_encuesta()