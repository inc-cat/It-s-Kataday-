function preventMutation(object) {
    let newObj = {};

    switch (typeof object) {
        case "number":
            return Number(object);
        case "string":
            return String(object);
        case "boolean":
            return Boolean(object);
        case "object":
            if (Array.isArray(object)) {
                return [
                    ...object.map(function (arrayElement) {
                        return preventMutation(arrayElement);
                    }),
                ];
            }
            for (keyCycle of Object.keys(object)) {
                newObj[keyCycle] = preventMutation(object[keyCycle]);
            }
    }

    return newObj;
}

module.exports = preventMutation;
