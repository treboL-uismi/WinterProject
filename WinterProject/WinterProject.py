"""rx.code(f"{config.app_name}/{config.app_name}.py")"""
import reflex as rx

from rxconfig import config


def new_game():
    return rx.link(
        rx.button("Nueva Partida"),
        href="/new_Game_page",
        external="True",
    )
    
@rx.page(route="/", title="Index")
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("¿Quién es quién?", size="9"),
            new_game(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

app = rx.App()