list = list(range(1, 11))
print("Original list: ", list)

sorted_list = sorted(list)[:5]
print(f"Extracted first five elements: {sorted_list}")

reversed_list = sorted_list.reverse()
print(f"Reversed extracted elements: {sorted_list}")