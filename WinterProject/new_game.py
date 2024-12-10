import reflex as rx
from .start_Mode.state import State
from rxconfig import config


def easy_game():
    return rx.link(
        rx.button(
            "Modo fácil",
            on_click=[State.set_mode("easy"), rx.redirect("/easy_game")],  # Define el modo y redirige
        ),
    )

def hard_game():
    return rx.link(
        rx.button(
            "Modo difícil",
            on_click=[State.set_mode("hard"), rx.redirect("/hard_game")],  # Define el modo y redirige
        ),
    )

def go_back():
    return rx.link(
        rx.button("Atrás"),
        href="/"
    )

@rx.page(route="/new_Game_page", title="New Game")
def new_Game_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Nueva Partida...", size="9"),
            easy_game(),
            hard_game(),
            go_back(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )