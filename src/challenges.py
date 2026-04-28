from __future__ import annotations
import heapq


def order_festival_alerts(alerts):
    heap = []

    # put everything into heap
    for alert in alerts:
        priority = alert[0]
        title = alert[1]
        heapq.heappush(heap, (priority, title))

    result = []

    # take out one by one
    while len(heap) > 0:
        item = heapq.heappop(heap)
        result.append(item[1])

    return result


def order_festival_alerts_stable(alerts):
    heap = []
    index = 0

    # adding index so order stays same if priority same
    for alert in alerts:
        priority = alert[0]
        title = alert[1]
        heapq.heappush(heap, (priority, index, title))
        index += 1

    result = []

    while len(heap) > 0:
        item = heapq.heappop(heap)
        result.append(item[2])

    return result


def top_k_festival_alerts(alerts, k):
    if k <= 0:
        return []

    heap = []

    for alert in alerts:
        heapq.heappush(heap, alert)

    result = []
    count = 0

    while len(heap) > 0 and count < k:
        item = heapq.heappop(heap)
        result.append(item[1])
        count += 1

    return result


def peek_next_festival_alert(alerts):
    if len(alerts) == 0:
        return None

    # copy list so original not touched
    temp = list(alerts)
    heapq.heapify(temp)

    item = heapq.heappop(temp)
    return item[1]