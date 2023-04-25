class Grafica:
    def __init__(self, func: str, figure: str):
        self.func = func
        self.figure = figure

    def toJson(self) -> dict:
        return {
            "funcionLatex": self.func,
            "grafica": self.figure
        }
