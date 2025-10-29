import flet as ft
from src.modules.far.handler import view_handler

def main(page: ft.Page):
    view_handler(page)
ft.app(main)