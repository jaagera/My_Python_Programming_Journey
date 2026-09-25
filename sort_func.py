# Assuming l1 was previously defined, e.g., l1 = [10, 50, 20]
l1.append(45)
print(l1)  # Output example: [10, 50, 20, 45]

# To add element to list in sorted manner
from sortedcontainers import SortedList

l3 = SortedList(l1)
l3.add(45)
print(l3)  # Output example: SortedList([10, 20, 45, 45, 50])
