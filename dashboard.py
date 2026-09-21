"""Final integration point - displays the results produced by calculator.py.

Added on the feature-dashboard branch: render_dashboard() builds an aligned,
titled summary instead of a loose series of print() calls, and the header now
greets the logged-in user through profile.get_display_name().
"""

from calculator import total, subtraction, multiplication, div
from profile import get_display_name

WIDTH = 49


def format_row(label, value):
    """Return one aligned 'label : value' row for the dashboard body."""
    if value is None:
        value = "unavailable"
    return "| {:<28}{:>16} |".format(label, value)


def render_dashboard():
    """Return the whole dashboard as a single printable string."""
    lines = [
        "*" * WIDTH,
        "|{:^{w}}|".format("DASHBOARD", w=WIDTH - 2),
        "|{:^{w}}|".format("Signed in as " + get_display_name(), w=WIDTH - 2),
        "*" * WIDTH,
        format_row("Result of addition", total),
        format_row("Result of subtraction", subtraction),
        format_row("Result of multiplication", multiplication),
        format_row("Result of division", div),
        "*" * WIDTH,
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    print(render_dashboard())
