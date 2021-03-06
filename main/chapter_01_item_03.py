"""
    Prefer Interpolated F-Strings Over C-style Format Strings and str.format
"""

# Defining binary and hexadecimal variables
binary = 0b10111011
hexadecimal = 0xc5f

key = "my_var"
value = 1.234

pantry = [
    ("avocados", 125),
    ("bananas", 2.5),
    ("cherries", 15)
]

template = "%s loves food, See %s cook."
name = "everlookneversee"


if __name__ == '__main__':
    # Converting binary and hexadecimal values to integer strings
    print("Binary is %d, hexadecimal is %d" % (binary, hexadecimal))

    print("\n" + "*-*" * 50 + "\n")

    # First problem in c-style string formatting
    formatted = "%-10s = %.2f" % (key, value)
    print(formatted)

    try:
        formatted = "%-10s = %.2f" % (value, key)
        print(formatted)
    except TypeError:
        print("Must be real number, not str")

    try:
        formatted = "%.2f = %-10s" % (key, value)
        print(formatted)
    except TypeError:
        print("Must be real number, not str")

    print("\n" + "*-*" * 50 + "\n")

    # Second problem in c-style string formatting
    for i, (item , count) in enumerate(pantry):
        print('#%d: %-10s = %.2f' % (i, item, count))

    print("\n")

    for i, (item, count) in enumerate(pantry):
        print('#%d: %-10s = %d' % (
            i + 1,
            item.title(),
            round(count)
        ))

    print("\n" + "*-*" * 50 + "\n")

    # Third problem in c-style string formatting
    formatted = template % (name, name)
    print(formatted)

    formatted = template % (name.title(), name.title())
    print(formatted)
