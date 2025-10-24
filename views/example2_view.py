from src.modules.constructor import Template
import flet as ft

example2 = Template()

example2.make_view(
    
    ft.View(
        
        route=example2.auto_route(),
        controls=[
            
            ft.Text("And yes, it supports automatic routes at the same time. 😎  [{route}]"),
            ft.Button("navegate",on_click=lambda _: example2.page.go("/"))
            
            
        ]
        
        
    )
)