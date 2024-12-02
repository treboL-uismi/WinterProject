import reflex as rx
from rxconfig import config
from WinterProject.start_Mode.state import State
from WinterProject.start_Mode import style
from PIL import Image

img = Image.open(r"assets\personajes_qsq_01.png")

hardChr = {
    "Susan" : ["pelo blanco"],
    "Claire" : ["sombrero", "gafas azules"],
    "David" : ["perilla", "rubio"],
    "Anne" : ["afro", "arietes"],
    "Robert" : ["pelo castaño", "ojos azules"],
    "Anita" : ["rubia", "cara rechoncha"],
    "Joe" : ["rubio", "gafas rojas"],
    "George" : ["pelo blanco", "fedora"],
    "Bill" : ["calvo", "cabeza huevo"],
    "Alfred" : ["pelo largo", "bigote"],
    "Max" : ["bigote", "pelo castaño"],
    "Tom" : ["calvo", "gafas marrones"],
    "Alex" : ["bigote", "pelo corto", "pelo castaño"],
    "Sam" : ["calvo", "gafas redondas"],
    "Richard" : ["calvo", "barba"],
    "Paul" : ["gafas", "pelo blanco", "cejas blancas"]    
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
    (0, 1542, 510, 2313),
    (510, 1542, 1020, 2313),
    (1020, 1542, 1530, 2313),
    (1530, 1542, 2040, 2313),
    (0, 2313, 510, 3084),
    (510, 2313, 1020, 3084),
    (1020, 2313, 1530, 3084),
    (1530, 2313, 2040, 3084),
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
        href="/hard_game"
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

@rx.page(route="/hard_game", title="Hard Game")
def hard_Game() -> rx.Component:
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