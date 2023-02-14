class Shape {
    constructor(m, kg) {
        if (this.constructor === Shape) {
            throw new Error("Cannot instantiate abstract class!");
        }

        this.m = m;
        this.kg = kg;
    }

    getVolume() {
        throw new Error("Abstract method must be overwritten by subclass!");
    }

    getSurfaceArea() {
        throw new Error("Abstract method must be overwritten by subclass!");
    }

    getDensity() {
        throw new Error("Abstract method must be overwritten by subclass!");
    }
}

class Sphere extends Shape {
    constructor(m, kg) {
        super(m, kg);
    }

    getVolume() {
        return Number(((4 * Math.PI * Math.pow(this.m, 3)) / 3).toFixed(3));
    }

    getSurfaceArea() {
        return Number((4 * Math.PI * Math.pow(this.m, 2)).toFixed(3));
    }

    getDensity() {
        return Number((this.kg / this.getVolume()).toFixed(3));
    }
}

class Cube extends Shape {
    constructor(m, kg) {
        super(m, kg);
    }

    getVolume() {
        return Number(Math.pow(this.m, 3).toFixed(3));
    }

    getSurfaceArea() {
        return Number((6 * Math.pow(this.m, 2)).toFixed(3));
    }

    getDensity() {
        return Number((this.kg / this.getVolume()).toFixed(3));
    }
}

module.exports = { Shape, Sphere, Cube };
