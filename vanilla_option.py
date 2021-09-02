from typing import Union
from copy import copy
import numpy as np

from payoff import Payoff


class VanillaOption:
    def __init__(self, the_payoff_: Payoff, expiry_: float):
        self._the_payoff = copy(the_payoff_)
        self._expiry = expiry_

    @property
    def expiry(self):
        return self._expiry

    def option_payoff(self, spot: Union[float, np.ndarray]):
        return self._the_payoff(spot)

    def __copy__(self):
        return self.__class__(copy(self._the_payoff), self._expiry)
