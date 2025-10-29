from flet import View, Page, Text
from dataclasses import dataclass, field
from inspect import stack
from os import path

@dataclass
class Template:
    route: str = field(init=False)
    page: Page = field(init=False)
    view: View = field(init=False)
    
    def __post_init__(self):
        self.route = self.auto_route() # type: ignore
        
    
    def auto_route(self):
        Stack = stack()
        current_file = path.abspath(__file__)

        for frame_info in Stack[1:]:
            caller_file = frame_info.filename
            if caller_file != current_file and not caller_file.startswith("<"):
                
                #limpiando la ruta
                route = path.abspath(caller_file)
                route = route.replace('\\',"/") #<- reconfiguramos los simbolos de navegacion
                caperta_view = route.find('/views') #<- buscamos en la ruta la carpeta de las views
                
                self.import_text = route[caperta_view+1:]
                
                route = route[caperta_view:] #<- cortamos la ruta desde la carpeta views
                
                route = route[:-3] #<- eliminamos el .py
                route = route[:-5] #<- se elimina el _views 
                route = route[6:] #<- se elimina la caperta views para crear rutas limpias
                return route
        return None
    
    
    def make_view(self,view: View):
        if not self.route == view.route:
            self.route = view.route
        self.view = view
        for ctrl in view.controls:
            if isinstance(ctrl, Text) and "{route}" in str(ctrl.value):
                ctrl.value = ctrl.value.replace("{route}", self.route)
    