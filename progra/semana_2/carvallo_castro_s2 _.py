"""
EVALUACIÓN SUMATIVA SEMANA 2 - PROGRAMACIÓN
Integrantes: Erick Carvallo y Carol Castro

PSEUDOCÓDIGO GENERAL

INICIO
    Crear una lista vacía para guardar el historial.

    MIENTRAS el programa esté activo:
        Mostrar el menú y solicitar una opción.

        SI la opción está entre 1 y 5:
            Solicitar y validar los datos de la operación.
            Ejecutar la función correspondiente.
            Mostrar el resultado.
            Guardar un resumen en el historial.
        SINO, SI la opción es 6:
            Mostrar el historial y finalizar.
        SINO:
            Informar que la opción no es válida.
FIN

PSEUDOCÓDIGO POR OPCIÓN

1. Cálculo de vuelto
    Entrada: monto de la compra y monto pagado.
    Proceso: validar los montos y calcular pago - compra.
    Salida: vuelto expresado en pesos.

2. Promedio de notas
    Entrada: tres notas decimales entre 1.0 y 7.0.
    Proceso: guardar las notas, sumarlas y dividir por tres.
    Salida: promedio con dos decimales.

3. Aplicación de descuento
    Entrada: precio original y descuento definido en 35%.
    Proceso: calcular el monto descontado y restarlo al precio.
    Salida: descuento aplicado y precio final.

4. Conversión de tiempo
    Entrada: cantidad total de minutos.
    Proceso: calcular horas con // y minutos restantes con %.
    Salida: tiempo expresado en horas y minutos.

5. Reparto y sobrante
    Entrada: cantidad de productos y cantidad de personas.
    Proceso: calcular reparto con // y sobrante con %.
    Salida: productos por persona y productos sobrantes.
"""


def leer_float(mensaje, minimo=None, maximo=None):
    """Solicita un número decimal y repite la entrada si no es válida."""
    while True:
        entrada = input(mensaje).strip().replace(",", ".")

        try:
            valor = float(entrada)
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
            continue

        if minimo is not None and valor < minimo:
            print(f"El valor debe ser mayor o igual que {minimo}.")
            continue

        if maximo is not None and valor > maximo:
            print(f"El valor debe ser menor o igual que {maximo}.")
            continue

        return valor


def leer_entero(mensaje, minimo=None, maximo=None):
    """Solicita un número entero y repite la entrada si no es válida."""
    while True:
        entrada = input(mensaje).strip()

        try:
            valor = int(entrada)
        except ValueError:
            print("Entrada no válida. Debe ingresar un número entero.")
            continue

        if minimo is not None and valor < minimo:
            print(f"El valor debe ser mayor o igual que {minimo}.")
            continue

        if maximo is not None and valor > maximo:
            print(f"El valor debe ser menor o igual que {maximo}.")
            continue

        return valor


def calcular_vuelto(monto_compra, monto_pagado):
    return monto_pagado - monto_compra


def promedio_notas(notas):
    return sum(notas) / len(notas)


def aplicar_descuento(precio, porcentaje_descuento):
    monto_descuento = precio * porcentaje_descuento / 100
    precio_final = precio - monto_descuento
    return monto_descuento, precio_final


def convertir_minutos(total_minutos):
    """Retorna el tiempo separado en horas y minutos."""
    horas = total_minutos // 60
    minutos_restantes = total_minutos % 60
    return horas, minutos_restantes


def calcular_reparto(total_productos, cantidad_personas):
    productos_por_persona = total_productos // cantidad_personas
    productos_sobrantes = total_productos % cantidad_personas
    return productos_por_persona, productos_sobrantes


def formatear_moneda(valor):
    formato = f"{valor:,.2f}"
    formato = (
        formato.replace(",", "PUNTO").replace(".", ",").replace("PUNTO", ".")
    )
    return f"${formato}"


def mostrar_menu():
    print("\n--- MINI APLICACIÓN DE CÁLCULOS ---")
    print("1. Calcular vuelto")
    print("2. Calcular promedio de tres notas")
    print("3. Aplicar descuento")
    print("4. Convertir minutos a horas y minutos")
    print("5. Calcular reparto y sobrante")
    print("6. Mostrar historial y salir")


def mostrar_historial(historial):
    print("\n--- HISTORIAL DE OPERACIONES ---")

    if not historial:
        print("No se realizaron operaciones durante esta sesión.")
        return

    for numero, operacion in enumerate(historial, start=1):
        print(f"{numero}. {operacion}")


def ejecutar_programa():
    historial = []
    porcentaje_descuento = 35.0

    while True:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opción: ")

        if opcion == 1:
            monto_compra = leer_float(
                "Ingrese el monto de la compra: $", minimo=0
            )

            # El pago debe cubrir la compra para que exista un vuelto válido.
            while True:
                monto_pagado = leer_float("Ingrese el monto pagado: $", minimo=0)
                if monto_pagado >= monto_compra:
                    break
                print("El monto pagado no puede ser menor que la compra.")

            vuelto = calcular_vuelto(monto_compra, monto_pagado)
            resultado = f"Vuelto calculado: {formatear_moneda(vuelto)}"
            print(resultado)
            historial.append(resultado)

        elif opcion == 2:
            notas = []

            for numero_nota in range(1, 4):
                nota = leer_float(
                    f"Ingrese la nota {numero_nota}: ", minimo=1.0, maximo=7.0
                )
                notas.append(nota)

            promedio = promedio_notas(notas)
            resultado = f"Promedio de notas: {promedio:.2f}"
            print(resultado)
            historial.append(resultado)

        elif opcion == 3:
            precio = leer_float("Ingrese el precio original: $", minimo=0)
            monto_descuento, precio_final = aplicar_descuento(
                precio, porcentaje_descuento
            )

            print(
                f"Descuento aplicado ({porcentaje_descuento:.0f}%): "
                f"{formatear_moneda(monto_descuento)}"
            )
            resultado = (
                "Precio final con descuento: "
                f"{formatear_moneda(precio_final)}"
            )
            print(resultado)
            historial.append(resultado)

        elif opcion == 4:
            total_minutos = leer_entero(
                "Ingrese la cantidad total de minutos: ", minimo=0
            )
            horas, minutos_restantes = convertir_minutos(total_minutos)
            resultado = (
                f"{total_minutos} minutos equivalen a "
                f"{horas} hora(s) y {minutos_restantes} minuto(s)"
            )
            print(resultado)
            historial.append(resultado)

        elif opcion == 5:
            total_productos = leer_entero(
                "Ingrese la cantidad de productos: ", minimo=0
            )
            cantidad_personas = leer_entero(
                "Ingrese la cantidad de personas: ", minimo=1
            )
            productos_por_persona, productos_sobrantes = calcular_reparto(
                total_productos, cantidad_personas
            )
            resultado = (
                f"Cada persona recibe {productos_por_persona} producto(s) "
                f"y sobran {productos_sobrantes}"
            )
            print(resultado)
            historial.append(resultado)

        elif opcion == 6:
            mostrar_historial(historial)
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Seleccione un número entre 1 y 6.")


if __name__ == "__main__":
    ejecutar_programa()


# EVIDENCIA Y FUNDAMENTO
#
# Decisiones de diseño:
# - Se utilizaron funciones para separar cada cálculo del flujo del menú.
# - Las funciones reciben parámetros y retornan resultados, sin depender de
#   variables globales.
# - Se usó una lista porque el historial crece cada vez que se completa una
#   operación y luego puede recorrerse antes de finalizar.
# - Las funciones leer_float() y leer_entero() concentran las validaciones y
#   evitan repetir el mismo código en cada opción.
#
# Casos de prueba:
# 1. Compra = 7500 y pago = 10000 -> vuelto esperado = $2.500,00.
# 2. Notas = 5.0, 6.0 y 7.0 -> promedio esperado = 6.00.
# 3. Minutos = 135 -> salida esperada = 2 horas y 15 minutos.
#
# Error típico evitado:
# - input() retorna texto. Antes de calcular, cada entrada se convierte a float
#   o int. Si el dato no es numérico, el programa informa el problema y vuelve
#   a solicitarlo. En el reparto también se impide usar cero personas, porque
#   produciría una división por cero.
