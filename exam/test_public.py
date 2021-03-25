import pytest

from main import words


class Case:
    def __init__(self, name: str, expected: dict):
        self._name = name
        self.expected = expected

    def __str__(self) -> str:
        return 'test_{}'.format(self._name)


TEST_CASES = [
    Case(name='basis', expected=['Ten', 'little', 'Crip', 'niggaz', 'runnin', 'outside\n', 'All', 'from', 'the', 'turf', 'and', 'they', 'bangin', 'out', 'lives\n', 'Far', 'from', 'a', 'scrub', 'cuzz', 'from', 'the', 'Eastside\n', 'Where', 'they', "don't", 'die', 'they', 'just', 'multiply\n', 'So..', "don't", 'give', 'them', 'niggaz', 'a', 'reason\n', 'To', 'turn', 'it', 'into', 'spray', 'season\n', "Don't", 'give', 'them', 'niggaz', 'a', 'reason\n', 'Because', "they'll", 'turn', 'it', 'into', 'Crip', 'season\n', 'The', "gangsta's", 'back,', 'the', 'bank', 'is', 'fat\n']
)
]


@pytest.mark.parametrize('test_case', TEST_CASES, ids=str)
def test_hello_world(test_case: Case) -> None:
    answer = words('test.txt')
    assert answer == test_case.expected
