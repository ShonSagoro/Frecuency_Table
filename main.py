from utilities import frecuency_table_tools as ftt
import matplotlib.pyplot as plt
import csv
import os

csv_file=os.path.join(os.path.dirname(__file__), 'csv_info\\data.csv')
numeros = []

with open(csv_file) as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    numeros=[float(numero) for numero in next(lector_csv)]
        

print(f"number without sort {numeros}")
numeros.sort()
print(f"numbers sort: {numeros}")


range=ftt.get_range(numeros)

print(f"range: {range}")

klases=ftt.get_klases(len(numeros))
print(f"Cant Data: {len(numeros)}")
print(f"number of classes: {klases}")

amplitude=ftt.get_amplitude(range, klases)
print(f"amplitude: {amplitude}")

variation_unit=ftt.get_variation_unit(numeros)
print(f"variation unit: {variation_unit}")

frecuency_table=ftt.make_frecuency_table(numeros, klases, amplitude, variation_unit)
print(f"Frecuency table: {frecuency_table}")

ftt.print_frecuency_table(frecuency_table)

media_arithmetic=ftt.get_arithmetic_media(frecuency_table, numeros)
print(f"Media aritmetica: {media_arithmetic}")

moda=ftt.get_moda(frecuency_table, amplitude)
print(f"Moda: {moda}")

media=ftt.get_mediana(frecuency_table, numeros, amplitude)
print(f"Mediana: {media}")


klases=[]
frecuency=[]

for element in frecuency_table:
    klases.append(str(element[1])+"-"+str(element[2]))
    frecuency.append(element[3])


plt.bar(klases, frecuency)
plt.title("Tabla de Frecuencias")
plt.xlabel("Valores")
plt.ylabel("Frecuencias")
plt.show()

plt.clf()


plt.pie(frecuency, labels=klases)
plt.title("Tabla de Frecuencias")

plt.show()
