import numpy as np
from typing import Union
from payoff import Payoff


class PayoffDigitalCall(Payoff):
    def __init__(self, strike_: float):
        super().__init__()
        self._strike = strike_

    def __call__(self, spot_: Union[float, np.ndarray]):
        return int(spot_ > self._strike)

    def __copy__(self):
        return self.__class__(self._strike)


class PayoffDigitalPut(Payoff):
    def __init__(self, strike_: float):
        super().__init__()
        self._strike = strike_

    def __call__(self, spot_: Union[float, np.ndarray]):
        return int(spot_ <= self._strike)

    def __copy__(self):
        return self.__class__(self._strike)


if __name__ == '__main__':
    pass
