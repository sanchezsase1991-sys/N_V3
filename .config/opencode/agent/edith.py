from pathlib import Path
import sys

archivo = sys.argv[1] if len(sys.argv) > 1 else "archivo.txt"

print(f"Editando {archivo}. Termina con una línea que contenga solo EOF")

lineas = []
while True:
    try:
        linea = sys.stdin.readline()
    except KeyboardInterrupt:
        break
    if not linea or linea.rstrip() == "EOF":
        break
    lineas.append(linea)

Path(archivo).write_text("".join(lineas))
print("Guardado:", archivo)
