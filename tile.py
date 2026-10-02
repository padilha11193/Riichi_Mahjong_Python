class Tile:
    def __init__(self, naipe, valor):
        if naipe in ("sou", "pin", "man"):
            if valor not in range(1, 10):
                raise ValueError("O valor deve estar entre 1 e 9.")

        elif naipe == "vento":
            if valor not in ("leste", "oeste", "norte", "sul"):
                raise ValueError("Peça de honra inválida.")

        elif naipe == "dragao":
            if valor not in ("vermelho", "verde", "branco"):
                raise ValueError("Peça de honra inválida.")
        else:
            raise ValueError("Naipe inválido.")

        self.naipe = naipe
        self.valor = valor

    def __str__(self):
        if self.naipe in ("sou", "pin", "man"):
            return str(self.valor) + " de " + self.naipe
        elif self.naipe == "dragao":
            return self.naipe + " " + self.valor
        else:
            return self.valor
