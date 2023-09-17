#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size=None):
        self._condition = "New"
        self.brand = brand
        self._size = 0
        if size is not None:
            self.size = size

    def get_size(self):
        return self._size

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("Size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")

    size = property(get_size, set_size)

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, new_condition):
        if new_condition in ["New", "Used", "Worn"]:
            self._condition = new_condition
        else:
            print("Invalid condition")

# Example usage:
shoe = Shoe("Nike", 9)
print(f"Brand: {shoe.brand}")
print(f"Size: {shoe.size}")
shoe.size = 10
print(f"New Size: {shoe.size}")
shoe.cobble()
shoe.condition = "Used"
print(f"Condition: {shoe.condition}")
