from pathlib import Path
import os

carpeta = Path("ruta_carpeta")

for archivo in carpeta.iterdir():
    name = archivo.name
    if "- Hecho con" in name:
      print(archivo.name)
      nuevoNombre = name.split("-")
      nombreFinal = nuevoNombre[0] + ".mp4"
      archivo.rename(f'ruta_carpeta{nombreFinal}')
      print(nombreFinal)
      print(archivo.name)
