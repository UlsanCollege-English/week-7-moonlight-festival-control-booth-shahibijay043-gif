import heapq

def order_festival_alerts(alerts):
    heap = []

    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    result = []

    while heap:
        p, t = heapq.heappop(heap)
        result.append(t)

    return result