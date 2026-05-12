from __future__ import annotations

import heapq


def order_festival_alerts(
    alerts: list[tuple[int, str]],
) -> list[str]:

    heap: list[tuple[int, str]] = []

    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    result: list[str] = []

    while heap:
        _, title = heapq.heappop(heap)
        result.append(title)

    return result


def order_festival_alerts_stable(
    alerts: list[tuple[int, str]],
) -> list[str]:

    heap: list[tuple[int, int, str]] = []

    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    result: list[str] = []

    while heap:
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def top_k_festival_alerts(
    alerts: list[tuple[int, str]],
    k: int,
) -> list[str]:

    if k <= 0 or not alerts:
        return []

    heap: list[tuple[int, int, str]] = []

    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    result: list[str] = []

    while heap and len(result) < k:
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def peek_next_festival_alert(
    alerts: list[tuple[int, str]],
) -> str | None:

    if not alerts:
        return None

    priority, title = min(alerts)

    return title