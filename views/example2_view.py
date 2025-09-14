from src.modules.constructor import Template
import flet as ft

example2 = Template()

example2.make_view(
    
    ft.View(
        
        route=example2.route,
        controls=[
            
            ft.Text("example2"),
            ft.Button("navega",on_click=lambda _: example2.page.go("/settings/example"))
            
            
        ]
        
        
    )
)