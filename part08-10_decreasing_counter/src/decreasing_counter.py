# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.value_start = self.value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -=1
    
    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.value_start

    # Write the rest of the methods here!

if __name__ == "__main__":
    new_value = DecreasingCounter(20)
    new_value.decrease()
    new_value.print_value()