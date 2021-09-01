from double_digital import PayoffDoubleDigital
from vanilla_option import VanillaOption
from simple_mc import simple_monte_carlo


def main():
    expiry: float = 1
    low: float = 0.5
    up: float = 1.5
    spot: float = 1
    vol: float = 1
    r: float = 200e-4
    number_of_paths: int = 10 ** 6
    the_payoff = PayoffDoubleDigital(low, up)
    the_option = VanillaOption(the_payoff, expiry)
    result = simple_monte_carlo(the_option, spot, vol, r, number_of_paths)
    print(result)


if __name__ == '__main__':
    main()
