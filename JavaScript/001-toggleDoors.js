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
        let initial = Array(n + 1).fill(0).map((_, i) => i * index)
        initial.shift()
        let shiftDown = initial.map(function (index) {
            return index - 1
        }).filter(function (int) {
            return int <= n
        })


        for (doorChange of shiftDown) {
            doors[doorChange]++
        }
    }
    return doors.map(function (v, i) {
        if (v % 2 == 1) {
            return i + 1
        }
    }).filter(Boolean)
}

console.log(toggleDoors(336))

module.exports = toggleDoors;