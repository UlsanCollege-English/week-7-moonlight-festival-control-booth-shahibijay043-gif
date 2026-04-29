import heapq


def order_festival_alerts(alerts):
    # create empty heap
    heap = []

    # push all alerts into heap
    for alert in alerts:
        priority, title = alert
        heapq.heappush(heap, (priority, title))

    result = []

    # pop from heap (smallest priority first)
    while heap:
        priority, title = heapq.heappop(heap)
        result.append(title)

    return result


def total_attendees(attendees):
    total = 0

    for num in attendees:
        total += num

    return total


def average_attendees(attendees):
    if len(attendees) == 0:
        return 0

    total = total_attendees(attendees)
    return total / len(attendees)