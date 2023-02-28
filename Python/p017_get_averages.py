def get_averages(number_list):
    if len(number_list) == 0:
        return None

    total = 0
    numbers = 0

    for set in number_list:
        numbers += len(set)

        for nums in set:
            total += nums

    return round(total / numbers, 2)
