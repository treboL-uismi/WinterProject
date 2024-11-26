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

class ChatState(rx.State):
    messages = []  # Lista de mensajes
    input_value = ""  # Valor del input de texto

    @staticmethod
    def set_input_value(value):
        ChatState.input_value = value

    @staticmethod
    def send_message(message):
        if message.strip():  # Verifica que el mensaje no esté vacío
            ChatState.messages.append(message)
            ChatState.input_value = ""  # Limpia el campo de entrada después de enviar

def chat_component():
    return rx.box(
        children=[
            rx.text("Chat", font_size="20px", font_weight="bold"),
            rx.vstack(
                # Usando rx.foreach para iterar sobre ChatState.messages
                rx.foreach(
                    ChatState.messages,
                    lambda msg: rx.text(msg)
                ),
                margin_bottom="10px"
            ),
            # Entrada de texto
            rx.input(
                placeholder="Escribe tu pregunta aquí...",
                width="100%",
                margin_top="10px",
                value=ChatState.input_value,  # Usamos el valor del estado ChatState
                on_change=lambda value: ChatState.set_input_value(value)  # Actualizamos el estado global
            ),
            # Botón para enviar el mensaje
            rx.button(
                "Enviar",
                margin_top="10px",
                color_scheme="blue",
                on_click=lambda: ChatState.send_message(ChatState.input_value)  # Usamos el estado al hacer clic
            ),
        ],
        position="fixed",
        bottom="20px",     # A 20px del borde inferior
        right="20px",      # A 20px del borde derecho
        width="300px",
        padding="20px",
        background_color="#1A202C",
        color="white",
        border_radius="8px",
        box_shadow="0px 0px 10px rgba(0, 0, 0, 0.3)",
        z_index="1000"
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
            chat_component(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )