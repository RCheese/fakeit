from random import randint, uniform


def fake_int(min=0, max=256):
    return randint(min, max)


def fake_float(min=0, max=1):
    return uniform(min, max)


def fake_complex(min_real, max_real, min_image, max_image, round=False):
    if round:
        return complex(randint(min_real, max_real), randint(min_image, max_image))
    return complex(uniform(min_real, max_real), uniform(min_image, max_image))
