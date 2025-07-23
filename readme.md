# Maximum Subarray Problem

---

## **1. Introducción**

En el contexto del análisis algorítmico, uno de los problemas clásicos con aplicaciones prácticas en finanzas, biología computacional y procesamiento de señales es el denominado **problema de la subsecuencia contigua de máxima suma** (*Maximum Subarray Problem*). Este problema consiste en encontrar una subsecuencia contigua dentro de un arreglo unidimensional de números enteros que maximice la suma de sus elementos.

En este caso en particular un jugador registra sus ganancias o pérdidas diarias en partidas de póquer, y desea determinar el intervalo de días consecutivos en los que su beneficio acumulado fue máximo. Se resuelve el problema mediante la técnica algorítmica de **Divide y Vencerás** (*Divide and Conquer*), garantizando una solución correcta y eficiente, conforme a los requisitos establecidos. Aunque como se señala posteriormente no es la mejor estratégia

---

## **2. Planteamiento del Problema**

Sea  A[1..N]  un arreglo de  N  enteros, donde cada elemento  A[i]  representa la ganancia (si positivo) o pérdida (si negativo) del jugador en el día  i . El objetivo es encontrar un par de índices  (i, j) , con  1 ≤ i ≤ j≤ N , tales que la suma:

S(i,j) = k=i ∑ j ​A[k]


sea **máxima** sobre todos los posibles subarreglos contiguos de  A .

Como se indica en el enunciado, aunque el beneficio total del mes es negativo (−47 €), existe un subintervalo (días 16 al 26) en el que el jugador obtuvo una ganancia neta de 105 €, lo cual representa la mejor estrategia retrospectiva de juego.

---

## **3. Diseño del Algoritmo: Estrategia Divide y Vencerás**

### **3.1. Fundamento Teórico**

La técnica **Divide y Vencerás** consiste en descomponer un problema de tamaño  N  en subproblemas más pequeños, resolverlos recursivamente, y luego combinar sus soluciones para obtener la solución del problema original.

Aplicado al problema de la subsecuencia máxima, el enfoque se basa en dividir el arreglo en dos mitades y considerar tres posibles casos para la subsecuencia óptima:

1. **Está completamente en la mitad izquierda** del arreglo.
2. **Está completamente en la mitad derecha** del arreglo.
3. **Cruza el punto medio**, extendiéndose desde la mitad izquierda hacia la derecha.

La solución final será el subarreglo que produzca la mayor suma entre estos tres casos.

### **3.2. Descripción del Algoritmo**

El algoritmo se implementa mediante una función recursiva `solve_divide_conquer(low, high)` que devuelve una tupla  (i, j, S) , donde  i  y  j  son los índices del subarreglo óptimo (en formato 0-basado), y  S  es la suma máxima.

#### **Caso base:**
Si  {low} = {high} , el subarreglo consiste en un solo elemento, por lo que se devuelve  ({low}, {high}, A[{low}]) .

#### **Caso recursivo:**
1. Calcular el punto medio:  {mid} = ⌊(low+high​)/2⌋.
2. Resolver recursivamente:
   - Izquierda:  (i_l, j_l, S_l) = {solve}({low}, {mid}) 
   - Derecha:  (i_r, j_r, S_r) = {solve}({mid}+1, {high}) 
3. Calcular el subarreglo de máxima suma que cruza el centro:
   - Suma máxima desde `mid` hacia la izquierda.
   - Suma máxima desde `mid+1` hacia la derecha.
   - Combinar ambas para obtener  (i_c, j_c, S_c) .

#### **Combinación:**
Se selecciona el caso con mayor suma:

max(S_l, S_r, S_c)


El cálculo del subarreglo cruzado se realiza en tiempo lineal mediante un recorrido hacia la izquierda y otro hacia la derecha desde el centro.

---

## **4. Implementación en Python con Programación Orientada a Objetos**

Para encapsular el estado y facilitar la reutilización, se implementó una clase `MaxSubarraySolver` que contiene los métodos necesarios para resolver el problema.

### **Estructura de la Clase**

```python
class MaxSubarraySolver:
    def __init__(self, gains):
        self.gains = gains
        self.n = len(gains)

    def solve_divide_conquer(self, low=0, high=None):
        ...

    def _max_crossing_subarray(self, low, mid, high):
        ...

    def solve(self):
        ...
```
---


## **6. Análisis de Complejidad**

### **6.1. Complejidad Temporal**

La recurrencia del algoritmo es:


T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)
\]

-  2T(n/2) : dos llamadas recursivas sobre mitades del arreglo.
-  \Theta(n) : cálculo del subarreglo cruzado (recorrido lineal desde el centro).

Aplicando el **Teorema Maestro**, esta recurrencia pertenece al **Caso 2**, donde  f(n) = \Theta(n) = \Theta(n^{\log_b a})  con  a=2 ,  b=2 ,  \log_b a = 1 .

Por tanto:


T(n) = \Theta(n \log n)
\]

### **6.2. Complejidad Espacial**

- **Espacio adicional:**  \Theta(1)  (variables locales en los bucles).
- **Profundidad de recursión:**  \Theta(\log n)  (debido a la división binaria).

Entonces, el espacio total es:


\Theta(\log n)
\]

---

## **7. Discusión y Consideraciones**

- Aunque existe un algoritmo más eficiente (Kadane,  O(n) ), el problema exige explícitamente el uso de **Divide y Vencerás**, por lo que se respetó la restricción.
- El uso de **multithreading** fue considerado, pero **no recomendado** en Python debido al **Global Interpreter Lock (GIL)**, que limita el paralelismo en tareas CPU-intensive.
- Alternativas como `multiprocessing` podrían explotar el paralelismo real, pero con alto costo de sobrecarga para problemas pequeños o medianos.

---

## **8. Conclusión**

Se ha diseñado, implementado y analizado un algoritmo basado en la técnica **Divide y Vencerás** para resolver el problema de encontrar la subsecuencia contigua de máxima suma. La solución cumple con los requisitos del enunciado y permite determinar el intervalo óptimo de días en los que un jugador maximiza sus ganancias.

El algoritmo tiene una **complejidad temporal de  Θ(nlogn) ** y espacial de  Θ(logn) , siendo eficiente y correcto. La implementación orientada a objetos facilita su integración en sistemas más grandes y mejora su mantenibilidad.

---

## **9. Referencias**

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
- Bentley, J. (1984). *Programming Pearls*. Addison-Wesley.







Universidad de Oriente 
Núcleo:  Anzoátegui
Departamento de Computación y Sistemas 
Asignatura:  Taller de Análisis y Diseño de Algoritmos
Autor: Jesús Alcala | C.I: 31.205.548
