from random import randint, uniform


def get_int(min, max):
    return randint(min, max)


def get_float(min, max):
    return uniform(min, max)


def get_complex(min_real, max_real, min_image, max_image, round=False):
    if round:
        return complex(randint(min_real, max_real), randint(min_image, max_image))
    return complex(uniform(min_real, max_real), uniform(min_image, max_image))
