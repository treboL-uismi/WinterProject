import reflex as rx
from rxconfig import config
from WinterProject.start_Mode.state import State
from WinterProject.start_Mode import style
from PIL import Image

def set_mode(mode: str):
    @rx.event
    def set_mode_action():
        State.mode = mode
    return set_mode_action

def game_board_easy():
    img_original = Image.open(r"assets\\personajes_qsq_02.png")
    img_negra = Image.open(r"assets\\imagenEnNegro.png")

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

    return rx.grid(
        *[
            rx.image(
                src=rx.cond(
                    State.selected_cards.contains(i),  # Usar Var.contains() aquí
                    img_negra.crop(card[i]),
                    img_original.crop(card[i]),
                ),
                alt=f"Card {i + 1}",
                on_click=lambda i=i: State.toggle_card(i),  # Acción del click en la imagen
                width="100%",
                height="auto",
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
        rx.button("Reiniciar", color_scheme="blue"),
        href="/easy_game", on_click=State.clear_chat
    )

def go_back():
    return rx.link(
        rx.button("Salir", color_scheme="red"),
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
        ),
        rx.cond(
            State.is_game_over,
            rx.box("¡Has ganado! Dale a Reiniciar para volver a empezar.", bg="green.200", padding="1em", border_radius="lg"),
        )
    )

def guess_action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Adivina el personaje",
            on_change=State.set_guess,
            style=style.input_style,
        ),
        rx.button(
            "Guess",
            on_click=State.guess_character,
            style=style.button_style,
        ),
    )

def action_bar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.input(
                placeholder="Pregunta por una característica",
                on_change=State.set_question,
                style=style.input_style,
            ),
            rx.button(
                "Ask",
                on_click=State.answer,
                style=style.button_style,
            ),
        ),
        guess_action_bar(),
    )

def clear_button() -> rx.Component:
    return rx.button(
    "Limpiar Chat",
    on_click=State.clear_chat,
)

@rx.page(route="/easy_game", title="Easy Game")
def easy_Game() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.hstack(
            rx.box(
                rx.vstack(
                    game_board_easy(),
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
                    clear_button(),
                    spacing="3",
                ),
                width="30%",
                padding="1em",
                bg="gray.100",
                border_radius="lg",
                shadow="md",
            ),
        ),
        on_mount=State.set_mode("easy"),
    )