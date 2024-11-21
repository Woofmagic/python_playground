class Fancy:
    def __init__(self, initial_value: float, final_value: float):
        self.initial_value = initial_value
        self.final_value = final_value

    def get_initial_value(self):
        return self.initial_value
    
    def get_final_value(self):
        return self.final_value
    
    def mysterious_operation(self):
        import math
        return (self.final_value * self.initial_value) / math.pi