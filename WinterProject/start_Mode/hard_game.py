import reflex as rx

from rxconfig import config

def game_board():
    return rx.grid(
        rx.foreach(
            rx.Var.range(16),
            lambda i: rx.card(f"Card {i + 1}", height="10vh"),
        ),
        columns="4",
        spacing="4",
        width="100%",
    )

def restart_game():
    return rx.link(
        rx.button("Restart"),
        href="/hard_game"
    )

def go_back():
    return rx.link(
        rx.button("Exit Game"),
        href="/new_Game_page"
    )

@rx.page(route="/hard_game", title="Hard Game")
def hard_Game() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Time left -", size="9"),
            game_board(),
            restart_game(),
            go_back(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )