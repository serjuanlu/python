"""
Escribe un programa que a partir de información de un donante determine si
puede donar sangre.
"""

ayuno = input("¿Ha comido algo? Responda: si/no")
edad = int(input("Dígame su edad: "))
peso = int(input("Dígame su peso: "))
diastolica = int(input("Dígame el valor de su tensión diastólica: "))
sistolica = int(input("Dígame el valor de su tensión sistólica: "))
pulso = int(input("Dígame el valor de su frecuencia cardíaca: "))
sexo = input("Es hombre o mujer?")
hemo = float(input("Dígame el valor de su hemoglobina: "))
plaquetas = int(input("Dígame el valor de sus plaquetas: "))
proteinas = int(input("Dígame la cantidad de proteínas totales: "))

if ayuno == "no":
    if edad >= 18 and edad <= 65:
        if peso > 50:
            if (diastolica >= 50 and diastolica <= 100) and (
                sistolica >= 90 and sistolica <= 180
            ):
                if pulso >= 50 and pulso <= 110:
                    if pulso >= 50 and pulso <= 110:
                        if sexo == "hombre":
                            if hemo > 13.5:
                                if plaquetas > 150000:
                                    if proteinas > 6:
                                        print("Puede donar sangre.")
                                    else:
                                        print("No puede donar sangre.")
                                else:
                                    print("No puede donar sangre.")
                            else:
                                print("No puede donar sangre.")
                        else:
                            if hemo > 12.5:
                                if plaquetas > 150000:
                                    if proteinas > 6:
                                        print("Puede donar sangre.")
                                    else:
                                        print("No puede donar sangre.")
                                else:
                                    print("No puede donar sangre.")
                            else:
                                print("No puede donar sangre.")
                    else:
                        print("No puede donar sangre.")
                else:
                    print("No puede donar sangre.")
            else:
                print("No puede donar sangre.")
        else:
            print("No puede donar sangre.")
    else:
        print("No puede donar sangre.")
else:
    print("No puede donar sangre.")

'''
# Evaluar si puede donar sangre
puede_donar = (
    ayuno == "no"
    and 18 <= edad <= 65
    and peso > 50
    and 50 <= diastolica <= 100
    and 90 <= sistolica <= 180
    and 50 <= pulso <= 110
    and ((sexo == "hombre" and hemo > 13.5) or (sexo == "mujer" and hemo > 12.5))
    and plaquetas > 150000
    and proteinas > 6
)

# Mostrar el resultado
if puede_donar:
    print("Puede donar sangre.")
else:
    print("No puede donar sangre.")
'''