import flet as ft
import importlib
import pathlib


def cargar_views():
    views = []
    ruta_views = pathlib.Path(__file__).parent.parent.parent / "views"
    for archivo in ruta_views.rglob("*_view.py"):
        relative_path = archivo.relative_to(ruta_views.parent).with_suffix("")
        nombre_modulo = ".".join(relative_path.parts)

        modulo = importlib.import_module(nombre_modulo)

        nombre_var = archivo.stem.replace("_view", "")
        if hasattr(modulo, nombre_var):
            views.append(getattr(modulo, nombre_var))

    return views


def view_handler(page: ft.Page):
    todas_las_views = cargar_views()
    rutas_dict = {v.route: v for v in todas_las_views}
    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        v = rutas_dict.get(e.route)
        if v:
            v.page = page
            page.views.append(v.view)
        page.update()

    page.on_route_change = route_change

    if page.route in rutas_dict:
        rutas_dict[page.route].page = page
        page.views.append(rutas_dict[page.route].view)
    else:
        primer_v = todas_las_views[0]
        primer_v.page = page
        page.views.append(primer_v.view)

    page.update()
