l1 = [1, 2]
l2 = ["a", "b"]

a = [(i, x) for i in l1 for x in l2]
print(a)