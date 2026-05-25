import sys
import itertools

class Tablon:
    def __init__(self, id, ts, tr, p, rp):
        self.id = id
        self.ts = ts
        self.tr = tr
        self.p = p
        self.rp = rp
    def __str__(self):
        return f"Tablon {self.id}: ts={self.ts}, tr={self.tr}, p={self.p}, rp={self.rp}"

def costo_tablon(tablon, t_inicio):
    ts, tr, p, rp = tablon.ts, tablon.tr, tablon.p, tablon.rp
    if t_inicio == rp:
        return ts - (t_inicio + tr)
    elif ts - tr >= t_inicio:
        return 2 * (ts - (t_inicio + tr))
    else:
        return 2 * p * ((t_inicio + tr) - ts)

def costo_permutacion(finca, permutacion):
    costo_total = 0
    t = 0
    for i in permutacion:
        costo_total += costo_tablon(finca[i], t)
        t += finca[i].tr
    return costo_total

def roFB(finca):
    n = len(finca)
    min_cost = float('inf')
    best_p = None
    for p in itertools.permutations(range(n)):
        c = costo_permutacion(finca, p)
        if c < min_cost:
            min_cost = c
            best_p = p
    return tuple(best_p), min_cost

def roV(finca):
    n = len(finca)
    # Orden voraz: deadline (ts - tr) ascendente, prioridad (p) descendente
    orden = sorted(range(n), key=lambda i: (finca[i].ts - finca[i].tr, -finca[i].p))
    c = costo_permutacion(finca, orden)
    return tuple(orden), c

def roPD(finca):
    n = len(finca)
    limit = 1 << n
    C = [float('inf')] * limit
    C[0] = 0
    Last = [-1] * limit
    
    for mask in range(1, limit):
        T = sum(finca[i].tr for i in range(n) if (mask & (1 << i)))
        for j in range(n):
            if mask & (1 << j):
                prev_mask = mask ^ (1 << j)
                cost_j = costo_tablon(finca[j], T - finca[j].tr)
                if C[prev_mask] + cost_j < C[mask]:
                    C[mask] = C[prev_mask] + cost_j
                    Last[mask] = j
                    
    orden_optimo = []
    mask_actual = limit - 1
    while mask_actual > 0:
        tablon_escogido = Last[mask_actual]
        orden_optimo.append(tablon_escogido)
        mask_actual ^= (1 << tablon_escogido)
        
    orden_optimo.reverse()
    return tuple(orden_optimo), C[limit - 1]

def leer_finca(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as f:
            lineas = f.read().splitlines()
        lineas = [l.strip() for l in lineas if l.strip()]
        if not lineas:
            print("El archivo esta vacio.")
            return None
        n = int(lineas[0])
        finca = []
        for i in range(1, n + 1):
            # Soporta tanto comas como espacios como separadores
            partes = lineas[i].replace(',', ' ').split()
            ts = int(partes[0])
            tr = int(partes[1])
            p = int(partes[2])
            rp = int(partes[3])
            finca.append(Tablon(i - 1, ts, tr, p, rp))
        return finca
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def escribir_salida(ruta_archivo, solucion):
    try:
        permutacion, costo = solucion
        with open(ruta_archivo, 'w') as f:
            f.write(f"{costo}\n")
            for idx in permutacion:
                f.write(f"{idx}\n")
        print(f"Salida escrita exitosamente en {ruta_archivo}")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")

def main():
    finca = None
    solucion_actual = None
    
    while True:
        print("\n" + "="*50)
        print("  PLAN DE RIEGO OPTIMO - MENU PRINCIPAL")
        print("="*50)
        print("1. Leer finca desde archivo")
        print("2. Visualizar entradas (finca actual)")
        print("3. Calcular optimo con Fuerza Bruta (roFB)")
        print("4. Calcular con Algoritmo Voraz (roV)")
        print("5. Calcular optimo con Programacion Dinamica (roPD)")
        print("6. Visualizar salida calculada")
        print("7. Escribir salida en archivo")
        print("8. Salir")
        
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == '1':
            ruta = input("Ingrese la ruta del archivo de entrada: ").strip()
            nueva_finca = leer_finca(ruta)
            if nueva_finca is not None:
                finca = nueva_finca
                solucion_actual = None
                print(f"Finca leida correctamente. ({len(finca)} tablones)")
        elif opcion == '2':
            if finca is None:
                print("No hay ninguna finca cargada en memoria.")
            else:
                print(f"Cantidad de tablones: {len(finca)}")
                for t in finca:
                    print(t)
        elif opcion in ['3', '4', '5']:
            if finca is None:
                print("Primero debe leer una finca desde un archivo.")
                continue
            
            if len(finca) > 10 and opcion == '3':
                print("Advertencia: La Fuerza Bruta tomara muchisimo tiempo para mas de 10 tablones.")
                confirm = input("¿Desea continuar? (s/n): ")
                if confirm.lower() != 's':
                    continue
            if len(finca) > 20 and opcion == '5':
                print("Advertencia: La Programacion Dinamica podria agotar la memoria para mas de 20 tablones.")
                confirm = input("¿Desea continuar? (s/n): ")
                if confirm.lower() != 's':
                    continue
                    
            print("Calculando...")
            if opcion == '3':
                solucion_actual = roFB(finca)
                print("Calculo con Fuerza Bruta completado.")
            elif opcion == '4':
                solucion_actual = roV(finca)
                print("Calculo con Algoritmo Voraz completado.")
            elif opcion == '5':
                solucion_actual = roPD(finca)
                print("Calculo con Programacion Dinamica completado.")
        elif opcion == '6':
            if solucion_actual is None:
                print("Aun no se ha calculado ninguna solucion.")
            else:
                permutacion, costo = solucion_actual
                print(f"Costo Total: {costo}")
                print(f"Orden de Riego (Indices de tablones): {list(permutacion)}")
        elif opcion == '7':
            if solucion_actual is None:
                print("Aun no se ha calculado ninguna solucion.")
            else:
                ruta = input("Ingrese la ruta del archivo de salida: ").strip()
                escribir_salida(ruta, solucion_actual)
        elif opcion == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()
