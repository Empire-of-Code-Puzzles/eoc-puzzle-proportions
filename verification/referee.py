from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiORefereeLevels

from tests import TESTS
from fractions import Fraction

cover = """def cover(func, data):
    from fractions import Fraction
    fdata = dict([(k, Fraction(*v)) for k, v in data.items()])
    res = func(fdata)
    if not isinstance(res, Fraction):
        raise TypeError("Result must be Fraction")
    return res.numerator, res.denominator
"""


def checker(answer, user_result):
    return Fraction(*answer) == Fraction(*user_result), None


api.add_listener(
    ON_CONNECT,
    CheckiORefereeLevels(
        tests=TESTS,
        cover_code={
            'python-27': cover,
            'python-3': cover
        }).on_ready)
