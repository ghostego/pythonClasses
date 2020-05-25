my_list = ["Junior", "Sybil", "Cornelius", "Marlo", "Mojo Jojo", "Hastur"]
iterable_list = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(iterable_list)
    print(next_item)