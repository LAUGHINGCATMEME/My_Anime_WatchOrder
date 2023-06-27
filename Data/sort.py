import json

def compare_names(name1, name2, comparisons):
    global tpe
    """Compares two names and returns True if name1 should come before name2 in the sorted list."""
    pair = tuple(sorted([name1, name2]))
    if pair in comparisons:
        response = comparisons[pair]
    else:
        while True:
            response = input(f"Which {tpe} should come first: {name1} or {name2}? (Enter 1 or 2): ")
            if response in ['1', '2']: break; else: print("Invalid input. Please enter either 1 or 2.")
        comparisons[pair] = response
    return response == '1'


def merge(left, right, comparisons):
    """Merges two sorted lists based on the comparison results."""
    merged = []
    while left and right:
        if compare_names(left[0], right[0], comparisons): merged.append(left.pop(0)); else: merged.append(right.pop(0))
    merged.extend(left)
    merged.extend(right)
    return merged


def merge_sort(name_list, comparisons):
    """Sorts the list of names using the Merge Sort algorithm."""
    if len(name_list) <= 1: return name_list
    mid = len(name_list) // 2
    left = merge_sort(name_list[:mid], comparisons)
    right = merge_sort(name_list[mid:], comparisons)
    return merge(left, right, comparisons)


def sort_anime():
    global tpe
    tpe = "anime"
    with open("anime.txt", "r") as nig:
        sort_list_str = str(nig.read()).split("Watch List:")[0].split("\n")[:-2]
        sort_list = []
        for i in sort_list_str:
            if i.endswith(" "): i = i[:-1:]
            sort_list.append(i)
        comparisons = {}
        sorted_names = merge_sort(sort_list, comparisons)

        print("\nSorted list of names:")
        for name in sorted_names:
            print(name)
        exit()


def filter_lines(input_string):
    lines = input_string.split('\n')
    filtered_lines = []

    for line in lines:
        if line.strip() == '' or line.strip().startswith('-'): continue
        filtered_lines.append(line)

    filtered_string = '\n'.join(filtered_lines)
    return filtered_string


def sort_characters():
    global tpe
    tpe = "characters"
    with open("characters.txt", "r") as nig:
        sort_list_str = str(nig.read())
        sort_list_str = filter_lines(sort_list_str).split("\n")
        sort_list = []
        for i in sort_list_str:
            if i.endswith(" "): i = i[:-1:]
            sort_list.append(i)
        comparisons = {}
        sorted_names = merge_sort(sort_list, comparisons)

        print("\nSorted list of names:")
        for name in sorted_names:
            print(name)
        exit()


# Added an empty string for not watched.
tpe = ""
sort_anime()
#sort_characters()

"""
sort_list = []
comparisons = {}
sorted_names = merge_sort(sort_list, comparisons)

print("\nSorted list of names:")
for name in sorted_names:
    print(name)
"""
