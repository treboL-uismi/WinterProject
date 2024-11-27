import reflex as rx

class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    @rx.event
    def answer(self):
        respuesta = "¡No sé eso!"
        self.chat_history.append((self.question, respuesta))
        self.question = ""
