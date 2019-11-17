Simple python function and testing using assert

To run:
    python3 evenfunc.py

Add " == False" to the end of this line "assert is_even(3)".

Run it again:
    python3 evenfunc.py

This works. But, when one line fails, all of the other "tests" will not run.

We can put code into a class like even.py.

Still can "test" the code like this:
    python3 even.py

But there is a better way.

Check out even_test.py
    python3 -m unittest even_test.py

or, if you want to see the details of the tests:
    python3 -m unittest -v even_test.py

Now, you can change the code knowing that you have tests that validate the code.

For instance, this code:

    def is_even(self):
        if self.i % 2 == 0:
            return True
        else:
            return False

Can be simplified to:

    def is_even(self):
        return self.i % 2 == 0

With testing, you want to test common cases and edge cases. What happens if you use a negative number? What about a really large number? These could be added as tests. If the test does not pass, then write the code to ensure the tests still pass.
