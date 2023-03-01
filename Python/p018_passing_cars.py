def passing_cars(road):
    passes = 0
    cars = 0

    for eastWest in road:
        if eastWest == 0:
            passes += 1
        elif eastWest == 1:
            cars += passes

    return cars
