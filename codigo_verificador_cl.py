Multiplication = [2,3,4,5,6,7,2,3,4,5,6,7,2,3]

def calcular_verificador(rut:str):
    calculo = 0
    contador = 0

    for digit in rut:
        calculo += int(digit) * Multiplication[contador]
        contador += 1
    
    base_sum = calculo
    calculo /= 11
    restar = int(calculo) * 11
    restar = base_sum - restar
    calculo = 11 - restar

    if calculo == 11:
        calculo = 0
    elif calculo == 10:
        calculo = "K"

    return calculo

def run():
    rut = input("Ingrese todos los numeros del rut sin el codigo verificador: \n")
    rut = rut[::-1]
    codigo_verificador = calcular_verificador(rut)
    print(f"El codigo verificador es: {codigo_verificador}")

if __name__ == '__main__':
    run()