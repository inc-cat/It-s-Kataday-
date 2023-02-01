function diffToFib(num) {
    let values = [0, 1]

    do {
        let newValue = values.slice(-2).reduce(function (input, added) {
            return input + added;
        });

        if (newValue >= num) {
            return newValue - num
        }

        values.push(newValue)
    }
    while (true)
}

module.exports = diffToFib