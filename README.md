# Важно знать 
## [Навигация и маршрутизация в flet](https://flet.dev/docs/getting-started/navigation-and-routing)
## [Асинхронные приложения в flet](https://flet.dev/docs/getting-started/async-apps)
## [Пользовательские элементы управления](https://flet.dev/docs/getting-started/custom-controls)

<br>

# Фаловая структура.

## Лучше чтобы фаловая структура имала такой вид: 

<br>

> src/ <br>
>>  короткое название сигмента ( типо: auth, home, ... )/ <br>
>>> ui/ <br>
>>
>>> view/ <br>
>>
>> database.py - связь с бэкендом <br>
>> router.py - маршрутизатор страниц ( view элементов )<br>
>> utils.py - утилиты  
> --- 

<br>

# Примеры кода

### Это все просто примеры кода, можно писать код по-другому

<br>


# 1. Пример роутера
## router.py 

    import flet as ft
    from repath import match

    class RoutersDict:
        def __init__(self,routers:dict = {}):
            self.routers = routers

        def __getitem__(self, route):
            if view:=self.routers.get(route,False):
                return view
            if any(key:=r for r in self.routers.keys() if (value := match(r,route))):
                return self.routers.get(key,False)
            return None

    class Router:
        def __init__(self,page:ft.Page):
            self.page = page
            self.routes = RoutersDict({
                "/путь": СигментView,
            })

        def route_change(self,route):
            if not [view for view in self.page.views if view.route == route.route]: 
                self.page.views.append(self.routes[route.route](self.page))
            self.page.update()

## main.py


    import flet as ft
    from src.router import Router
    
    def main(page:ft.Page):
        router = Router(page)
        page.on_route_change = router.route_change
        page.views.clear()

        ...




