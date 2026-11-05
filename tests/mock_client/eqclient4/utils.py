import math


def eq_heading(x1: float, y1: float, x2: float, y2: float) -> int:
    """0-512 heading, the same quadrants the server uses for IsFacingMob."""
    x_diff = abs(x1 - x2)
    y_diff = abs(y1 - y2) or 1e-9
    angle = math.atan2(x_diff, y_diff) * 180.0 * 0.3183099014828645
    if y1 >= y2:
        degrees = (90.0 - angle + 90.0) if x2 >= x1 else (angle + 180.0)
    elif y1 > y2 or x2 > x1:
        degrees = angle
    else:
        degrees = 90.0 - angle + 270.0
    return int(degrees * 511.5 * 0.0027777778) & 0xFFF
