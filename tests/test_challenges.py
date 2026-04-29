from __future__ import annotations
import heapq


def order_festival_alerts(alerts):
    heap = []

    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    result = []
    while heap:
        priority, title = heapq.heappop(heap)
        result.append(title)

    return result


def order_festival_alerts_stable(alerts):
    heap = []

    # add index to maintain order when priorities are same
    for i, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, i, title))

    result = []
    while heap:
        priority, i, title = heapq.heappop(heap)
        result.append(title)

    return result


def top_k_festival_alerts(alerts, k):
    if k <= 0 or not alerts:
        return []

    heap = []

    for i, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, i, title))

    result = []
    while heap and len(result) < k:
        priority, i, title = heapq.heappop(heap)
        result.append(title)

    return result


def peek_next_festival_alert(alerts):
    if not alerts:
        return None

    # return smallest priority without changing original list
    return min(alerts, key=lambda x: x[0])[1]