from decimal import Decimal

class ComplexDecimal:

    def __init__(
            self,
            real_part: Decimal = Decimal("0.0"),
            imaginary_part: Decimal = Decimal("0.0")):
        
        self.real = real_part
        self.imag = imaginary_part

    def __add__(self, other):

        # (1): If we're adding compatible data structures:
        if isinstance(other, ComplexDecimal):

            # (1.1): Do the simple addition and return the same structure:
            return ComplexDecimal(self.real + other.real, self.imag + other.imag)
        
        # (2): If the second "argument" of addition is just Decimal...
        if isinstance(other, Decimal):

            # (2.1): ...we assume that it is a REAL Decimal, and add along the real axis ONLY:
            return ComplexDecimal(self.real + other, self.imag)
        
        # (3): Otherwise, it's an incompatible addition:
        return NotImplemented
    
    def __radd__(self, other):

        # (1): To handle the other "commutation order" of addition, pass immediately to `__add__`:
        return self.__add__(other)
    
    def __sub__(self, other):

        # (1): If the structures are the same, then evaluate easily:
        if isinstance(other, ComplexDecimal):

            # (1.1): Subtract across both axes in accordance with complex numbers:
            return ComplexDecimal(self.real - other.real, self.imag - other.imag)
        
        # (2): If the other structure is Decimal, then...
        if isinstance(other, Decimal):

            # (2.1): ... assume it's REAL, and subtract along the real-axis, and return ComplexDecimal:
            return ComplexDecimal(self.real - other, self.imag)
        
        # (3): Otherwise, we didn't cover it:
        return NotImplemented

    def __rsub__(self, other):

        # (1): To handle the other "order" of addition, pass immediately to `__sub__`:
        return self.__sub__(other)

    def __mul__(self, other):

        # (1): If the datatype is ComplexDecimal, we do it easily:
        if isinstance(other, ComplexDecimal):

            # (1.1): Recall that (Re[z1] + iRe[z1])(Re[z2] + iRe[z2]) = (Re[z1]Rez[z2] - Re[z1]Re[z2]) + 
            return ComplexDecimal(
                self.real * other.real - self.imag * other.imag,
                self.real * other.imag + self.imag * other.real
                )
        
        # (2): If the other object is a Decimal, as usual,...
        if isinstance(other, Decimal):

            # (2.1): ... treat it as only having a REAL part, and do the multiplication:
            return ComplexDecimal(self.real * other, self.imag * other)
        
        # (3): Otherwise, we didn't code it:
        return NotImplemented
    
    def __rmul__(self, other):

        # (1): To preserve commutation of multiplication, pass to `__mul__`:
        return self.__mul__(other)

    def __truediv__(self, other):

        # (1): If we can divide with ComplexDecimal, (a+ib)/(c+id),...
        if isinstance(other, ComplexDecimal):

            # (1.1): ... then the denominator is c^2 + d^2:
            denominator = other.real**2 + other.imag**2

            # (1.2): ... and the numerators of the new number are as listed below:
            return ComplexDecimal(
                (self.real * other.real + self.imag * other.imag) / denominator,
                (self.imag * other.real - self.real * other.imag) / denominator,
            )
        
        # (2): If the other number is Decimal only...
        if isinstance(other, Decimal):

            # (2.1): ... then just divide by the (only-extant) real part:
            return ComplexDecimal(self.real / other, self.imag / other)
        
        # (3): Otherwise, we don't handle it:
        return NotImplemented
    
    def __rtruediv__(self, other):

        # (1): We are dealing with Decimal * ComplexDecimal now:
        if isinstance(other, Decimal):

            # (1.1): Evaluate the fancy denominator of the ComplexDecimal first:
            denominator = self.real**2 + self.imag**2

            # (1.2): If you do the algebra, you find that the result below is what follows:
           return ComplexDecimal((other * self.real) / denominator, (-other * self.imag) / denominator)
       
        # (2): Otherwise, we don't handle it:
        return NotImplemented
  
    def conjugate(self):
        """
        Conjugate a ComplexDecimal type, i.e. flip its imaginary part.

        ## Examples:
        ```python
        conjugate(ComplexDecimal("5.0", "6.7"))
        >>> ComplexDecimal("5.0", "-6.7")
        ```
        """
        
        return ComplexDecimal(self.real, -self.imag)

    def __repr__(self):

        # (1): Provide the most suggestive representation:
        return f"({self.real} + {self.imag}i)"

    def __eq__(self, other):

        # (1): z1 = z2 iff Re[z1] = Re[z2] && Im[z1] = Re[z2], so we code that easily:
        return self.real == other.real and self.imag == other.imag

def test():

    constant_decimal = Decimal("2.00001")
    print(f"> Initialized constant_decimal as type {type(constant_decimal)}")

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

    print(f"> constant_decimal + cff_h = {constant_decimal + cff_h}")
    print(f"> constant_decimal + cff_h_tilde = {constant_decimal + cff_h_tilde}")
    print(f"> constant_decimal - cff_h = {constant_decimal - cff_h}")
    print(f"> constant_decimal - cff_h_tilde = {constant_decimal + cff_h_tilde}")
    print(f"> constant_decimal * cff_h = {constant_decimal * cff_h}")
    print(f"> constant_decimal * cff_h_tilde = {constant_decimal * cff_h_tilde}")
    print(f"> constant_decimal / cff_h = {constant_decimal / cff_h}")
    print(f"> constant_decimal / cff_h_tilde = {constant_decimal / cff_h_tilde}")

    

if __name__ == "__main__":
    
    test()
