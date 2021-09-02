import copy
from payoff import PayoffCall, PayoffPut
from vanilla_option import VanillaOption
from simple_mc import simple_monte_carlo


def main():
    expiry: float = 1
    strike: float = 1
    spot: float = 1
    vol: float = 1
    r: float = 200e-4
    number_of_paths: int = 10 ** 6
    the_payoff = PayoffCall(strike)
    the_option = VanillaOption(the_payoff, expiry)
    result = simple_monte_carlo(the_option, spot, vol, r, number_of_paths)
    print(result)
    second_option = copy.deepcopy(the_option)
    result = simple_monte_carlo(second_option, spot, vol, r, number_of_paths)
    print(result)
    other_payoff = PayoffPut(strike)
    third_option = VanillaOption(other_payoff, expiry)
    the_option = third_option
    result = simple_monte_carlo(the_option, spot, vol, r, number_of_paths)
    print(result)


if __name__ == '__main__':
    main()
