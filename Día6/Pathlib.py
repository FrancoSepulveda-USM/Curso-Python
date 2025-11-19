from pathlib import Path,PureWindowsPath

directorio = Path("C:/Users/franc/Documents/Escritorio/Pycharm/Día6/Prueba.txt")
print(type(directorio)) #Objeto Path
print(directorio.read_text())

dir_windows = PureWindowsPath(directorio)
print(directorio)