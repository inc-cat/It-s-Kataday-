function getAverages(arr) {
    if (arr.length === 0) {
        return null;
    }

    let sum = 0;
    let numbers = 0;

    for (let set of arr) {
        numbers += set.length;
        for (let nums of set) {
            sum += nums;
        }
    }

    return Number((sum / numbers).toFixed(2));
}

module.exports = getAverages;
