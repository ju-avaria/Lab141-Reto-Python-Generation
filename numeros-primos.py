numero_inicial = 1
numero_final = 250

print(f"Buscando números primos entre {numero_inicial} y {numero_final}...")

lista_primos = []
for numero in range(numero_inicial, numero_final + 1):
    if numero < 2:
        continue

    es_primo = True

    for divisor in range(2, int(numero ** 0.5) + 1):

        if numero % divisor == 0:
            es_primo = False
            break

    if es_primo:
        lista_primos.append(numero)


print(f"Total de números primos encontrados en la lista: {len(lista_primos)}")
print()
print("Lista de números primos:")

contador = 0
for primo in lista_primos:
    print(f"{primo:4}", end="  ")  # Imprimir con formato alineado a la derecha
    contador += 1
    if contador % 10 == 0:  # Cada 10 números, hacer un salto de línea 
        print()

print()

nombre_archivo = "resultados.txt"

print()
print(f"Guardando resultados en '{nombre_archivo}'...")

archivo = open(nombre_archivo, 'w', encoding='utf-8')

archivo.write("NÚMEROS PRIMOS ENTRE 1 Y 250\n")

archivo.write(f"Total de números primos encontrados: {len(lista_primos)}\n\n")

archivo.write("Lista completa de números primos:\n")

contador = 0
for primo in lista_primos:
    archivo.write(f"{primo:4}  ")
    contador += 1
    if contador % 10 == 0:
        archivo.write("\n")

archivo.write("\nInformación adicional:\n")
archivo.write(f"- Rango analizado: {numero_inicial} a {numero_final}\n")
archivo.write(f"- Primer número primo: {lista_primos[0]}\n")
archivo.write(f"- Último número primo: {lista_primos[-1]}\n")

archivo.close()

print(f"Nombre del Archivo: {nombre_archivo}")