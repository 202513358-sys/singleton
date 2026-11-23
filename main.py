from singleton import Counter

a = Counter.get_instance()
b = Counter.get_instance()

print("같은 객체?", a is b)
print("변경 전 b.count:", b.count)

a.count += 1

print("변경 후 b.count:", b.count)
