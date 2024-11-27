import reflex as rx
from rxconfig import config

from PIL import Image

img = Image.open(r"assets\personajes_qsq_02.png")


card = [(0, 0, 510, 771),
        (510, 0, 1020, 771),
        (1020, 0, 1530, 771),
        (1530, 0, 2040, 771),
        (0, 771, 510, 1542),
        (510, 771, 1530, 1542),
        (1020, 771, 1530, 1542),
        (1530, 771, 2040, 1542)]


def game_board():
    return rx.grid(
        rx.foreach(
            rx.Var.range(8),
            lambda i: rx.card(rx.inset(rx.image(src=img.crop(card[0]),
                         width="100%",
                         height="auto",
                         ),
                        side="center",
                        pb="current",
            ),          
          ),
        ),
        columns="4",
        spacing="4",
        width="100%",
    )

def restart_game():
    return rx.link(
        rx.button("Restart"),
        href="/easy_game"
    )

def go_back():
    return rx.link(
        rx.button("Exit Game"),
        href="/new_Game_page"
    )

@rx.page(route="/easy_game", title="Easy Game")
def easy_Game() -> rx.Component:
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