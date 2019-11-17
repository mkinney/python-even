class Even:

    def __init__(self, i):
        self.i = i

    def is_even(self):
        if self.i % 2 == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    # Can still test code like this... (but there is a better way)
    assert Even(1).is_even() == False
    assert Even(2).is_even()
