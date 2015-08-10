from checkio_referee import RefereeBase
from checkio_referee import validators, ENV_NAME



import settings_env
from tests import TESTS

Validator = validators.FloatEqualValidator

Validator.PRECISION = 2


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "adamantite_proportion"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "adamantiteProportion"
    }
    VALIDATOR = Validator
