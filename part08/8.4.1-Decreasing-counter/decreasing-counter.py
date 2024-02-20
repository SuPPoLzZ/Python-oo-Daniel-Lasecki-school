class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.original_value = initial_value
        self.value = initial_value
    def print_value(self):
        print("value:", self.value)
        
    def set_to_zero(self):
        self.value = 0
        print("value:", self.value)
        
    def reset_original_value(self):
        self.value = self.original_value
        return self.value

    def decrease(self):
    
        if self.value != 0:
            self.value = self.value - 1
            return self.value
        pass
    
    
counter = DecreasingCounter(10)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.set_to_zero()
counter.reset_original_value()
counter.print_value()

