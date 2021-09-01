from typing import Union
import numpy as np

from payoff import Payoff


class VanillaOption:
    def __init__(self, the_payoff_: Payoff, expiry_: float):
        self._the_payoff = the_payoff_
        self._expiry = expiry_

    @property
    def expiry(self):
        return self._expiry

    def option_payoff(self, spot: Union[float, np.ndarray]):
        return self._the_payoff(spot)
