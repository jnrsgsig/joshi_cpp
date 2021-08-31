import numpy as np
from numpy.random import standard_normal
from payoff import Payoff


def simple_monte_carlo(the_payoff: Payoff, expiry: float, spot: float, vol: float, r: float, number_of_paths: float):
    variance = vol * vol * expiry
    root_variance = np.sqrt(variance)
    ito_correction = - 0.5 * variance
    moved_spot = spot * np.exp(r * expiry + ito_correction)
    this_gaussian= standard_normal(number_of_paths)
    this_spot = moved_spot * np.exp(root_variance * this_gaussian)
    mean_payoff = the_payoff(this_spot).mean()
    mean_payoff *= np.exp(- r * expiry)
    return mean_payoff


if __name__ == '__main__':
    from payoff import PayoffCall
    from payoff import PayoffPut
    expiry = 1
    strike = 1
    spot = 1
    vol = 1
    r = 1
    number_of_paths = 10 ** 6
    result_call = simple_monte_carlo(PayoffCall(strike), expiry, spot, vol, r, number_of_paths)
    result_put = simple_monte_carlo(PayoffPut(strike), expiry, spot, vol, r, number_of_paths)
    print(result_call, result_put)
