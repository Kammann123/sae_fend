"""
PyGeneral includes general purpose methods or functions...
"""

# python native modules

# third-party modules

# sae project


def hash_by_ascii(source: str):
    """ Hashes a string id using the number representation of each
    character from the array. """
    hashed_number = 0
    offset = 0

    for character in reversed(source):
        buffer_number = ord(character)
        for i in range(offset):
            buffer_number *= 10
        hashed_number += buffer_number
        offset += len(str(ord(character)))

    return hashed_number
