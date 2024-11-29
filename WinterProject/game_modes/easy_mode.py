import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...
    
def start_game():
    return rx.link(
        rx.button("Start"),
        href="/easy_game"
    )

def go_back():
    return rx.link(
        rx.button("Atrás"),
        href="/new_Game_page"
    )
    
@rx.page(route="/easy_mode", title="Easy Mode")
def easy_Mode() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Modo Fácil...", size="9"),
            start_game(),
            go_back(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )