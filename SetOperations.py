set1 = {1, 2, 3, 4} 
set2= {3, 4, 5, 6}
union_set = set1.union(set2)
print("Union using union() method:", union_set)
union_set_operator = set1 | set2
print("Union using | operator:", union_set_operator)
intersection_set = set1.intersection(set2)
print("Intersection using intersection() method:",intersection_set)
intersection_set_operator = set1 & set2
print("Intersection using & operator:", intersection_set_operator)
difference_set = set1.difference(set2)
print("Difference using difference() method (set1 - set2):", difference_set)
difference_set_operator = set1 - set2
print("Difference using - operator (set1 - set2):", difference_set_operator)
