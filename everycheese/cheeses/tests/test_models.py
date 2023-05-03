import pytest

from .factories import CheeseFactory

# Connects our test with our database
pytestmark = pytest.mark.django_db


def test__str__():
    cheese = CheeseFactory()

    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name
