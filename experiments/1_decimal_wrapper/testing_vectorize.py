from decimal import Decimal

import numpy as np

def run():
    
    x_Bjorken = np.array([Decimal("0.34") for _ in range(10)])
    print(f"> Initialized x_Bjorken type {type(x_Bjorken)}")

    squared_Q_momentum_transfer = np.array([Decimal("1.82") for _ in range(10)])
    print(f"> Initialized squared_Q_momentum_transfer as type {type(squared_Q_momentum_transfer)}")

    def compute_epsilon(x_Bjorken: float, squared_Q_momentum_transfer: float):

        return (Decimal("2.") * x_Bjorken * _MASS_OF_PROTON_IN_GEV) / squared_Q_momentum_transfer

    epsilon = np.vectorize(compute_epsilon)(x_Bjorken, squared_Q_momentum_transfer)
    print(f"> Calculated epsilon with vectorize to be:\n{epsilon}")

if __name__ == "__main__":

    _MASS_OF_PROTON_IN_GEV = Decimal("0.938")
    print(f"> Initialized _MASS_OF_PROTON_IN_GEV as type {type(_MASS_OF_PROTON_IN_GEV)}")

    run()
    