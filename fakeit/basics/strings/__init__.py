from itertools import combinations, combinations_with_replacement, permutations
from random import randint
from string import ascii_letters, digits

from fakeit.exceptions import EmptyAlphabet, InvalidRange


def fake_literal(alphabet=ascii_letters + digits):
    if not alphabet:
        raise EmptyAlphabet
    return alphabet[randint(0, len(alphabet) - 1)]


def fake_string(
    min_length=0, max_length=16, alphabet=ascii_letters + digits, unique=False
):
    if max_length < min_length:
        raise InvalidRange

    if (max_length > len(alphabet)) and unique:
        raise InvalidRange

    length = randint(min_length, max_length)

    if unique:
        cache = set()
        result = []
        while len(result) != length:
            buf = fake_literal(alphabet=list((set(alphabet) - cache)))
            cache.add(buf)
            result.append(buf)
        return "".join(result)
    else:
        return "".join(fake_literal(alphabet=alphabet) for _ in range(length))


def fake_strings(
    amount,
    min_length=0,
    max_length=16,
    alphabet=ascii_letters + digits,
    unique=False,
    unique_strings=False,
):
    if unique:
        cache = set()
        result = []
        while len(result) != amount:
            buf = fake_string(
                min_length=min_length,
                max_length=max_length,
                alphabet=alphabet,
                unique=unique_strings,
            )
            cache.add(buf)
            result.append(buf)
            yield buf
        else:
            return
    else:
        yield from (
            fake_string(
                min_length=min_length,
                max_length=max_length,
                alphabet=alphabet,
                unique=unique_strings,
            )
            for _ in range(amount)
        )


def all_combinations_fake_string(
    min_length=0, max_length=16, alphabet=ascii_letters + digits
):
    length = randint(min_length, max_length)
    yield from ("".join(x) for x in combinations(alphabet, length))


def all_combinations_with_replacement_fake_string(
    min_length=0, max_length=16, alphabet=ascii_letters + digits
):
    length = randint(min_length, max_length)
    yield from ("".join(x) for x in combinations_with_replacement(alphabet, length))


def all_permutations_fake_string(alphabet=ascii_letters + digits):
    yield from ("".join(x) for x in permutations(alphabet, len(alphabet)))
