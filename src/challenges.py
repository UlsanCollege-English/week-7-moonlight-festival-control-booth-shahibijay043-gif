"""Weekly Coding — Festival Alert Priority Center."""

from __future__ import annotations

import heapq


def order_festival_alerts(
    alerts: list[tuple[int, str]],
) -> list[str]:

    priority_heap: list[tuple[int, str]] = []

    for priority, title in alerts:
        heapq.heappush(priority_heap, (priority, title))

    ordered_alerts: list[str] = []

    while priority_heap:
        _, title = heapq.heappop(priority_heap)
        ordered_alerts.append(title)

    return ordered_alerts


def order_festival_alerts_stable(
    alerts: list[tuple[int, str]],
) -> list[str]:

    priority_heap: list[tuple[int, int, str]] = []

    for insertion_order, (priority, title) in enumerate(alerts):
        heapq.heappush(
            priority_heap,
            (priority, insertion_order, title),
        )

    ordered_alerts: list[str] = []

    while priority_heap:
        _, _, title = heapq.heappop(priority_heap)
        ordered_alerts.append(title)

    return ordered_alerts


def top_k_festival_alerts(
    alerts: list[tuple[int, str]],
    k: int,
) -> list[str]:

    if k <= 0 or not alerts:
        return []

    priority_heap: list[tuple[int, int, str]] = []

    for insertion_order, (priority, title) in enumerate(alerts):
        heapq.heappush(
            priority_heap,
            (priority, insertion_order, title),
        )

    top_alerts: list[str] = []

    while priority_heap and len(top_alerts) < k:
        _, _, title = heapq.heappop(priority_heap)
        top_alerts.append(title)

    return top_alerts


def peek_next_festival_alert(
    alerts: list[tuple[int, str]],
) -> str | None:

    if not alerts:
        return None

    _, title = min(alerts)

    return title