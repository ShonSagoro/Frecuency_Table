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
    print(f"el valor da . decimal: {r % k == 0}")
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

    len_decimal = (
        get_digits(variation_unit)
        if get_digits(variation_unit) != 0
        else 1
    )
    for i in range(0, numberClasses):
        lim_sup = lim_inf + amplitude - variation_unit
        frequency = get_frecuency_range(data, lim_inf, lim_sup);
        frequency_table.append(
            [
                chr(65 + i),
                round(lim_inf, len_decimal),
                round(lim_sup, len_decimal),
                round(frequency, len_decimal),
                round((lim_sup + lim_inf) / 2, len_decimal),
                round(lim_inf - (variation_unit / 2), len_decimal),
                round(lim_sup + (variation_unit / 2), len_decimal),
                round(frequency/len(data), len_decimal),
                round((frequency/len(data))*100, len_decimal),
            ]
        )
        lim_inf = lim_sup + variation_unit

    return frequency_table


def get_frecuency_range(data: list, limInf: Decimal, limSup: Decimal):
    frecuency = 0
    for number in data:
        if number <= limSup and number >= limInf:
            frecuency += 1
    return frecuency


def print_frecuency_table(data: list):
    print(
        "|{:<8}|{:<15}|{:<15}|{:<10}|{:<20}|{:<18}|{:<18}|{:<18}|{:<18}|".format(
            "Clase",
            "Límite Inf.",
            "Límite Sup.",
            "Frec.",
            "Marca d Clases",
            "Lim Inf Exac",
            "Lim Sup Exac",
            "Frec Rel prop",
            "Frec Rel %",
        )
    )
    print(
        "|{:<8}|{:<15}|{:<15}|{:<10}|{:<20}|{:<18}|{:<18}|{:<18}|{:<18}|".format(
            "---", "---", "---", "---", "---", "---", "---", "---", "---"
        )
    )
    for i in data:
        print(
            "|{:<8}|{:<15}|{:<15}|{:<10}|{:<20}|{:<18}|{:<18}|{:<18}| % {:<18}|".format(
                i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]
            )
        )
