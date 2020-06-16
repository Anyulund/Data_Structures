A = [5, 10, 15, 20]
B = [3, 7, 13, 60]

# C now equals [3, 5, 7, 10, 13, 15, 20, 60]


def mergeLists(sorted_list_a, sorted_list_b):
    merged_list = []
    while len(sorted_list_a) > 0 and len(sorted_list_b) > 0:
        if sorted_list_a [0] < sorted_list_b[0]:
            merged_list.append(sorted_list_a.pop(0))
        else:
            merged_list.append(sorted_list_b.pop(0))
    if len(sorted_list_b) > 0:
        merged_list += sorted_list_b
    if len(sorted_list_a) > 0:
        merged_list += sorted_list_a
    return merged_list

C = mergeLists(A, B)
print(C)
