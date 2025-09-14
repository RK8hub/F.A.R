from src.modules.constructor import Template
import flet as ft

example = Template()

example.make_view(
    
    ft.View(
        
        route=example.route,
        controls=[
            
            ft.Text("settings dir example"),
            ft.Button("navega",on_click=lambda _: example.page.go("/example1"))
            
        ]
        
        
    )
)
