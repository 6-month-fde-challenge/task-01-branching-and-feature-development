"""Derive the profile name from the login details.

profile_name is initialised to an empty string first. Previously it was only
assigned inside the `if` block, so blank input left the name undefined and every
module importing it failed.

Added on the feature-profile branch: the profile is now gated by
login.is_authenticated() and exposes get_display_name() for the dashboard.
"""

from login import user_name, pass_word, is_authenticated

profile_name = ""

if is_authenticated(user_name, pass_word):
    profile_name = user_name


def get_display_name():
    """Return a human friendly name for the dashboard header."""
    if not profile_name:
        return "Guest"
    return profile_name.replace("_", " ").replace(".", " ").title()
