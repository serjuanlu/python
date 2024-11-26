import string

entrada1 = input("Introduce la primera palabra ")
entrada2 = input("Introduce la segunda palabra para ver si palindroma ")
# le doy la vuelta a la entrda dos para que no tenga que hacerlo tu manualmente
entrada2 = entrada2[::-1]
letras = string.ascii_letters + "ÑñáÁéÉíÍóÓúÚ"
textoFiltrado1 = ""
textoFiltrado2 = ""
salir = False

for t in entrada1:
    if t in letras:
        textoFiltrado1 = textoFiltrado1 + t

for t in entrada2:
    if t in letras:
        textoFiltrado2 = textoFiltrado2 + t

while salir == False:
    entrada = input("¿Quieres tener en cuenta las mayusculas? si/no ")
    entrada.lower()

    if entrada == "si":
        if textoFiltrado1 == textoFiltrado2[::-1]:
            print("Si son palidromas entre ellas")
            salir = True
        else:
            print("No son palindromas entre si")
            salir = True
    elif entrada == "no":
        textoFiltrado1.lower
        textoFiltrado2.lower
        if textoFiltrado1 == textoFiltrado2[::-1]:
            print("Si son palidromas entre ellas")
            salir = True
        else:
            print("No son palindromas entre si")
            salir = True
    else:
        print("opcion incorrecta vuelva a intentarlo si o no.")
        salir = True
