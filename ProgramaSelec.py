# Programa principal
afirmacion = True
Bienvenida = " gestiona los perfiles laborales"
inventario = []
candidatos = []

Menu = """
-------------------------------------------------
|                                               |
           Gestor Hojas de Vida                 |
|-----------------------------------------------|
|                                               |
|           1. Agregue su oferta                |
|           2. Edite la oferta                  |
|           3. Elimine la oferta                |
|           4. Registre su candidato            |
|           5. Asigne perfil                    |
|           6. Salir                            |
|-----------------------------------------------|
"""

print(Bienvenida)

def oferta_add():
    print("Ha seleccionado la opción 1: Agregue su oferta")
    nombre = input("Nombre de la oferta: ")
    experiencia = input("Experiencia necesaria: ")
    salario = input("Salario ofrecido: ")
    detalles = input("Detalles de la oferta: ")
    requisitos = input("Requisitos para aplicar: ")
    oferta = {
        "Nombre": nombre,
        "Experiencia": experiencia,
        "Salario": salario,
        "Detalles": detalles,
        "Requisitos": requisitos
    }
    inventario.append(oferta)
    print("Oferta agregada exitosamente.")

def editar_oferta():
    print("Ha seleccionado la opción 2: Editar oferta")
    nombre = input("Ingrese el nombre de la oferta que desea editar: ")
    encontrada = False
    for oferta in inventario:
        if oferta["Nombre"] == nombre:
            print("Oferta encontrada. Ingrese los nuevos datos.")
            oferta["Experiencia"] = input("Nueva experiencia: ")
            oferta["Salario"] = input("Nuevo salario: ")
            oferta["Detalles"] = input("Nuevos detalles: ")
            oferta["Requisitos"] = input("Nuevos requisitos: ")
            print("Oferta actualizada.")
            encontrada = True
    if not encontrada:
        print("Oferta no encontrada.")

def eliminar_oferta():
    print("Ha seleccionado la opción 3: Eliminar oferta")
    nombre = input("Ingrese el nombre de la oferta que desea eliminar: ")
    eliminada = False
    for oferta in inventario[:]:
        if oferta["Nombre"] == nombre:
            inventario.remove(oferta)
            print("Oferta eliminada.")
            eliminada = True
    if not eliminada:
        print("Oferta no encontrada.")

def registrar_candidato():
    print("Ha seleccionado la opción 4: Registrar candidato")
    nombre = input("Nombre del candidato: ")
    experiencia = input("Experiencia del candidato: ")
    habilidades = input("Habilidades del candidato: ")
    candidato = {
        "Nombre": nombre,
        "Experiencia": experiencia,
        "Habilidades": habilidades,
        "Asignado": "" 
    }
    candidatos.append(candidato)
    print("Candidato registrado exitosamente.")

def asignar_perfil():
    print("Ha seleccionado la opción 5: Asignar perfil")
    nombre_candidato = input("Nombre del candidato: ")
    nombre_oferta = input("Nombre de la oferta: ")
    encontrado_candidato = False
    for candidato in candidatos:
        if candidato["Nombre"] == nombre_candidato:
            encontrado_candidato = True
            encontrado_oferta = False
            for oferta in inventario:
                if oferta["Nombre"] == nombre_oferta:
                    candidato["Asignado"] = oferta["Nombre"]
                    print(f"Candidato {candidato['Nombre']} asignado a la oferta {oferta['Nombre']}.")
                    encontrado_oferta = True
            if not encontrado_oferta:
                print("Oferta no encontrada.")
    if not encontrado_candidato:
        print("Candidato no encontrado.")


while afirmacion:
    print(Menu)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        oferta_add()
    elif opcion == "2":
        editar_oferta()
    elif opcion == "3":
        eliminar_oferta()
    elif opcion == "4":
        registrar_candidato()
    elif opcion == "5":
        asignar_perfil()
    elif opcion == "6":
   
        print("Gracias por usar nuestro gestor de hojas de vida. Esperamos hayas encontrado la persona idónea.¡Hasta pronto!")
        afirmacion = False  
    else:
        print("Opción inválida. Intente nuevamente.")




        

