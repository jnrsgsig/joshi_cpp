from typing import Union
import numpy as np
from payoff import Payoff


class PayoffDoubleDigital(Payoff):
    def __init__(self, lower_level_: float, upper_level_: float):
        self.lower_level = lower_level_
        self.upper_level = upper_level_

    def __call__(self, spot_: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        return (spot_ > self.lower_level) & (spot_ < self.upper_level)


if __name__ == '__main__':
    pass
