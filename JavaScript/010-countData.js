function countData(object) {
    let newObj = {};
    let amounts = {
        number: 0,
        string: 0,
        boolean: 0,
        array: 0,
        object: 0,
        function: 0,
    };

    switch (typeof object) {
        case "number":
            amounts.number++;
            break;
        case "string":
            amounts.string++;
            break;
        case "boolean":
            amounts.boolean++;
            break;
        case "function":
            amounts.function++;
            break;
        case "object":
            let counts;
            if (Array.isArray(object)) {
                amounts.array++;
                counts = [
                    ...object.map(function (arrayElement) {
                        return countData(arrayElement);
                    }),
                ];
            } else {
                amounts.object++;
                counts = [];
                for (keyCycle of Object.keys(object)) {
                    counts.push(countData(object[keyCycle]));
                }
            }
            amounts.number = counts
                .map(function (a) {
                    return a.number;
                })
                .reduce(function (acc, a) {
                    return acc + a;
                }, 0);

            amounts.string = counts
                .map(function (a) {
                    return a.string;
                })
                .reduce(function (acc, a) {
                    return acc + a;
                }, 0);

            amounts.boolean = counts
                .map(function (a) {
                    return a.boolean;
                })
                .reduce(function (acc, a) {
                    return acc + a;
                }, 0);

            amounts.function = counts
                .map(function (a) {
                    return a.function;
                })
                .reduce(function (acc, a) {
                    return acc + a;
                }, 0);

            amounts.array += counts
                .map(function (a) {
                    return a.array;
                })
                .reduce(function (acc, a) {
                    return acc + a;
                }, 0);

            amounts.object += counts
                .map(function (a) {
                    return a.object;
                })
                .reduce(function (acc, a) {
                    return acc + a;
                }, 0);
    }

    return amounts;
}

module.exports = countData;

console.log(
    countData({
        1: 1,
        2: true,
        3: "no",
        4: 4,
        5: function () {},
        6: {},
        7: [],
        8: {},
        9: [],
        10: "ludwig",
    })
);
