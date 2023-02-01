function updateInventory(arr1, arr2) {
    let arr3 = arr1.map(function (arr) {
        return arr.slice();
    });

    const itemsOnly = arr3.map(function (array) {
        return array[1];
    });

    arr2.forEach(function (element) {
        if (itemsOnly.includes(element[1])) {
            itemIndex = itemsOnly.indexOf(element[1]);
            arr3[itemIndex][0] += element[0];
        } else {
            arr3.push([Number(element[0]), String(element[1])]);
        }
    });
    arr3 = arr3.sort(function (a, b) {
        if (a[1] < b[1]) {
            return -1;
        } else if (a[1] === b[1]) {
            return 0;
        } else {
            return 1;
        }
    });

    return arr3;
}

module.exports = updateInventory;
