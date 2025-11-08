def find_indixes(lst, item):
    indices = []
    for index, value in enumerate(lst):
        if value == item:
            indices.append([index])
        elif isinstance(value, list):
            #for sub_index in value:
            for i in find_indixes(value, item):
                indices.append([index] + i)
    return indices

example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(find_indixes(example, 2))  # [ [0, [1]], [0, 1], 1 ]
print(find_indixes(example, [1, 2, 3]))  # [ [0], 1 ] 