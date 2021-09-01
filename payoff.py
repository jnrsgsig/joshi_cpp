from typing import Union
from abc import ABC
from abc import abstractmethod
import numpy as np


class Payoff(ABC):
    @abstractmethod
    def __call__(self, spot_: Union[float,]):
        pass

    @abstractmethod
    def __copy__(self):
        pass


class PayoffCall(Payoff):
    def __init__(self, strike_: float):
        self._strike = strike_

    def __call__(self, spot_: Union[float, np.ndarray]):
        return np.clip(spot_ - self._strike, a_min=0, a_max=None)

    def __copy__(self):
        return self.__class__(self._strike)


class PayoffPut(Payoff):
    def __init__(self, strike_: float):
        self._strike = strike_

    def __call__(self, spot_: Union[float, np.ndarray]):
        return np.clip(self._strike - spot_, a_min=0, a_max=None)

    def __copy__(self):
        return self.__class__(self._strike)


if __name__ == '__main__':
    pass
