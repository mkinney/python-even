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
