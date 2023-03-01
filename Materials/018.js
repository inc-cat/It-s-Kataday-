const passingCars = (A) => {
    let sum = 0,
        arr = [],
        localPassings = 0;
    for (let i = 0; i < A.length; i++) {
        if (A[i] === 0) {
            localPassings++;
        } else {
            arr[arr.length] = localPassings;
            localPassings = 0;
        }
    }

    for (let i = arr.length, j = 0; i > 0; i--, j++) {
        sum += i * arr[j];
        if (sum > 2000000000) return -1;
    }
    return sum;
};

module.exports = passingCars;
