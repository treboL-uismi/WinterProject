import reflex as rx
from typing import List

from rxconfig import config

def game_board():
    return rx.grid(
        rx.foreach(
            rx.Var.range(8),
            lambda i: rx.card(f"Card {i + 1}", height="10vh"),
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

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )

def chat() -> rx.Component:
    qa_pairs = [
        ("Pregunta", "Respuesta"),
    ]
    return rx.box(
        *[qa(q, a) for q, a in qa_pairs]
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Escribe tu pregunta"),
        rx.button("Enviar"),
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
            chat(),
            action_bar(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )