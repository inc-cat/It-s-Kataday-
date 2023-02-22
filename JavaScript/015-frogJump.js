function calculateJumps(a, b, d) {
    const numbers = [a, b].sort(function (a, b) {
        return b - a;
    });

    console.log(numbers);

    return Math.abs(Math.ceil((numbers[0] - numbers[1]) / d));
}

module.exports = calculateJumps;
