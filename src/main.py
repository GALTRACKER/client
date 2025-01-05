import flet as ft  
from UI.NavBar import NavBar
   
def main(page: ft.Page):
    page.bgcolor = "#151515"
    page.horizontal_alignment = page.vertical_alignment = "center"
    
    page.add(
        ft.Column(
            expand=True,
            controls=[
                ft.Text('Body', color='white')
            ]
        )
    )
    
    page.bottom_appbar = NavBar.navbar()
    
    page.update()

ft.app(target=main)
    
def plus_btn(page: ft.Page):
        page.floating_action_button = ft.FloatingActionButton(icon=ft.Icons.ADD, focus_color="#3F7199")
        page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_TOP
