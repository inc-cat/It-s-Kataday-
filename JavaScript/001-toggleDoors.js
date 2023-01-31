const toggleDoors = (n) => {
    // exit early in simple cases
    if (n === 0) {
        return []
    }
    else if (n === 1) {
        return [1]
    }

    // array to represent open doors as 1st cycle will open all doors
    const doors = Array(n).fill(1)


    for (index = 2; index <= n; index++) {
        let initial = Array(Math.floor(n / index)).fill(0).map((_, i) => (i + 1) * index - 1)

        for (doorChange of initial) {
            doors[doorChange]++
        }
    }
    return doors.map(function (v, i) {
        if (v % 2 == 1) {
            return i + 1
        }
    }).filter(Boolean)
}

module.exports = toggleDoors;