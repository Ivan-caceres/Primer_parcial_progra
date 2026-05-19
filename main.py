from validaciones import validar_contraseña
from analisis import (
    evaluar_seguridad, contar_tipos, buscar_caracter, 
    invertir_contraseña, es_palindromo, ordenar_caracteres
)
from estadisticas import generar_reporte

def ejecutar_menu() -> None:
    """
    Maneja la interfaz de consola y el bucle principal de control del programa.

    Return:
        None
    """
    contraseña = ""
    contraseña_cargada = False
    opcion = ""
    
    while opcion != "9":
        print("\n")
        print("=="*26)
        print("🖥 BIENVENIDO AL SISTEMA DE PROCESAMIENTO DE CLAVES 🖥")
        print("=="*26)
        print("\n")
        print("1. Ingresar contraseña 🔑")
        print("2. Validar nivel de seguridad 👮‍♂️")
        print("3. Contar tipos de caracteres 🈵🅰2️⃣")
        print("4. Buscar caracter especifico 🔍")
        print("5. Mostrar contraseña invertida 🔁")
        print("6. Generar reporte estadistico 📊")
        print("7. Verificar si es palindromo ✔")
        print("8. Ordenar caracteres de la contraseña ↗ ↘")
        print("9. Salir 🛑")
        print("\n")
        print("=="*26)
        print("\n")
        
        opcion = input("Seleccione una opcion (1-9): ")
        print("\n")
        
        if opcion == "1":
            ingreso = input("Ingrese la contraseña: ")
            if validar_contraseña(ingreso):
                contraseña = ingreso
                contraseña_cargada = True
                print("\n✅¡Contraseña aceptada!✅")
            else:
                print("❌No se pudo cargar la contraseña.❌")
                
        elif (opcion == "2" or opcion == "3" or opcion == "4" or 
            opcion == "5" or opcion == "6" or opcion == "7" or opcion == "8"):
            
            if not contraseña_cargada:
                print("🚨Error: Primero debe ingresar una contraseña valida mediante la opcion 1.🚨")
            else:
                match opcion:
                    case "2":
                        nivel = evaluar_seguridad(contraseña)
                        print("=="*26)
                        print("\n")
                        print(f"Nivel de seguridad: {nivel}")
                    
                    case "3":
                        contar_tipos(contraseña)
                        
                    case "4":
                        caracter = input("Ingrese el carácter a buscar: ")
                        print("\n")
                        if len(caracter) != 1:
                            print("🚨Error: Ingrese estrictamente un solo carácter.🚨")
                        else:
                            buscar_caracter(contraseña, caracter)
                            
                    case "5":
                        invertida = invertir_contraseña(contraseña)
                        print("=="*26)
                        print(f"Contraseña invertida: {invertida}")
                        
                    case "6":
                        generar_reporte(contraseña)
                        
                    case "7":
                        print("=="*26)
                        if es_palindromo(contraseña):
                            print("\nLa contraseña es un palíndromo.✅")
                        else:
                            print("\nLa contraseña NO es un palíndromo.❌")
                            
                    case "8":
                        print("1. Orden Ascendente ↗")
                        print("2. Orden Descendente ↘")
                        modo = input("\nSeleccione orden: ")
                        if modo == "1":
                            print("=="*26)
                            print(f"\nResultado: {ordenar_caracteres(contraseña, True)}")
                        elif modo == "2":
                            print("=="*26)
                            print(f"\nResultado: {ordenar_caracteres(contraseña, False)}")
                        else:
                            print("\nOpcion invalida.")
                            
        elif opcion == "9":
            print("\nSaliendo del programa...")
        else:
            print("🚨Opcion invalida, intente de nuevo.🚨")

if __name__ == "__main__":
    ejecutar_menu()