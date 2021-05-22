"""
    Knowing the difference between bytes and str

        there are two types that represent sequences of character data: bytes and str.
        Instances of bytes contain raw, unsigned 8-bit values (often displayed in the
        ASCII encoding). Instances of str contain Unicode code points that represent
        textual characters from human languages.
"""

from typing import Union


# Defining bytes instances
my_byte = b"h\x65llo"
b_one = b"one"
b_two = b"two"

# Defining str instances
my_string = "a\u0300 python"
s_one = "one"
s_two = "two"


def to_str(bytes_or_str: Union[bytes, str]) -> str:
    """
    This function takes a bytes or string instance and always returns a str
    :param bytes_or_str: bytes or str instance
    :return: str instance
    """
    if isinstance(bytes_or_str, bytes):
        result = bytes_or_str.decode("utf-8")
    else:
        result = bytes_or_str
    return result


def to_bytes(str_or_bytes: Union[bytes, str]) -> bytes:
    """
    This function takes a bytes or string instance and always returns a bytes
    :param str_or_bytes: str or bytes instance
    :return: bytes instance
    """
    if isinstance(str_or_bytes, str):
        result = str_or_bytes.encode("utf-8")
    else:
        result = str_or_bytes
    return result


if __name__ == '__main__':

    print(f"list of my_byte: {list(my_byte)}")
    print(f"type of my_byte: {type(my_byte)}")
    print(f"my_byte: {my_byte}")

    # This is the output separator
    print("*-*" * 50)

    print(f"list of my_byte: {list(my_string)}")
    print(f"type of my_byte: {type(my_string)}")
    print(f"my_byte: {my_string}")

    print("*-*" * 50)

    # Testing to_str function
    print(repr(to_str(b"foo")))
    print(repr(to_str("bar")))
