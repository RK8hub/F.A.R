import importlib
import pathlib

def cargar_views():
    views = []
    ruta_views = pathlib.Path(__file__).parent.parent.parent / "views"
    for archivo in ruta_views.rglob("*_view.py"):
        # Construimos nombre de módulo 
        relative_path = archivo.relative_to(ruta_views.parent).with_suffix("")
        nombre_modulo = ".".join(relative_path.parts)

        modulo = importlib.import_module(nombre_modulo)

        nombre_var = archivo.stem.replace("_view", "")
        if hasattr(modulo, nombre_var):
            views.append(getattr(modulo, nombre_var))
    

    return views

handler_views = []
todas_las_views = cargar_views()
for i in todas_las_views:
    handler_views.append(i.view)