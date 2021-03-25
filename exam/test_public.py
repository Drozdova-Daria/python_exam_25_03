import pytest

from main import hello


class Case:
    def __init__(self, name: str, expected: dict):
        self._name = name
        self.expected = expected

    def __str__(self) -> str:
        return 'test_{}'.format(self._name)


TEST_CASES = [
    Case(name='basis', expected='Hello World'
]


@pytest.mark.parametrize('test_case', TEST_CASES, ids=str)
def test_hello_world(test_case: Case) -> None:
    answer = hello()
)
    assert answer == test_case.expected
