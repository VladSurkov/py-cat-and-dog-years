import pytest

from app.main import get_human_age

def test_should_return_error_if_input_values_are_not_int():
    with pytest.raises(TypeError):
        get_human_age("50", 15)
        get_human_age(50, "15")

def test_should_return_error_if_input_values_less_than_0():
    with pytest.raises(ValueError):
        get_human_age(-20, 15)
        get_human_age(15, -20)

def test_should_return_list_with_correct_cat_and_dog_ages():
    assert get_human_age(100, 100) == [21, 17]