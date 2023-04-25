class Paso:
    def __init__(self, paso: str, pasoLatex: str, descripcion: str):
        self.paso = paso
        self.pasoLatex = pasoLatex
        self.descripcion = descripcion

    def toJson(self) -> dict:
        return {
            "paso": self.paso,
            "pasoLatex": self.pasoLatex,
            "descripcion": self.descripcion
        }
