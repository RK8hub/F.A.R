from src.modules.constructor import Template
import flet as ft

example1 = Template()

example1.make_view(
    
    ft.View(
        
        route=example1.route,
        controls=[
            ft.Text("example1"),
            ft.Button("navega",on_click=lambda _: example1.page.go("/example2"))
            
        ]
        
        
    )
)