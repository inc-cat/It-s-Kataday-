function areIdentical(obj1, obj2) {
    if (typeof obj1 !== typeof obj2) {
        return false;
    }

    if (!(obj1 instanceof Object)) {
        return obj1 === obj2;
    }

    const keys = [...Object.keys(obj1), ...Object.keys(obj2)];
    for (let key of keys) {
        if (!areIdentical(obj1[key], obj2[key])) {
            return false;
        }
    }
    return true;
}

module.exports = areIdentical;
