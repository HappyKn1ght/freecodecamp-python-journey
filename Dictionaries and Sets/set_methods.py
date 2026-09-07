my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(f"issubset: {your_set.issubset(my_set)}")
print(f"issuperset: {my_set.issuperset(your_set)}")
print(f"isdisjoint: {my_set.isdisjoint(your_set)}")
print(f"union: {my_set | your_set}")
print(f"intersection: {my_set & your_set}")
print(f"difference: {my_set - your_set}")
print(f"symmetric_difference: {my_set ^ your_set}")