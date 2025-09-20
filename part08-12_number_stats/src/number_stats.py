# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0


    def add_number(self, number:int):
        self.numbers += 1
        self.sum += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        if self.numbers == 0:
            return 0
        else:
            return self.sum
    
    def average(self):
        if self.numbers == 0:
            return 0
        else:
            avg = self.sum / self.numbers
            return avg

number_stats = NumberStats()   
odd = NumberStats()
even = NumberStats()

while True:
    user_input = int(input("Please type in integer numbers:"))
    if user_input == -1:
        break
    
    if user_input % 2 == 0:
        even.add_number(user_input)
    else: 
        odd.add_number(user_input)

    number_stats.add_number(user_input)

print(f"Sum of numbers: {number_stats.get_sum()}")
print(f"Mean of numbers: {number_stats.average()}")
print(f"Sum of even numbers: {even.get_sum()}")
print(f"Sum of odd numbers: {odd.get_sum()}")

