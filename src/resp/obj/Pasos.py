from .Paso import Paso

class Pasos:
    def __init__(self, pasos: list[Paso]):
        self.pasos = pasos

    def toJson(self) -> dict:
        return {
            "pasos": [paso.toJson() for paso in self.pasos]
        }
