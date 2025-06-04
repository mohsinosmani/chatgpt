"""Calculate ROI and payback period for a project."""

import argparse


def calculate_roi(net_profit: float, investment: float) -> float:
    """Return on investment as a percentage."""
    if investment == 0:
        raise ValueError("Investment cannot be zero.")
    return (net_profit / investment) * 100


def calculate_payback_period(initial_investment: float, annual_cash_flow: float) -> float:
    """Compute how many years it will take to recoup the investment."""
    if annual_cash_flow <= 0:
        raise ValueError("Annual cash flow must be positive.")
    return initial_investment / annual_cash_flow


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate ROI and Payback period of a project."
    )
    parser.add_argument(
        "initial_investment",
        type=float,
        nargs="?",
        help="Initial investment amount",
    )
    parser.add_argument(
        "annual_cash_flow",
        type=float,
        nargs="?",
        help="Expected annual cash flow",
    )
    parser.add_argument(
        "years",
        type=int,
        nargs="?",
        default=1,
        help="Number of years to calculate ROI over",
    )
    args = parser.parse_args()

    if args.initial_investment is None:
        args.initial_investment = float(input("Initial investment: "))
    if args.annual_cash_flow is None:
        args.annual_cash_flow = float(input("Annual cash flow: "))

    net_profit = args.annual_cash_flow * args.years - args.initial_investment
    roi = calculate_roi(net_profit, args.initial_investment)
    payback = calculate_payback_period(args.initial_investment, args.annual_cash_flow)

    print(f"ROI after {args.years} year(s): {roi:.2f}%")
    print(f"Payback period: {payback:.2f} year(s)")
