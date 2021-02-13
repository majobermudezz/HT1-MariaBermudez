print("Cual es tu nombre?")
texto=input().lower()
print("Ingresa tu sexo ")
texto2=input().lower()
if texto2=="mujer":
    if texto<"m":
        print("Su grupo es el A")
    else:
        print("Su grupo es el B")
if texto2=="hombre":
    if texto>"n":
        print("Su grupo es el A")
    else:
        print("Su grupo es el B")