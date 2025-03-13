class ParteProcesal:
    def __init__(self, parteA: list[object], parteB: list[object]):
        self._parteA = parteA
        self._parteB = parteB

    def get_parteA(self):
        return self._parteA

    def get_parteB(self):
        return self._parteB

    def __str__(self):
        demandados = ", ".join(str(p) for p in self._parteA)
        demandantes = ", ".join(str(p) for p in self._parteB)
        return f"Parte Procesal --->\n - Demandados: {demandados}\n  - Demandantes: {demandantes}\n"
