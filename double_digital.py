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
    from simple_mc import simple_monte_carlo

    expiry = 1
    lower_level = 0.5
    upper_level = 1.5
    spot = 1
    vol = 1
    r = 1
    number_of_paths = 10 ** 6
    result_double_digital = simple_monte_carlo(
        PayoffDoubleDigital(lower_level, upper_level), expiry, spot, vol, r, number_of_paths)
    print(result_double_digital)
