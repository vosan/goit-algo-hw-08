import heapq


def min_cost_to_connect_cables(lengths) -> float:
    """
    Calculate the minimum cost to connect all cables.

    :param lengths: List of cable lengths, all of which must be non-negative.
    :return: Minimum cost to connect all cables.
    """
    arr = [float(x) for x in lengths]
    if any(x < 0 for x in arr):
        raise ValueError("lengths must be non-negative")
    if len(arr) <= 1:
        return 0.0
    heapq.heapify(arr)
    total = 0.0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        c = a + b
        total += c
        heapq.heappush(arr, c)
    return total


print(min_cost_to_connect_cables([]))  # 0.0
print(min_cost_to_connect_cables([5]))  # 0.0
print(min_cost_to_connect_cables([1, 2]))  # 3.0
print(min_cost_to_connect_cables([1, 2, 3]))  # 9.0
print(min_cost_to_connect_cables([1, 2, 3, 4]))  # 19.0
print(min_cost_to_connect_cables([8, 4, 6, 12]))  # 58.0
print(min_cost_to_connect_cables([0.5, 1.5, 2.0]))  # 6.0
print(min_cost_to_connect_cables([0, 0, 0]))  # 0.0
print(min_cost_to_connect_cables([5, 5, 5, 5]))  # 40.0
