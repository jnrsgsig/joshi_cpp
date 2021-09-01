from payoff import Payoff


class PayoffDigitalCall(Payoff):
    def __init__(self, strike_: float):
        self._strike = strike_

    def __call__(self, spot_: Union[float, np.ndarray]):
        return int(spot_ > self._strike)


class PayoffDigitalPut(Payoff):
    def __init__(self, strike_: float):
        self._strike = strike_

    def __call__(self, spot_: Union[float, np.ndarray]):
        return int(spot_ <= self._strike)


if __name__ == '__main__':
    pass
