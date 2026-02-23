"""
Minions Scheduler Python SDK

Schedules, cron triggers, and timed execution definitions
"""

__version__ = "0.1.0"


def create_client(**kwargs):
    """Create a client for Minions Scheduler.

    Args:
        **kwargs: Configuration options.

    Returns:
        dict: Client configuration.
    """
    return {
        "version": __version__,
        **kwargs,
    }

from .schemas import *
