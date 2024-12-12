import reflex as rx
from .list_names import easyChr, hardChr
from .personajeRonadom import personajeRandom
from .ComprobarCaracteristicas import tiene_caracteristica

class State(rx.State):
    question: str = ""
    chat_history: list[tuple[str, str]] = []
    random_character: str = ""
    is_game_over: bool = False
    guessed_character: str = ""
    mode: str = ""
    selected_cards: set[int] = set()

    def toggle_card(self, index: int):
        if index in self.selected_cards:
            self.selected_cards.remove(index)
        else:
            self.selected_cards.add(index)


    @rx.event
    def set_mode(self, mode: str):
        self.mode = mode
        self.random_character = ""

    def get_character_list(self):
        return easyChr if self.mode == "easy" else hardChr

    def get_answer(self, question: str) -> str:
        if not self.random_character:
            self.random_character = personajeRandom(self.get_character_list())
        if tiene_caracteristica(self.get_character_list(), self.random_character, question):
            return f"Sí, el personaje tiene la característica '{question}'."
        else:
            return f"No, el personaje no tiene la característica '{question}'."

    @rx.event
    def answer(self):
        if self.question:
            answer = self.get_answer(self.question)
            self.chat_history.append((self.question, answer))
        self.question = ""

    def set_guess(self, guess: str):
        self.guessed_character = guess.strip()

    @rx.event
    def guess_character(self):
        if not self.random_character:
            self.random_character = personajeRandom(self.get_character_list())

        if self.guessed_character.lower() == self.random_character.lower():
            self.chat_history.append(("¡Eso es!", f"¡Correcto! El personaje es {self.random_character}."))
            self.is_game_over = True
        else:
            self.chat_history.append(("¡Eso es!", f"¡Incorrecto! Inténtalo de nuevo."))
        self.guessed_character = ""

    @rx.event
    def clear_chat(self):
        self.chat_history.clear()
        self.random_character = ""
        self.is_game_over = False



