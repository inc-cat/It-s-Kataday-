function objFilter(obj, method) {
    let newObj = {};
    for (let key in obj) {
        let entry = method(obj[key]);
        if (entry) {
            newObj[key] = obj[key];
        }
    }
    return newObj;
}

module.exports = objFilter;
