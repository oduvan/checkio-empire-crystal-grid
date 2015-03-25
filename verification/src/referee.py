from checkio_referee import RefereeBase

import settings
import settings_env
from tests import TESTS

cover = """def cover(f, data):
    return f([[str(ch) for ch in row] for row in data])
"""


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "check_grid"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": None,
        "javascript": None
    }
