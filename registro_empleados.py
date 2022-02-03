from datetime import datetime

registros_entrada = {}
registros_salida = {}

dict_empleados = {
    1:{"name":"Juan", "NIF": "4987456Z", "clave":1602, "alta":0, "baja":0, "reporte":0}, 
    2:{"name":"Ismael", "NIF":"51286243S", "clave":2806, "alta":0, "baja":0, "reporte":0},  
    3:{"name":"Ainhoa", "NIF":"4689932R", "clave":4206 , "alta":0, "baja":0, "reporte":0}, 
    4:{"name":"Ysabel", "NIF":"4398431Z", "clave":4213 , "alta":0, "baja":0, "reporte":0}}

dict_claves = {
    1602:1, 
    2806:2, 
    3478:3,
    4206:4,
    4213:5}

menu00 = "="*20+"Registro de empleados"+"="*20+"\nC) Consultar\nR) Registro\nT) Tabla de empleados\nO) Salir"

flag_00 = True
flag_01 = False
flag_02 = False
flag_03 = False

while True:
    if not flag_00 and not flag_01 and not flag_02 and not flag_03:
        break
    while flag_00:
        print(menu00)

        opcion = input("--Opción: ").upper()

        print()
        if not opcion.isalpha():
            print("===== Opción inválida =====\n")
        else:
            break
    
    if opcion == "C":
        flag_00 = False
        flag_01 = True
    elif opcion == "R":
        flag_00 = False
        flag_02 = True
    elif opcion == "T":
        flag_00 = False
        flag_03 = True
    elif opcion == "O":
        flag_00 = False



    while flag_01:
        while True:

            print("-"*20+"Consulta"+"-"*20)

            while True:            
                consulta = input("Introduzca su código de operador: ")
                if not consulta.isdigit():
                    print("===== Opción inválida =====\n")
                elif int(consulta)<1 or int(consulta)>5:
                    print("===== Opción inválida =====\n")
                else:
                    con = int(consulta)
                    break

            if not con in registros_entrada:
                print("No se ha registrado para entrar")
            elif not con in registros_salida:
                print("No se ha registrado para salir")

                while True:
                    save = input("Desea registrarse (S/N)? ").upper()
                    print()
                    if not save.isalpha():
                        print("===== Opción inválida =====\n")
                    else:
                        sv = save
                        break

                if sv == "S":
                    flag_00 = False
                    flag_01 = False
                    flag_02 = True
                elif sv == "N":
                    flag_02 = False
                    flag_01 = False
                    flag_00 = True
            break
        
        if len(registros_entrada) != 0 and con in registros_entrada:
            print("\n")
            print("-"*15+"Usuario:",dict_empleados[con]["name"]+"-"*15)
            print(f"Hora de entrada: {registros_entrada[con]}")
            print(f"Hora de salida: {registros_salida[con]}")
            print()
            flag_01 = False
            flag_00 = True
        else:
            flag_00 = False
            flag_01 = False
            flag_02 = True
                
    while flag_02:
        while True:

            while True:
                control = input("Registrarse para entrar o salir (E/S)? ").upper()
                print()
                if not control.isalpha():
                    print("===== Opción inválida =====\n")
                elif control == "E" or control == "S":
                    ctrl = control
                    break

            if ctrl == "E":

                print("-"*20+"Registro"+"-"*20)

                ok = False
                while True:
                    cod_operador = input("- Código de operador: ")
                    if not cod_operador.isdigit():
                        print("===== Opción inválida =====\n")
                    elif int(cod_operador)<1 or int(cod_operador)>5:
                        print("===== Opción inválida =====\n")
                    else:
                        cod_op = int(cod_operador)
                        break
            
                while ok == False:
                    if not cod_op in dict_empleados:
                        print("Número de empleado incorrecto")
                        cod_op = int(input("- Código de operador: "))
                        ok = False
                    else:
                        ok = True
                
                tipo_doc = input("Que tipo de documento posee (NIF/NIE)? ").upper()

                if tipo_doc == "NIF":
                    k = False
                    while k == False:
                        while True:
                            nif = input("- NIF del operador: ")
                            if not nif.isalnum():
                                print("===== Opción inválida =====\n===== Debe contener 7 números y una letra =====\n")
                            elif len(nif) < 8:
                                print("===== Opción inválida =====\n===== Debe contener 8 carácteres =====\n")
                            else:
                                nif_op = nif
                                break

                        if nif_op == dict_empleados[cod_op]["NIF"]:
                            k = True
                        else:
                            print("NIF incorrecto")
                            k = False

                elif tipo_doc == "NIE":
                    k = False
                    while k == False:
                        while True:
                            nif = input("- NIE del operador: ")
                            if not nif.startswith() and not nif.isalnum():
                                print("===== Opción inválida =====\n===== Debe contener una letra y 7 números  =====\n")
                            elif len(nif) < 8:
                                print("===== Opción inválida =====\n===== Debe contener 8 carácteres =====\n")
                            else:
                                nif_op = nif
                                break

                        if nif_op == dict_empleados[cod_op]["NIF"]:
                            k = True
                        else:
                            print("NIF incorrecto")
                            k = False

                paso = False
                while paso == False:
                    clave_operador = int(input("-- Clave de operador: "))

                    if clave_operador == dict_empleados[cod_op]["clave"]:
                        print("Clave correcta")
                        print()
                        print("Registro completado")
                        print()
                        paso = True
                    else:
                        print("Clave incorrecta")
                        paso = False

                registros_entrada[cod_op] = datetime.today().strftime('%H:%M:%S')
                dict_empleados[cod_op]["alta"] = datetime.today().strftime('%H:%M:%S')
                print("Código:",cod_op,"| Usuario:",dict_empleados[cod_op]["name"])
                print(f"Hora de entrada: {datetime.today().strftime('%A, %B %d, %Y')} | {registros_entrada[cod_op]}")
                print()
                

            if ctrl == "S":

                print("-"*20+"Registro"+"-"*20)
                ok = False
                while True:
                    cod_operador = input("- Código de operador: ")
                    if not cod_operador.isdigit():
                        print("===== Opción inválida =====\n")
                    elif int(cod_operador)<1 or int(cod_operador)>4:
                        print("===== Opción inválida =====\n")
                    else:
                        cod_op = int(cod_operador)
                        break
            
                while ok == False:
                    if not cod_op in dict_empleados:
                        print("Número de empleado incorrecto")
                        cod_op = int(input("- Código de operador: "))
                        ok = False
                    else:
                        ok = True
                        
                tipo_doc = input("Que tipo de documento posee (NIF/NIE)? ").upper()

                if tipo_doc == "NIF":
                    k = False
                    while k == False:
                        while True:
                            nif = input("- NIF del operador: ")
                            if not nif.isalnum():
                                print("===== Opción inválida =====\n===== Debe contener 7 números y una letra =====\n")
                            elif len(nif) < 8:
                                print("===== Opción inválida =====\n===== Debe contener 8 carácteres =====\n")
                            else:
                                nif_op = nif
                                break

                        if nif_op == dict_empleados[cod_op]["NIF"]:
                            k = True
                        else:
                            print("NIF incorrecto")
                            k = False

                elif tipo_doc == "NIE":
                    k = False
                    while k == False:
                        while True:
                            nif = input("- NIE del operador: ")
                            if not nif.startswith() and not nif.isalnum():
                                print("===== Opción inválida =====\n===== Debe contener una letra y 7 números  =====\n")
                            elif len(nif) < 8:
                                print("===== Opción inválida =====\n===== Debe contener 8 carácteres =====\n")
                            else:
                                nif_op = nif
                                break

                        if nif_op == dict_empleados[cod_op]["NIF"]:
                            k = True
                        else:
                            print("NIF incorrecto")
                            k = False

                for i in dict_empleados:
                    if cod_op == i:
                        print(f"- NIF del empleado: {nif}")

                paso = False
                while paso == False:
                    clave_operador = int(input("- Clave de operador: "))

                    if clave_operador == dict_empleados[cod_op]["clave"]:
                        print("Clave correcta")
                        print()
                        print("Registro completado")
                        print()
                        paso = True
                    else:
                        print("Clave incorrecta")

                registros_salida[cod_op] = datetime.today().strftime('%H:%M:%S')
                dict_empleados[cod_op]["baja"] = datetime.today().strftime('%H:%M:%S')

                print("Código:",cod_op,"| Usuario:",dict_empleados[cod_op]["name"])
                print(f"Hora de salida: {datetime.today().strftime('%A, %B %d, %Y')} | {registros_salida[cod_op]}")
                print()
                
            break
                
        flag_02 = False
        flag_00 = True
                
    while flag_03:
        while True:
            print("*"*45+"Tabla de empleados"+"*"*45+"\n"+"Código".ljust(20)+"Nombre".ljust(20)+"NIF".ljust(20) +"Alta".ljust(20) + "Baja".ljust(20) + "Reporte mensual".ljust(20) +"\n"+"-"*109)
            for i in dict_empleados:
                if i == 5:
                    break
                print(str(i).ljust(20)+str(dict_empleados[i]["name"]).ljust(20)+ str(dict_empleados[i]["NIF"]).ljust(20) + str(dict_empleados[i]["alta"]).ljust(20) + str(dict_empleados[i]["baja"]).ljust(20) + str(dict_empleados[i]["reporte"]).ljust(20))
            print()
            break

        input("<Pulsa ENTER para continuar>")
        print()
        flag_03 = False
        flag_00 = True