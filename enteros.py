class Enteros:
    def __init__(self, a, b):
        self.a = abs(a)
        self.b = abs(b)
    
    def mcd(self):
        """Algoritmo de Euclides para calcular MCD."""
        x, y = self.a, self.b
        while y != 0:
            x, y = y, x % y
        return x

if __name__ == "__main__":
    numeros = Enteros(56, 98)
    print(f"MCD de 56 y 98: {numeros.mcd()}")  # Output: 14