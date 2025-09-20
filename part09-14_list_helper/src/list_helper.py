# WRITE YOUR SOLUTION HERE:
class ListHelper:

    def greatest_frequency(my_list: list):
        most_freq = {}
        for char in my_list:
            if char in most_freq:
                most_freq[char] += 1
            else:
                most_freq[char] = 1

        freq = max(most_freq, key=most_freq.get)
        return freq
    
    def doubles(my_list: list):
        most_freq = {}
        for char in my_list:
            if char in most_freq:
                most_freq[char] += 1
            else:
                most_freq[char] = 1
        
        return sum(1 for i in most_freq.values() if i >= 2)
    

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))