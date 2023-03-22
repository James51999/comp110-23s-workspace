"""Example function for unit tests"""

def sum(xs: list[float]) -> float:
    """Return sum off all elements in xs."""
    sum_total: float = 0.0

    for x in range(0,len(xs)):
        sum_total += xs[x]
    return sum_total
