import operations
from operations import *
import pytest

@pytest.fixture()
def costOfEspresso(monkeypatch):
    espressoIndex = coffee_names.index("Espresso")
    monkeypatch.setattr(operations, "coffeeChoice", espressoIndex)
    return coffee_types[espressoIndex].cost

class Test_takePayment():
    def test_exactSum(s, costOfEspresso):
        assert takePayment(costOfEspresso) == CM_state.CREATE_TRANSACTION

    def test_overPay(s, costOfEspresso):
        assert takePayment(costOfEspresso + 10) == CM_state.GIVE_CHANGE

    def test_zeroPay(s, costOfEspresso):
        assert takePayment(0) == CM_state.GET_COFFEE_SELECTION
