from decimal import Decimal

class ComplexDecimal:
    def __init__(self, real: Decimal, imag: Decimal = Decimal("0.0")):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, ComplexDecimal):
            return ComplexDecimal(self.real + other.real, self.imag + other.imag)
        return ComplexDecimal(self.real + Decimal(other), self.imag)

    def __mul__(self, other):
        if isinstance(other, ComplexDecimal):
            return ComplexDecimal(
                self.real * other.real - self.imag * other.imag,
                self.real * other.imag + self.imag * other.real,
            )
        return ComplexDecimal(self.real * Decimal(other), self.imag * Decimal(other))

    def conjugate(self):
        return ComplexDecimal(self.real, -self.imag)

    def __repr__(self):
        return f"({self.real} + {self.imag}i)"

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __truediv__(self, other):
        if isinstance(other, ComplexDecimal):
            denom = other.real**2 + other.imag**2
            return ComplexDecimal(
                (self.real * other.real + self.imag * other.imag) / denom,
                (self.imag * other.real - self.real * other.imag) / denom,
            )
        return ComplexDecimal(self.real / Decimal(other), self.imag / Decimal(other))

    def __sub__(self, other):
        if isinstance(other, ComplexDecimal):
            return ComplexDecimal(self.real - other.real, self.imag - other.imag)
        return ComplexDecimal(self.real - Decimal(other), self.imag)

    def __abs__(self):
        return (self.real**2 + self.imag**2).sqrt()

    def to_numpy(self):
        """
        Converts the `ComplexDecimal` to a NumPy array (real, imag).
        """
        return np.array([float(self.real), float(self.imag)])


# Example usage:
if __name__ == "__main__":
    # Create some ComplexDecimal instances
    z1 = ComplexDecimal(Decimal("1.5"), Decimal("2.5"))
    z2 = ComplexDecimal(Decimal("3.0"), Decimal("1.0"))
    print(f"z1 = {z1}, z2 = {z2}")

    # Add, multiply, and conjugate
    print(f"z1 + z2 = {z1 + z2}")
    print(f"z1 * z2 = {z1 * z2}")
    print(f"z1.conjugate() = {z1.conjugate()}")
