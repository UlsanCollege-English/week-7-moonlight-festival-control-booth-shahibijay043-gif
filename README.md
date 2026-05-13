[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-HC-VniT)
Summary

In this assignment, I practiced working with priority queues and heaps in Python using the heapq module.
I implemented functions to order festival alerts by priority, preserve insertion order for equal priorities, retrieve the top k alerts, and peek at the next upcoming alert.
This project helped me improve my understanding of heap operations, priority-based processing, and efficient data handling.
I also learned how to carefully manage edge cases while keeping the code clean, readable, and well-documented.

Approach
order_festival_alerts
I used a min-heap to process alerts from the smallest priority value to the largest.
order_festival_alerts_stable
I added an insertion index to preserve the original order when priorities were equal.
top_k_festival_alerts
I used a heap and removed only the first k highest-priority alerts.
peek_next_festival_alert
I used min() to quickly find the next alert without modifying the original list.
Complexity reasoning
Function	Time Complexity	Why
order_festival_alerts	O(n log n)	Each heap insertion and removal takes logarithmic time
order_festival_alerts_stable	O(n log n)	Heap operations are performed for all alerts
top_k_festival_alerts	O(n log n)	Building and removing from the heap requires logarithmic operations
peek_next_festival_alert	O(n)	min() scans the list once to find the smallest priority
Edge-case checklist
 empty alert list
 single alert
 multiple alerts
 duplicate priorities
 stable ordering with equal priorities
 k = 0
 k larger than number of alerts
 negative priority values
 peek on empty list
 peek on populated list


Assistance / Sources
online site of python course

Person / tool / website:
Help received:
Helped improve code readability, formatting, documentation, and complexity explanations.

Person / tool / website:
Python Documentation

Help received:
Used to review heapq functions and heap behavior in Python.