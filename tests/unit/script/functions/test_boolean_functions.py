import pytest
from unit.script.conftest import single_variable_output

from ytdl_sub.script.script import Script


class TestBooleanFunctions:
    @pytest.mark.parametrize(
        "lhs, rhs, expected_output",
        [
            ("'abc'", "'abc'", True),
            ("123", "123", True),
            ("3.14", "3.14", True),
            ("True", "True", True),
            ("False", "False", True),
            ("[1, 2, 3]", "[1, 2, 3]", True),
            ("{'key': 'value'}", "{'key': 'value'}", True),
            ("{'key': 'value'}", 5, False),
            ("{'key': 'value'}", "[1, 2, 3]", False),
        ],
    )
    @pytest.mark.parametrize("is_ne", [True, False])
    def test_eq_ne(self, lhs: str, rhs: str, expected_output: bool, is_ne: bool):
        op = "ne" if is_ne else "eq"
        output = single_variable_output(f"{{%{op}({lhs}, {rhs})}}")

        if is_ne:
            assert output != expected_output
        else:
            assert output == expected_output

    @pytest.mark.parametrize(
        "lhs, rhs, expected_output",
        [
            ("'abc'", "'abc'", True),
            ("123", "123", True),
            ("3.14", "3.14", True),
            ("3.14", "4.0", True),
        ],
    )
    @pytest.mark.parametrize("is_gt", [True, False])
    def test_lte_gt(self, lhs: str, rhs: str, expected_output: bool, is_gt: bool):
        op = "gt" if is_gt else "lte"
        output = single_variable_output(f"{{%{op}({lhs}, {rhs})}}")

        if is_gt:
            assert output != expected_output
        else:
            assert output == expected_output

    @pytest.mark.parametrize(
        "lhs, rhs, expected_output",
        [
            ("'abc'", "'abc'", True),
            ("123", "123", True),
            ("3.14", "3.14", True),
            ("5.32", "4", True),
            ("3.14", "4.0", False),
        ],
    )
    @pytest.mark.parametrize("is_lt", [True, False])
    def test_gte_lt(self, lhs: str, rhs: str, expected_output: bool, is_lt: bool):
        op = "lt" if is_lt else "gte"
        output = single_variable_output(f"{{%{op}({lhs}, {rhs})}}")

        if is_lt:
            assert output != expected_output
        else:
            assert output == expected_output

    @pytest.mark.parametrize(
        "values, expected_output",
        [
            ("True", True),
            ("True, True", True),
            ("True, True, True", True),
            ("False", False),
            ("False, True", False),
            ("True, False, True", False),
        ],
    )
    def test_and(self, values: str, expected_output: bool):
        output = single_variable_output(f"{{%and({values})}}")
        assert output == expected_output

    @pytest.mark.parametrize(
        "values, expected_output",
        [
            ("True", True),
            ("True, True", True),
            ("True, True, True", True),
            ("False", False),
            ("False, True", True),
            ("True, False, True", True),
            ("False, False, False", False),
        ],
    )
    def test_or(self, values: str, expected_output: bool):
        output = single_variable_output(f"{{%or({values})}}")
        assert output == expected_output

    @pytest.mark.parametrize(
        "values, expected_output",
        [
            ("True", True),
            ("True, True", False),
            ("True, True, True", False),
            ("False", False),
            ("False, True", True),
            ("True, False, True", False),
            ("False, False, False", False),
            ("False, True, False", True),
        ],
    )
    def test_xor(self, values: str, expected_output: bool):
        output = single_variable_output(f"{{%xor({values})}}")
        assert output == expected_output

    @pytest.mark.parametrize(
        "value, expected_output",
        [
            ("True", False),
            ("False", True),
        ],
    )
    def test_not(self, value: str, expected_output: bool):
        output = single_variable_output(f"{{%not({value})}}")
        assert output == expected_output

    @pytest.mark.parametrize(
        "value, expected_output",
        [
            ("null", True),
            ("''", True),
            ("0", False),
            ("{}", False),
            ("'h'", False),
        ],
    )
    def test_is_null(self, value: str, expected_output: bool):
        output = single_variable_output(f"{{%is_null({value})}}")
        assert output == expected_output
