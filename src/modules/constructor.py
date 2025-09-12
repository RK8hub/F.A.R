from dataclasses import dataclass, field
import flet as ft
import inspect, os

@dataclass
class Template:
    route: str = field(init=False)
    view: ft.View = field(init=False)
    
    def __post_init__(self):
        self.route = self.auto_route() # type: ignore
        
    
    def auto_route(self):
        stack = inspect.stack()
        current_file = os.path.abspath(__file__)

        for frame_info in stack[1:]:
            caller_file = frame_info.filename
            if caller_file != current_file and not caller_file.startswith("<"):
                
                #limpiando la ruta
                route = os.path.abspath(caller_file)
                route = route.replace('\\',"/") #<- reconfiguramos los simbolos de navegacion
                caperta_view = route.find('/views') #<- buscamos en la ruta la carpeta de las views
                
                self.import_text = route[caperta_view+1:]
                
                route = route[caperta_view:] #<- cortamos la ruta desde la carpeta views
                
                route = route[:-3] #<- eliminamos el .py
                route = route[:-5] #<- se elimina el _views 
                route = route[6:] #<- se elimina la caperta views para crear rutas limpias
                return route
        return None
    
    def make_view(self,view: ft.View):
        self.view = view
    