import reflex as rx

from rxconfig import config

from PIL import Image

img = Image.open(r"assets\personajes_qsq_01.png")

card = [(0, 0, 510, 771),
        (510, 0, 1020, 771),
        (1020, 0, 1530, 771),
        (1530, 0, 2040, 771),
        (0, 771, 510, 1542),
        (510, 771, 1020, 1542),
        (1020, 771, 1530, 1542),
        (1530, 771, 2040, 1542),
        (0, 1542, 510, 2313),
        (510, 1542, 1020, 2313),
        (1020, 1542, 1530, 2313),
        (1530, 1542, 2040, 2313),
        (0, 2313, 510, 3084), 
        (510, 2313, 1020, 3084),
        (1020, 2313, 1530, 3084),
        (1530, 2313, 2040, 3084)]

def game_board():
    return rx.grid(
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[0])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[1])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[2])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[3])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[4])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[5])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[6])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[7])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[8])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[9])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[10])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[11])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[12])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[13])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[14])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        rx.card(rx.button(rx.inset(rx.image(src=img.crop(card[15])), side="center", pb="current")), as_child=True, radius="medium", variant="ghost"),
        
        columns="4",
        spacing="6",
        align_items="start",
        flex_wrap="wrap",
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