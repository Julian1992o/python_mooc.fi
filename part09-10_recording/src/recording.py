# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length):
        if length < 0:
            raise ValueError("Length cannot be negative")
        self.__length = length

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        if length < 0:
            raise ValueError("Error.")
        else:
            self.__length = length