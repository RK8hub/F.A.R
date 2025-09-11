import flet as ft
from views.home_view import home

def main(page: ft.Page):
    page.title = "test"
    page.views.clear()
    page.views.append(home.view)
    page.update()
    print(home.route)

ft.app(main)