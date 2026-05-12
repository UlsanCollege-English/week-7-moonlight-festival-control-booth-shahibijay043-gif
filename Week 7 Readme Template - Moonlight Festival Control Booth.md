# Week 7 Homework: Moonlight Festival Control Booth

## Summary

This homework uses Python heaps with the `heapq` module to manage festival alerts by priority.  
The program sorts alerts from highest priority to lowest priority number.  
It also keeps alerts stable when priorities are equal, returns only the top `k` alerts, and allows checking the next alert without removing it.  
This assignment helped practice priority queues, heaps, and edge-case handling.

---

## Approach

### `order_festival_alerts`

I created a heap and pushed every alert into it using `heapq.heappush()`.  
Each heap item stored `(priority, title)`.  
Since heaps automatically keep the smallest value first, lower priority numbers were removed first.  
I repeatedly popped items from the heap and added their titles to the result list.

### `order_festival_alerts_stable`

To handle ties correctly, I added the original index to the heap item.  
Each item looked like `(priority, index, title)`.  
The index preserved the original order when two alerts had the same priority.  
This was important because alerts with equal priority should stay in the same order they arrived.

### `top_k_festival_alerts`

I used a heap to sort alerts by priority and only removed the first `k` items.  
If `k` was `0` or negative, the function returned an empty list.  
If `k` was larger than the number of alerts, the function returned all available alerts.

### `peek_next_festival_alert`

I used `min()` to find the alert with the smallest priority number.  
This allowed me to check the next alert without removing or changing the original input list.

---

## Complexity

### `order_festival_alerts`

* **Time:** O(n log n)
* **Space:** O(n)
* **Why:** Every alert is inserted and removed from the heap once.

### `order_festival_alerts_stable`

* **Time:** O(n log n)
* **Space:** O(n)
* **Why:** The heap stores all alerts with their indexes and processes each one once.

### `top_k_festival_alerts`

* **Time:** O(n log n)
* **Space:** O(n)
* **Why:** Alerts are added into the heap and up to `k` alerts are removed.

### `peek_next_festival_alert`

* **Time:** O(n)
* **Space:** O(1)
* **Why:** `min()` checks the list once and does not create another large structure.

---

## Edge-case checklist

### `order_festival_alerts`

* [x] empty input
* [x] one alert
* [x] multiple different priorities

### `order_festival_alerts_stable`

* [x] same-priority tie
* [x] all same priority
* [x] empty input

### `top_k_festival_alerts`

* [x] `k = 0`
* [x] `k > len(alerts)`
* [x] duplicate priorities
* [x] empty input

### `peek_next_festival_alert`

* [x] empty input
* [x] normal case

---

## Test notes

* Tested empty lists to avoid crashes.
* Tested same-priority alerts to confirm stable ordering.
* Tested large and small values of `k`.

---

## Assistance & Sources

### AI used?

* [ ] No
* [x] Yes

If yes, what did it help with?

AI helped review heap logic, edge cases, and formatting.

### Other sources

* Python documentation
* Class lecture notes

---

## Reflection

What was hardest?

* Understanding how heaps automatically sort items and how to preserve order during ties.

What do you understand better now?

* I understand heaps, priority queues, stable ordering, and how heapq works in Python.
