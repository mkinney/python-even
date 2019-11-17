def is_even(i):
    if i % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    assert is_even(1) == False
    assert is_even(2)
    assert is_even(3)
    assert is_even(4)
