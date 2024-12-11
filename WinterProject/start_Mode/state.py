import reflex as rx
from .list_names import easyChr, hardChr
from .personajeRonadom import personajeRandom
from .ComprobarCaracteristicas import buscar_caracteristicas, tiene_caracteristica

class State(rx.State):
    question: str = ""
    chat_history: list[tuple[str, str]] = []
    random_character: str = ""
    is_game_over: bool = False
    guessed_character: str = ""
    mode: str = ""

    @rx.event
    def set_mode(self, mode: str):
        """Establece el modo de juego."""
        self.mode = mode

    def set_question(self, question: str):
        self.question = question.strip()
        

    def clear_chat(self):
        self.reset()

    def get_character_list(self):
        # Retorna el diccionario correspondiente basado en el modo de juego
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
            self.chat_history.append(("Guess", f"Correct! The character was {self.random_character}."))
            self.is_game_over = True
        else:
            self.chat_history.append(("Guess", f"Incorrect! Try again."))
        self.guessed_character = ""


