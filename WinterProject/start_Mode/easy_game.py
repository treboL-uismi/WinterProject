import reflex as rx
from rxconfig import config
from PIL import Image

img = Image.open(r"assets\personajes_qsq_02.png")

card = [
    (0, 0, 510, 771),
    (510, 0, 1020, 771),
    (1020, 0, 1530, 771),
    (1530, 0, 2040, 771),
    (0, 771, 510, 1542),
    (510, 771, 1020, 1542),
    (1020, 771, 1530, 1542),
    (1530, 771, 2040, 1542),
]

def game_board():
    return rx.grid(
        *[
            rx.card(
                rx.button(
                    rx.image(src=img.crop(card[i]), alt=f"Card {i + 1}"),
                    as_child=True,
                    radius="medium",
                    variant="ghost",
                ),
            )
            for i in range(len(card))
        ],
        columns="4",
        spacing="6",
        align_items="start",
        flex_wrap="wrap",
        width="100%",
    )

def restart_game():
    return rx.link(
        rx.button("Restart", color_scheme="blue"),
        href="/easy_game"
    )

def go_back():
    return rx.link(
        rx.button("Exit Game", color_scheme="red"),
        href="/new_Game_page"
    )

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right", bg="gray.200", padding="0.5em", border_radius="md"),
        rx.box(answer, text_align="left", bg="blue.100", padding="0.5em", border_radius="md"),
        margin_y="1em",
    )

def chat() -> rx.Component:
    qa_pairs = [
        ("Pregunta 1", "Respuesta 1"),
        ("Pregunta 2", "Respuesta 2"),
    ]
    return rx.box(
        *[qa(q, a) for q, a in qa_pairs],
        overflow_y="auto",
        height="50vh",
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Escribe tu pregunta", flex="1", border="1px solid gray"),
        rx.button("Enviar", color_scheme="green"),
    )

@rx.page(route="/easy_game", title="Easy Game")
def easy_Game() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.hstack(
            # Sección de la cuadrícula de imágenes
            rx.box(
                rx.vstack(
                    rx.heading("Time left -", size="9"),
                    game_board(),
                    rx.hstack(restart_game(), go_back(), spacing="2"),
                    spacing="5",
                ),
                width="70%",
                padding="1em",
                bg="gray.50",
                border_radius="lg",
                shadow="md",
            ),
            # Sección del chat
            rx.box(
                rx.vstack(
                    chat(),
                    action_bar(),
                    spacing="3",
                ),
                width="30%",
                padding="1em",
                bg="gray.100",
                border_radius="lg",
                shadow="md",
            ),
        ),
        spacing="4",
        align_items="start",
        padding="2em",
        min_height="100vh",
    )