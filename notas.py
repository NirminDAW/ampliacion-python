def calcularNotaMaxima(notaPrimeraEval, notaSegundaEval, notaTerceraEval):
    return max(notaPrimeraEval, notaSegundaEval, notaTerceraEval)

def calcularNotaMinima(notaPrimeraEval, notaSegundaEval, notaTerceraEval):
    return min(notaPrimeraEval, notaSegundaEval, notaTerceraEval)

def calcularNotaMedia(notaPrimeraEval, notaSegundaEval, notaTerceraEval):
    return (notaPrimeraEval + notaSegundaEval + notaTerceraEval) / 3

notaPrimeraEval = float(input("Introduce la nota de la primera evaluación: "))
notaSegundaEval = float(input("Introduce la nota de la segunda evaluación: "))
notaTerceraEval = float(input("Introduce la nota de la tercera evaluación: "))

notaMaxima = calcularNotaMaxima(notaPrimeraEval, notaSegundaEval, notaTerceraEval)
notaMinima = calcularNotaMinima(notaPrimeraEval, notaSegundaEval, notaTerceraEval)
notaMedia = calcularNotaMedia(notaPrimeraEval, notaSegundaEval, notaTerceraEval)

print("La nota máxima es:", notaMaxima)
print("La nota mínima es:", notaMinima)
print("La nota media es:", notaMedia)

