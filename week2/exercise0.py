# -*- coding: UTF-8 -*-
"""Modify each function until the tests pass."""


def add_5(a_number):

    x1 = (a_number+5)
    return float(x1)


def adder(a_number, another_number):

    x2 = (a_number + another_number)
    return float(x2)

    



def shout(a_string):
    loud = (a_string.upper())
    return str(loud)


def really_shout(a_string):
    really_loud = (shout(a_string)+"!")
    return really_loud   

def shout_with_a_number(a_string, a_number):

    x3 = (shout(a_string))
    x4 = str(a_number)
    x5 = x3 + " " + x4

    return str(x5)


def minitest(f, args, expected):
    """Run a function with a list of args and print a response.

    This is a helper. Don't edit it.
    """
    result = f(*args)
    template = "expect {name}({args}) == {expected} => {result}"
    print(template.format(name=f.__name__,
                          args=str(args)[1:-1],
                          result=result == expected,
                          expected=expected))
    return result == expected


if __name__ == "__main__":
    minitest(add_5, [1], 6)
    minitest(add_5, [6], 11)
    minitest(add_5, [-3], 2)
    minitest(add_5, [0.5], 5.5)
    minitest(adder, [-0.5, -0.5], -1)
    minitest(adder, [2, 2], 4)
    minitest(adder, [2, -2], 0)
    minitest(shout, ["hello"], "HELLO")
    minitest(really_shout, ["hello"], "HELLO!")
    minitest(really_shout, [""], "!")
    minitest(really_shout, ["!"], "!!")
    minitest(shout_with_a_number, ('hello', 42), "HELLO 42")
    print("""
          This section does a quick test on your results and prints them nicely
          It's NOT the official tests, they are in tests.py as usual.
          Add to these tests, give them arguments etc. to make sure that your
          code is robust to the situations that you'll see in action.

          REMEMBER: these aren't the tests that you submit, these are just
          there to keep you sane.""")
