import os, time
os.system("cls")

banderaMenu = True
pacientes = []
while banderaMenu:
    print("1. Registrar Paciente")
    print("2. Atencion Paciente")
    print("3. Gestionar Paciente")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese una opcion\n"))
        if opcion == 1:
            banderaPaciente = True
            while banderaPaciente:
                banderaRut = True
                banderaEdad = True
                print("***Registrar Paciente***")
                os.system("cls")
                while banderaRut:
                    try:
                        rut = int(input("Ingrese rut\n"))
                        while rut < 5000000 or rut > 30000000:
                            rut = int(input("Ingrese rut nuevamente, ingrese un rut en rango 5M y 30M\n"))
                            banderaRut = False       
                    except:
                        print("en campo rut no se aceptan caracteres")
                nombre = input("Ingrese Nombre\n")
                while nombre == "":
                    nombre = input("Ingrese nombre nuevamente, no puede venir vacio el campo\n")
                direccion = input("Ingrese dirección\n")
                while direccion == "":
                    direccion = input("Ingrese dirección, campo no puede venir vacio\n")
                correo = input("Ingrese un correo\n")
                while '@' not in correo:
                    correo = correo = input("Ingrese un correo, recuerde que debe agregar el @\n")
                while banderaEdad:
                    try:
                        edad = int(input("Ingrese edad\n"))
                        while edad < 0 or edad > 110:
                            edad = int(input("Ingrese edad, debe estar en el rango entre 0 a 110\n"))
                        banderaEdad = False
                    except:
                        print("en campo edad no se aceptan caracteres")
                sexo = input("Ingrese Sexo\n").lower()
                while sexo != 'f' and sexo != 'm':
                    sexo = input("Ingrese sexo 'f' o 'm'\n").lower()
                ps = input("Ingrese prevision salud\n").lower()
                while ps != 'fonasa' and sexo != 'isapre':
                    ps = input("Ingrese prevision salud\n").lower()
                paciente = [rut, nombre, direccion, correo, edad, sexo, ps]
                pacientes.append(paciente)
                otroPaciente = int(input("Deseas agregar otro paciente? 1. Si  2. No\n"))
                if otroPaciente == 1:
                    continue
                else:
                    banderaPaciente = False
                print (paciente)
                x = input("enter para salir...")
        elif opcion == 2:
            print("***Atencion Paciente***")
            
        elif opcion == 3:
            print("***Gestionar Paciente***")
        elif opcion == 4:
            print("Ha salido del sistema...")
            x = input("enter para salir...")
            banderaMenu = False
        
        
        
    except:
        print("opcion no valida")