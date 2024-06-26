import csv
lista_trabajadores=[]

def ingresar_nombre():
    while True:
        nombre=input("Ingrese el nombre: ")
        if any(caracter.isalpha() for caracter in nombre) and len(nombre) >=2:
            print("Registrado con exito...")
            return nombre
        if any(caracter.isdigit() for caracter in nombre):
            print("Ingrese nuevamente...")
        else:
            print("Ingrese nuevamente...")

def ingresar_apellido():
    while True:
        apellido=input("Ingrese el apellido: ")
        if any(caracter.isalpha() for caracter in apellido) and len(apellido) >=2:
            print("Registrado con exito...")
            return apellido
        if any(caracter.isdigit() for caracter in apellido):
            print("Ingrese nuevamente...")
        else:
            print("Ingrese nuevamente...")
    
def ingresar_cargo():
    while True:
        cargo=input("Ingresa el cargo Mesero, Cocinero, Cajero)")
        if any(caracter.isalpha() for caracter in cargo) and len(cargo) >=2:
            if cargo.upper() == "MESERO":
                print("Cargo ingresado...")
                return cargo
            if cargo.upper() =="COCINERO":
                print("Cargo ingresado...")
                return cargo
            if cargo.upper() =="CAJERO":
                print("Cargo ingresado...")
                return cargo
            else:
                print("Ingrese un cargo disponible (Mesero, Cocinero, Cajero)")
        else:
            print("Ingrese un cargo disponible (Mesero, Cocinero, Cajero)")

def ingresar_sueldo():
    global sueldo
    sueldo=input("Ingrese el sueldo sin signo ($): ")
    if sueldo.isdigit():
        sueldo=int(sueldo)
        print("Sueldo ingresado correctamente...")
        return sueldo
    else:
        print("ingrese nuevamente...")
def descuento_sueldo():
    global sueldo
    liquido=0
    liquido += sueldo
    liquido *=0.9
    return liquido


def mostrar_trabajadores(lista_trabajadores):
    for item in lista_trabajadores:
        print(item)
    

def ingresar_trabajador(lista_trabajadores):
    nombre=ingresar_nombre()
    apellido=ingresar_apellido()
    cargo=ingresar_cargo()
    sueldo=ingresar_sueldo()
    liquido=descuento_sueldo()

    lista_trabajador=[nombre,apellido,cargo,sueldo,liquido]
    lista_trabajadores.append(lista_trabajador)

def imprimir_lista(lista_trabajadores):
    nombre_archivo=input("Ingrese el nombre que desea ponerle al archivo")
    nombre_archivo += ".csv"
    
    with open(nombre_archivo,"w",newline='')as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow([["Nombre","Apellido","Cargo","Sueldo Bruto","Sueldo Liquido"]])
        for item in lista_trabajadores:
            escritor.writerow(item)
    print("Se imprimio correctamente")

def menu():
    lista_trabajadores=[]
    while True:
        print('''
    1)Ingresar
    2)Mostrar trabajadores
    3)Salir''')
        rsp=input("Ingrese una opcion: ")
        if rsp.isdigit():
            rsp=int(rsp)
            if rsp==1:
                ingresar_trabajador(lista_trabajadores)
            elif rsp==2:
                mostrar_trabajadores(lista_trabajadores)
            elif rsp==3:
                imprimir_lista(lista_trabajadores)
            elif rsp==4:
                print("Saliendo...")
                break
            else:
                print("Ingrese una opcion valida")
        else:
            print("Ingrese una opcion valida")
menu()