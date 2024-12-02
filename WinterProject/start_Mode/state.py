import reflex as rx


class State(rx.State):
    question: str
    
    chat_history: list[tuple[str, str]]

    @rx.event
    def answer(self):
        answer = "I don't know!"
        self.chat_history.append((self.question, answer))