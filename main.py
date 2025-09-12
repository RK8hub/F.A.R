from src.modules.handler import handler_views
import flet as ft

def main(page: ft.Page):
    
    page.views.extend(handler_views)
    page.update()
    
ft.app(main)