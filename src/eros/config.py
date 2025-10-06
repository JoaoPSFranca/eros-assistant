import os


class Settings:
    GEMINI_API_KEY: str

    def __init__(self):
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise ValueError(
                "A variável de ambiente GEMINI_API_KEY não foi encontrada."
            )
        self.GEMINI_API_KEY = key
