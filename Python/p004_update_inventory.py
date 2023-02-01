import copy

def update_inventory(items_1, items_2):
    items_clear = copy.deepcopy(items_1)
    items_only = [i[1] for i in items_clear]

    for current_item in items_2:
        if current_item[1] in items_only:
            item_index = items_only.index(current_item[1])
            items_clear[item_index][0] += current_item[0]
        else:
            if isinstance(current_item[0], int):
                push_input = int(current_item[0])
            else:
                push_input = float(current_item[0])
            items_clear.append([push_input p, str(current_item[1])])

    items_clear.sort(key=lambda x: x[1])

    return items_clear

