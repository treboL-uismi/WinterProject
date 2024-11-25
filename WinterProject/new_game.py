import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...
    
def easy_game():
    return rx.link(
        rx.button("Modo fácil"),
        href="/easy_mode"
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
            go_back(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )