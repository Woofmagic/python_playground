from decimal import Decimal

class ComplexDecimal:

    def __init__(self, real_part: Decimal = Decimal("0.0"), imaginary_part: Decimal = Decimal("0.0")):
        self.real = real_part
        self.imag = imaginary_part

    def __add__(self, other):
        if isinstance(other, ComplexDecimal):
            return ComplexDecimal(self.real + other.real, self.imag + other.imag)
        return ComplexDecimal(self.real + Decimal(other), self.imag)

    def __mul__(self, other):
        if isinstance(other, ComplexDecimal):
            return ComplexDecimal(
                self.real * other.real - self.imag * other.imag,
                self.real * other.imag + self.imag * other.real)
        return ComplexDecimal(self.real * Decimal(other), self.imag * Decimal(other))

    def conjugate(self):
        return ComplexDecimal(self.real, -self.imag)

    def __repr__(self):
        return f"({self.real} + {self.imag}i)"

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __truediv__(self, other):
        if isinstance(other, ComplexDecimal):
            denominator = other.real**2 + other.imag**2
            return ComplexDecimal(
                (self.real * other.real + self.imag * other.imag) / denominator,
                (self.imag * other.real - self.real * other.imag) / denominator)
        return ComplexDecimal(self.real / Decimal(other), self.imag / Decimal(other))

    def __sub__(self, other):
        if isinstance(other, ComplexDecimal):
            return ComplexDecimal(self.real - other.real, self.imag - other.imag)
        return ComplexDecimal(self.real - Decimal(other), self.imag)

    def __abs__(self):
        return ComplexDecimal((self.real**2 + self.imag**2).sqrt())

def run():

    cff_h_real_part = Decimal("-0.884")
    cff_h_imaginary_part = Decimal("1.851")
    cff_h = ComplexDecimal(cff_h_real_part, cff_h_imaginary_part)

    print(f"> Initialized cff_h as type {type(cff_h)}")
    
    cff_h_tilde_real_part = Decimal("3.118")
    cff_h_tilde_imaginary_part = Decimal("0.911")
    cff_h_tilde = ComplexDecimal(cff_h_tilde_real_part, cff_h_tilde_imaginary_part)

    print(f"> Initialized cff_h_tilde as type {type(cff_h)}")

    print(f"> cff_h + cff_h_tilde = {cff_h + cff_h_tilde}")
    print(f"> cff_h - cff_h_tilde = {cff_h - cff_h_tilde}")
    print(f"> cff_h * cff_h_tilde = {cff_h * cff_h_tilde}")
    print(f"> cff_h / cff_h_tilde = {cff_h / cff_h_tilde}")
    print(f"> Conjugate cff_h: {cff_h.conjugate()}")
    print(f"> Conjugate cff_h_tilde: {cff_h_tilde.conjugate()}")

    

if __name__ == "__main__":
    
    run()
