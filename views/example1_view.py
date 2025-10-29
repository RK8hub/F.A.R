from src.modules.far.constructor import Template
import flet as ft

example1 = Template()

example1.make_view(
    
    ft.View(
        
        route='/',
        controls=[
            ft.Text("Manual Routes Are Here! 🥳 [{route}]"),
            ft.Button("navegate",on_click=lambda _: example1.page.go("/example2"))
            
        ]
        
        
    )
)
