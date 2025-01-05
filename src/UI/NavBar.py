import flet as ft


class NavBar:        
    @staticmethod
    def navbar():  
        return ft.BottomAppBar(
            height=80,
            bgcolor="#1A1A1A",
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
                vertical_alignment="center",
                alignment="spaceAround",
                controls=[
                    ft.Column(
                        horizontal_alignment="center",
                        spacing=1,
                        controls=[
                            ft.IconButton(icon=ft.Icons.LIBRARY_BOOKS_ROUNDED, icon_color=ft.colors.WHITE, icon_size=28),
                            ft.Text("Книги", size=12, color=ft.colors.WHITE)
                        ]
                    ),

                    ft.Column(
                        horizontal_alignment="center",
                        spacing=1,
                        controls=[
                            ft.IconButton(icon=ft.Icons.PEOPLE_ROUNDED, icon_color=ft.colors.WHITE, icon_size=28),
                            ft.Text("Поиск", size=12, color=ft.colors.WHITE)
                        ]
                    ),

                    ft.Column(
                        horizontal_alignment="center",
                        spacing=1,
                        controls=[
                            ft.FloatingActionButton(
                                icon=ft.Icons.ADD,
                                bgcolor="#3F7199",  # Цвет кнопки
                                shape=ft.CircleBorder(),  # Круглая кнопка
                                elevation=6,  # Тень кнопки
                                height=40,  # МЕНЬШИЙ РАЗМЕР
                                width=40   # МЕНЬШИЙ РАЗМЕР
                            ),
                            ft.Text("Добавить", size=12, color=ft.colors.WHITE)
                        ]
                    ),

                    ft.Column(
                        horizontal_alignment="center",
                        spacing=1,
                        controls=[
                            ft.Container(
                                content=ft.Image(src="../assets/stat.png", width=42, height=42, color=ft.colors.GREY),
                            ),
                            ft.Text("Избранное", size=12, color=ft.colors.WHITE)
                        ]
                    ),

                    ft.Column(
                        horizontal_alignment="center",
                        spacing=1,
                        controls=[
                            ft.IconButton(icon=ft.Icons.PERSON, icon_color=ft.colors.WHITE, icon_size=28),
                            ft.Text("Профиль", size=12, color=ft.colors.WHITE)
                        ]
                    ), 
                ]
            ),
        )
        
    @staticmethod
    def plus_btn(page: ft.Page):
        page.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD, 
            bgcolor="#3F7199", 
            foreground_color="#C2C2C2"
            )
        page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_TOP