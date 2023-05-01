import math
from decimal import Decimal

def get_range(data:list):
    return data[len(data)-1] - data[0]

def get_klases(len:int):
    print(f"klases: {1 + 3.322 * math.log(10,len)}")
    return math.ceil(1 + 3.322 * math.log(10,len))

def get_amplitude(r:int ,k:int):
    return math.ceil(r/k);

def get_variation_unit(data:list):
    len_variation_unit=0
    decimal_max=0
    variation_unit=1;

    for number in data:
     if isinstance(number, float):
        variation_unit=str(0.0)
        integer, decimal = math.modf(number)
        for element in str(decimal):
            decimal_max+=1
        if len_variation_unit<decimal_max:
            len_variation_unit=decimal_max

    for i in range(0, len_variation_unit-1):
        variation_unit=+"0"

    if isinstance(variation_unit, float):
        return float(variation_unit)
    
    return int(variation_unit)
    

    
def make_frecuency_table(data: list, numberClasses:int, amplitude: Decimal, variation_unit: Decimal):
    frecuency_table=[]
    lim_inf=data[0];

    for i in range(0, numberClasses):
        lim_sup=lim_inf+amplitude-variation_unit
        frecuency_table.append(
            [
                chr(65+i),
                lim_inf,
                lim_sup,
                get_frecuency_range(data, lim_inf, lim_sup),
                (lim_sup + lim_inf) / 2,
                lim_inf - (variation_unit / 2),
                lim_sup + (variation_unit / 2),
            ]
        )
        lim_inf = lim_sup + variation_unit
    
    return frecuency_table

def get_frecuency_range(data: list, limInf: Decimal, limSup: Decimal):
    frecuency = 0
    for number in data:
        if number <= limSup and number >= limInf:
            frecuency += 1
    return frecuency


def print_frecuency_table(data: list):
    print(
        "|{:<8}|{:<15}|{:<15}|{:<10}|{:<20}|{:<18}|{:<18}|".format(
            "Clase",
            "Límite Inf.",
            "Límite Sup.",
            "Frec.",
            "Marca d Clases",
            "Lim Inf Exac",
            "Lim Sup Exac",
        )
    )
    print(
        "|{:<8}|{:<15}|{:<15}|{:<10}|{:<20}|{:<18}|{:<18}|".format(
            "---", "---", "---", "---", "---", "---", "---"
        )
    )
    for i in data:
        print(
            "|{:<8}|{:<15}|{:<15}|{:<10}|{:<20}|{:<18}|{:<18}|".format(
                i[0], i[1], i[2], i[3], i[4], i[5], i[6]
            )
        )
        
