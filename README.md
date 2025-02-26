# Simulación de un Autómata desde una Expresión Regular

## Expresión Regular

Dada una expresión regular, el objetivo es convertirla en un autómata finito no determinista (AFN), transformarlo en un autómata finito determinista (AFD), minimizarlo y simular su comportamiento con cadenas de entrada.

---

## Pasos de Construcción

### **1. Convertir Expresión Regular de Infija a Postfija**

- Se utiliza el algoritmo *Shunting Yard* para convertir la expresión infija a notación postfix.
- Se emplea la función `toPostFix` en `shunYard.py`.

---

### **2. Construcción del Autómata Finito No Determinista (AFN)**

- Se construye un AFN a partir de la notación postfix usando `toAFN` en `regexToAFN.py`.
- Se utiliza una pila para evaluar los operadores de concatenación (`.`), unión (`+`) y cierre de Kleene (`*`).

---

### **3. Conversión del AFN a AFD**

- Se emplea `fromAFNToAFD` en `AFNToAFD.py`.
- Se calcula el cierre-ε y se generan los estados del AFD a partir del AFN.

---

### **4. Minimizar el AFD**

- Se minimiza el AFD usando `minimize_afd` en `minimizeAFD.py`.
- Se agrupan estados equivalentes y se redefinen las transiciones.

---

### **5. Generación Visual de los Autómatas**

- Se generan diagramas de los autómatas usando `generate_graph` en `simulate.py`.
- Los autómatas se almacenan en `automaton_graphs/`.

---

### **6. Simulación de Cadenas en el AFD Minimizado**

- Se utiliza `simulate_regexp_process` en `simulate.py`.
- Se verifica si una cadena es aceptada por el autómata minimizado.

---

## Compilación del Programa

- Carpeta: `parte2.procesador`

---

# Construcción de un DFA directamente desde una Expresión Regular (r.e)

## Expresión Regular

Dada la expresión regular **r = (a|b)*abb**, el objetivo es construir un DFA directamente a partir del árbol sintáctico generado.

---

## Pasos de Construcción

### **1. Aumentar la Expresión Regular**

- Se añade un símbolo especial `#` al final para marcar el fin de la cadena.

---

### **2. Conversión a Notación Postfix**

- Se utiliza el algoritmo *Shunting Yard* para convertir la expresión infija a notación postfix.

---

### **3. Construcción del Árbol Sintáctico**

- Se crea un árbol sintáctico a partir de la notación postfix.
- Se asignan posiciones a las hojas y se calculan `nullable`, `firstpos`, y `lastpos`.

---

### **4. Cálculo de `followpos`**

- Se computan los `followpos` recorriendo el árbol y aplicando las reglas en `compute_followpos`.

---

### **5. Generación del AFD**

- Se crean los estados del AFD.
- Se define un estado inicial a partir de `firstpos` de la raíz.
- Se iteran las transiciones según `followpos`.

---

### **6. Minimización del AFD**

- Se utiliza minimización para reducir el número de estados.

---

### **7. Simulación del AFD**

- La función `validate_string` en `verificador.py` verifica si una cadena es aceptada por el AFD.

---

### **8. Generación Visual de los Autómatas**

- Se usan funciones de Graphviz para generar visualizaciones:
  - Árbol sintáctico.
  - AFD.
  - AFD minimizado.

---

## Compilación del Programa

- Ejecutar `Main.py`

---

## Referencias

- Proyecto base de referencia: [RegExpAutomata](https://github.com/ElrohirGT/RegExpAutomata)
- Computerphile. (2018, October 30). Regular Expressions: How do they work? [Video]. YouTube. [Ver Video](https://www.youtube.com/watch?v=gjIDl44-omU)
- Aho, A. V., Lamxa, M. S., Sethi, R., & Ullman, J. D. (2008). *Compiladores: Principios, técnicas y herramientas* (2a ed.). Pearson Educación.
