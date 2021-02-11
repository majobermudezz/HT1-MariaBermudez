a = int(input("ingrese el numero: "))
def es_primo(a):
    contador = 0
    resultado = True
    for i in range(1 , a+1):
        if (a % i == 0):
            contador +=1
        if (contador > 2):
            resultado = False
            break
    return resultado  
if(es_primo(a)== True):
    print( "el numero es primo")
else:
    print("el numero no es primo")
            