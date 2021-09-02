import numpy as np
from numpy.random import standard_normal
from vanilla_option import VanillaOption


def simple_monte_carlo(vanilla_option: VanillaOption, spot: float, vol: float, r: float, number_of_paths: int):
    expiry = vanilla_option.expiry
    variance = vol * vol * expiry
    root_variance = np.sqrt(variance)
    ito_correction = - 0.5 * variance
    moved_spot = spot * np.exp(r * expiry + ito_correction)
    this_gaussian = standard_normal(number_of_paths)
    this_spot = moved_spot * np.exp(root_variance * this_gaussian)
    mean_payoff = vanilla_option.option_payoff(this_spot).mean()
    mean_payoff *= np.exp(- r * expiry)
    return mean_payoff


if __name__ == '__main__':
    pass
