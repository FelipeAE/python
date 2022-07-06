meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
numero = -1
while(numero!=0):
    numero = int(input("Ingresa un numero: "))
    if(numero==0):
        break
    else:
        if(numero>=1 and numero<=len(meses)):
            print(meses[numero-1])
        else:
            print("Ingresa un numero entre 1 y ",len(meses))