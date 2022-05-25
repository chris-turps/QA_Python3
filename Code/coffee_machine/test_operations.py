import operations
from operations import *
import pytest

@pytest.fixture()
def costOfEspresso(monkeypatch):
    monkeypatch.setattr(operations, "coffeeChoice", 1)
    return coffee_types[1].cost

class Test_takePayment():
    def test_exactSum(s, costOfEspresso):
        assert takePayment(costOfEspresso) == CM_state.CREATE_TRANSACTION

    def test_overPay(s, costOfEspresso):
        assert takePayment(costOfEspresso + 10) == CM_state.GIVE_CHANGE

