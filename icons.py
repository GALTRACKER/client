import flet as ft
import re

def main(page: ft.Page):

    def item_list(icons_name:str):
        return ft.ListTile(
                    leading=ft.Icon(icons_name),
                    title=ft.Text(icons_name),
                )

    lv = ft.ListView(expand=True, spacing=10)
    for icon in ft.icons.__dict__:
        try:
            lv.controls.append(item_list(icon))
        except:
            pass
    page.add(lv)

ft.app(main)