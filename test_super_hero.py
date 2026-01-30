import pytest
from contextlib import nullcontext as does_not_raise

from super_hero import find_the_best


@pytest.mark.parametrize(
        "sex, have_work, result, expectation",
        [
            ('Male', True, ('Ymir', 30480.0), does_not_raise()),
            ('Male', False, ('Utgard-Loki', 1520.0), does_not_raise()),
            ('Female', True, ('Giganta', 6250.0), does_not_raise()),
            ('Female', False, ('Bloodaxe', 218.0), does_not_raise()),
            ('wtf', True, None, pytest.raises(IndexError)),
            ('wtf', False, None, pytest.raises(IndexError))
        ]
)
def test_find_the_best(sex, have_work, result, expectation):
    with expectation:
        assert find_the_best(sex, have_work) == result  

@pytest.mark.parametrize(
    "sex, have_work",
        [
            ('Male', True),
            ('Female', True),
            ('Male', False),
            ('Female', False)
        ]
)
def test_result_structure(sex, have_work):
    result = find_the_best(sex, have_work)
    # проверяем, что выход - это кортеж
    assert isinstance(result, tuple) 
    assert len(result) == 2