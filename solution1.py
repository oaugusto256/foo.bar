def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


def solution(data, n):
    # Your code here
    dictionary = {}

    if n == 0:
        return []

    for value in data:
        if (dictionary.get(value) == None):
            dictionary[value] = 1
        else:
            dictionary[value] = dictionary[value] + 1

    values_to_be_removed = []

    for value in dictionary:
        if (dictionary[value] > n):
            values_to_be_removed.append(value)

    list_to_be_cleaned = data

    for value in values_to_be_removed:
        list_to_be_cleaned = remove_values_from_list(list_to_be_cleaned, value)

    return list_to_be_cleaned


solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
