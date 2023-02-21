def obj_filter(object, method):
    new_object = {}
    for iteration in object.keys():
        if method(object[iteration]):
            new_object[iteration] = object[iteration]

    return new_object
