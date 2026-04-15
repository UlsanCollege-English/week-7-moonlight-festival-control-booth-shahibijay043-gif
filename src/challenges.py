"""
Week 7: Moonlight Festival Control Booth

Use Python's heapq module to solve priority queue problems.
"""

from __future__ import annotations

import heapq


def order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles in the order they should be handled.

    Each alert is a tuple:
        (priority, title)

    Smaller priority numbers should be handled first.
    """
    raise NotImplementedError


def order_festival_alerts_stable(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles in the order they should be handled.

    If two alerts have the same priority, keep the original input order.
    """
    raise NotImplementedError


def top_k_festival_alerts(alerts: list[tuple[int, str]], k: int) -> list[str]:
    """
    Return the titles of the k most urgent alerts.

    If k <= 0, return an empty list.
    If k is larger than the number of alerts, return as many as possible.
    """
    raise NotImplementedError


def peek_next_festival_alert(alerts: list[tuple[int, str]]) -> str | None:
    """
    Return the title of the next alert to handle without permanently
    changing the original input.

    If alerts is empty, return None.
    """
    raise NotImplementedError
