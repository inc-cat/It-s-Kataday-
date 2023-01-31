const isCoPrime = (...args) => {
    if (gcdNumbers(...args) !== 1) {
        return false
    }
    return true
}
const gcdTwoNumbers = function (x, y) {
    while (y) {
        let t = y;
        y = x % y;
        x = t;
    }
    return x;
}

const gcdNumbers = function (...args) {
    let [gcd, ...rest] = args
    for (const n of rest) {
        gcd = gcdTwoNumbers(gcd, n)
    }
    return gcd
}

module.exports = isCoPrime;