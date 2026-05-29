Proyecto de curso: Calculando el plan de riego óptimo de una finca
Integrantes: 
   VENUS PAIPILLA - 202343803  venus.paipilla@correounivalle.edu.co
   DANIEL ARIAS CASTRILLÓN - 202222205  daniel.arias.castrillon@correounivalle.edu.co
   NICOLAS ENRIQUE GRANADA FERNANDEZ - 202310107  granada.nicolas@correounivalle.edu.co

=====================================================================

1. ARCHIVOS ENTREGADOS
---------------------------------------------------------------------
- main.py: Código fuente principal en Python. Contiene la lógica interactiva por consola y las implementaciones de los 3 algoritmos (roFB, roV, roPD).
- guia_proyecto_2.docx / pdf: Informe del proyecto con análisis de complejidad, optimalidad y ejemplos.
- main.exe: Programa ejecutable interactivo.
- Readme.txt: Este archivo de instrucciones.
- entrada_ejemplo.txt: Archivo de prueba con el formato de entrada especificado.

2. REQUISITOS
---------------------------------------------------------------------
- Si deseas ejecutar el código fuente directamente, necesitas Python 3.x instalado.
- Si vas a usar el ejecutable (main.exe), no necesitas instalar Python (solo compatible con Windows).

3. INSTRUCCIONES PARA EJECUTAR LA APLICACIÓN
---------------------------------------------------------------------
Opción A) Usar el Ejecutable:
1. Haz doble clic en "main.exe" o ejecútalo desde una terminal de comandos.
2. Sigue las opciones del menú interactivo.

Opción B) Usar el Código Fuente:
1. Abre una terminal o consola de comandos.
2. Navega hasta la carpeta del proyecto.
3. Ejecuta el comando: python main.py
4. Sigue las opciones del menú interactivo.

4. INSTRUCCIONES PARA COMPILAR EL EJECUTABLE (En caso de necesitar generarlo de cero)
---------------------------------------------------------------------
1. Instalar pyinstaller: 
   pip install pyinstaller
2. Ejecutar el empaquetado:
   pyinstaller --onefile main.py
3. El archivo main.exe se generará dentro de la carpeta "dist".

5. USO DEL PROGRAMA (INTERFAZ INTERACTIVA)
---------------------------------------------------------------------
El programa ofrece un menú con 8 opciones:
1. Leer finca desde archivo: Pedirá la ruta de un archivo .txt. Las entradas deben seguir el formato del enunciado (primera línea N, siguientes líneas ts,tr,p,rp separadas por comas o espacios).
2. Visualizar entradas: Muestra en consola cómo se almacenaron internamente los tablones leídos.
3. Calcular con roFB: Usa Fuerza Bruta. (Advertencia: Lento para más de 10 tablones).
4. Calcular con roV: Usa Algoritmo Voraz (EDF + Prioridad).
5. Calcular con roPD: Usa Programación Dinámica con bitmasking.
6. Visualizar salida calculada: Muestra en pantalla el costo óptimo y el orden (los índices de los tablones).
7. Escribir salida en archivo: Pedirá un nombre de archivo (ej. salida.txt) y escribirá el costo seguido de la permutación, línea por línea.
8. Salir: Cierra el programa.
