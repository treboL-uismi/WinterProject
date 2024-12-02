import reflex as rx
from rxconfig import config
from WinterProject.start_Mode.state import State
from WinterProject.start_Mode import style
from PIL import Image

img = Image.open(r"assets\personajes_qsq_02.png")

easyChr = {
    "Maria" : ["pelo castaño"],
    "Frans" : ["boca pequeña"],
    "Herman" : ["calvo"],
    "Bernard" : ["gorro"],
    "Philip" : ["barba", "pelo castaño"],
    "Eric" : ["rubio", "sombrero"],
    "Charles" : ["rubio", "bigote"],
    "Peter" : ["nariz grande", "boca grande", "pelo blanco"]
}

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
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
    )

@rx.page(route="/easy_game", title="Easy Game")
def easy_Game() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.hstack(
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