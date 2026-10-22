
import math


def calculate_revenue(quantity, unit_price):
    """Calculate gross item revenue after validating the inputs."""

    if quantity is None or unit_price is None:
        raise TypeError("Quantity and unit price are required.")

    if (
        isinstance(quantity, bool)
        or isinstance(unit_price, bool)
        or not isinstance(quantity, (int, float))
        or not isinstance(unit_price, (int, float))
    ):
        raise TypeError("Quantity and unit price must be numbers.")

    if not math.isfinite(quantity) or not math.isfinite(unit_price):
        raise ValueError("Inputs must be finite numbers.")

    if quantity < 0 or unit_price < 0:
        raise ValueError("Quantity and unit price cannot be negative.")

    return quantity * unit_price


if __name__ == "__main__":
    revenue = calculate_revenue(4, 25.00)
    print(f"Gross item revenue: GHS {revenue:.2f}")
