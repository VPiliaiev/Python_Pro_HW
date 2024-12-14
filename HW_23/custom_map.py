def custom_map(data, func1, func2):
    return {func1(key): func2(value) for key, value in data.items()}


my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}


def funk1(k):
    return k + k


def funk2(v):
    return v * v


result = custom_map(my_dict, funk1, funk2)
print(result)
