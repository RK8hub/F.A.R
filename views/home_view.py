from src.modules.constructor import Template
import flet as ft

home = Template()

home.make_view(
    
    ft.View(
        
        route=home.route,
        controls=[
            
            ft.Text("hola")
            
        ]
        
        
    )
)