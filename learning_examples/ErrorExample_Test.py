import pytest
from learning_examples.ErrorExample import an_example_error


def test_good_case():
    assert an_example_error(7) == 7


def test_bad_case():
    with pytest.raises(ValueError):
        an_example_error(3)
