import os
from regexparser import to_postfix
from arbol import build_syntax_tree, generate_ast_graph
from afdgenerador import compute_followpos, generate_afd
from afdminimizador import minimize_afd
from verificador import validate_string
import re 


print("¡Generador de AFD desde una expresión regular 👨🏻‍💻")

while True:
    regex = input("\nIngrese la expresión regular, si desea finalizar ingrese salir: ")
    if regex.lower() == 'salir':
        print("¡Generador de AFD! ")
        break


    postfix = to_postfix(regex + "#")
    root, positions = build_syntax_tree(postfix)
    followpos = compute_followpos(root, positions)

    #Arreglo de caracteres no permitidos
    regex_sanitized = re.sub(r'[<>:"/\\|?*]', '_', regex) 
    regex_folder = f"resultados_images/{regex_sanitized}"
    os.makedirs(regex_folder, exist_ok=True)


    # Generar AST y guardarlo
    generate_ast_graph(root).render(f"{regex_folder}/ast", format="png", cleanup=True)

    # Generar AFD y guardarlo
    afd, afd_dict = generate_afd(root, positions, followpos)
    afd.render(f"{regex_folder}/afd", format="png", cleanup=True)

   
    minimized_afd = minimize_afd(afd_dict)
    minimized_afd.render(f"{regex_folder}/afd_minimized", format="png", cleanup=True)

    print(f"\n Diagramas generados en: {regex_folder}")
    
    while True:
        string = input("\nIngrese una cadena para verificar (si desea cambiar de regex escriba cambio: ")
        if string.lower() == 'cambio':
            break
        
        if validate_string(afd_dict, string):
            print(f"- La cadena '{string}' ES ACEPTADA 🟢 por la expresión regular.")
        else:
            print(f"- La cadena '{string}' FUE RECHAZADA 🔴 por la expresión regular.")

print("\nFINALIZACION")
