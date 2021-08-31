from typing import Union
from abc import ABC
from abc import abstractmethod
import numpy as np


class Payoff(ABC):
    @abstractmethod
    def __call__(self, spot_: Union[float,]):
        pass


class PayoffCall(Payoff):
    def __init__(self, strike_: float):
        self.strike = strike_

    def __call__(self, spot_: Union[float,]):
        return np.clip(spot_ - self.strike, a_min=0, a_max=None)


class PayoffPut(Payoff):
    def __init__(self, strike_: float):
        self.strike = strike_

    def __call__(self, spot_: Union[float,]):
        return np.clip(self.strike - spot_, a_min=0, a_max=None)


if __name__ == '__main__':
    payoff_call = PayoffCall(1)
    print(payoff_call(0), payoff_call(2))
    payoff_put = PayoffPut(1)
    print(payoff_put(0), payoff_put(2))
