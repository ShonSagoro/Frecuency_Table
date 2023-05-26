import math
from decimal import Decimal

len_decimal = 0


def get_digits(number):
    digit_decimal = 0
    if "." in str(number):
        digit_decimal = (
            len(str(number).split(".")[1])
            if len(str(number).split(".")[1]) > digit_decimal
            else digit_decimal
        )
    return digit_decimal


def get_range(data: list):
    result = data[len(data) - 1] - data[0]
    len_digits = get_digits(data[0])
    return round(result, len_digits)


def get_klases(len: int):
    decimal, integer = math.modf(1 + 3.322 * math.log(len, 10))
    return int(integer)


def get_amplitude(r: int, k: int):
    if r % k == 0:
        return (r / k) + 1
    len_digits = get_digits(r)
    return round(r / k, len_digits)


def get_variation_unit(data: list):
    maxDecimalNumber = 0
    for number in data:
        maxDecimalNumber = get_digits(number)

    return float(str(math.pow(10, -(maxDecimalNumber))))


def make_frecuency_table(data: list, numberClasses: int, amplitude: Decimal, variation_unit: Decimal):
    frequency_table = []

    lim_inf = data[0]
    frec_acumulate=0
    len_decimal = (
        get_digits(variation_unit)
        if get_digits(variation_unit) != 0
        else 1
    )
    for i in range(0, numberClasses):

        lim_sup = lim_inf + amplitude - variation_unit
        frequency = get_frecuency_range(data, lim_inf, lim_sup);
        frec_acumulate += frequency
        frequency_table.append(
            [
                chr(65 + i), #Clase
                round(lim_inf, len_decimal),
                round(lim_sup, len_decimal),
                round(frequency, len_decimal),
                round(get_class_mark(lim_inf,lim_sup), len_decimal),
                round(frec_acumulate, len_decimal),
                round(lim_inf - (variation_unit / 2), len_decimal),
                round(lim_sup + (variation_unit / 2), len_decimal),
                round(frequency/len(data), len_decimal),
                round((frequency/len(data))*100, len_decimal),
            ]
        )
        lim_inf = lim_sup + variation_unit

    return frequency_table


def get_class_mark(lim_inf, lim_sup):
    return (lim_sup + lim_inf) / 2


def get_frecuency_range(data: list, limInf: Decimal, limSup: Decimal):
    frecuency = 0
    for number in data:
        if number <= limSup and number >= limInf:
            frecuency += 1
    return frecuency


def print_frecuency_table(data: list):
    print(
        "|{:<8}|{:<15}|{:<15}|{:<10}|{:<20}|{:<18}|{:<18}|{:<18}|{:<18}|{:<18}|".format(
            "Clase",
            "Límite Inf.",
            "Límite Sup.",
            "Frec.",
            "Marca d Clases",
            "Frec. Acu.",
            "Lim Inf Exac",
            "Lim Sup Exac",
            "Frec Rel prop",
            "Frec Rel %",
        )
    )
    print(
        "|{:<8}|{:<15}|{:<15}|{:<10}|{:<20}|{:<18}|{:<18}|{:<18}|{:<18}|{:<18}|".format(
            "---", "---", "---", "---", "---", "---", "---", "---", "---", "---"
        )
    )
    for i in data:
        print(
            "|{:<8}|{:<15}|{:<15}|{:<10}|{:<20}|{:<18}|{:<18}|{:<18}| % {:<18}|{:<18}|".format(
                i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8],i[9]
            )
        )
def get_arithmetic_media(frecuency:list, data:list):
    len_digits = get_digits(frecuency[0][1])
    summation=0
    for element in frecuency:
        summation+=(element[3]*element[4])
    return round(summation/len(data),len_digits)

def get_moda(frecuency:list, amplitude:float):
    len_digits = get_digits(frecuency[0][1])
    max_valor=None
    max_fila_index=None
    for index, fila in enumerate(frecuency):
        if max_valor is None or fila[3] > max_valor:
            max_valor = fila[3]
            max_fila_index = index
    lim_inf_exac=frecuency[max_fila_index][6]
    d1=frecuency[max_fila_index][3]-frecuency[(max_fila_index-1)][3]
    d2=frecuency[max_fila_index][3]-frecuency[(max_fila_index+1)][3]

    return round(lim_inf_exac+(d1/(d1+d2))*(amplitude), len_digits)


def get_mediana(frecuency:list, data:list, amplitude:float):
    len_digits = get_digits(frecuency[0][1])
    location=(len(data)+1)/2
    media_index=None
    for index, fila in enumerate(frecuency):
        if media_index is None and fila[5]>=location:
            media_index=index

    lim_inf_exac = frecuency[media_index][6]
    media_n=len(data)/2
    frec_last=frecuency[(media_index-1)][3]
    frec=frecuency[media_index][3]
    return round(lim_inf_exac+((media_n-frec_last)/frec)*(amplitude), len_digits)
