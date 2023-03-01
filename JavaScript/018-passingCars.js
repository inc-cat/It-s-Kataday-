const passingCars = (road) => {
    let passes = 0;
    let cars = 0;

    for (eastWest of road) {
        if (eastWest === 0) {
            passes++;
        } else if (eastWest === 1) {
            cars += passes;
        }
    }

    return cars;
};

module.exports = passingCars;
