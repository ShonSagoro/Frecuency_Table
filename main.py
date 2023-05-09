from utilities import frecuency_table_tools as ftt
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
