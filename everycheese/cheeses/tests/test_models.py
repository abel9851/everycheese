import pytest

from ..models import Cheese

# Connects our test with our database
pytestmark = pytest.mark.django_db


def test__str__():
    cheese = Cheese.objects.create(
        name="Stracchino",
        description="Semi-sweet cheese eaten wsith starches.",
        firmness=Cheese.Firmness.SOFT,
    )

    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"
