def count_data(obj):
    amounts = {
        "int": 0,
        "float": 0,
        "str": 0,
        "bool": 0,
        "list": 0,
        "dict": 0,
        "function": 0,
    }

    element_type = str(type(obj)).split("'")[1]

    amounts[element_type] += 1

    if element_type == "dict":
        for i in obj.values():
            obj_data = count_data(i)
            for cycle in obj_data:
                if obj_data[cycle] == 1:
                    amounts[cycle] += 1

    elif element_type == "list":
        for i in obj:
            list_data = count_data(i)
            for cycle in list_data:
                if list_data[cycle] == 1:
                    amounts[cycle] += 1

    return amounts

print(count_data({
            1: 1,
            2: [1, 2, 3, { 1: True, 2: count_data, 3: [1, 2, 3] }],
            3: "hi",
            4: { 1: True, 2: False, 3: ["string", "is", "not", { 1: "here" }] },
            5: count_data,
            6: [
                {
                    1: [[[3, 4, 5, "hi", "northcoders", ["Edd!"]]]],
                    2: "something here"
                },
            ],
        }))