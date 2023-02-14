const { Shape, Cube, Sphere, Dodecahedron } = require("./012-shapes");

describe("Shapes and the use of inheritance", () => {
    describe("Shape Class", () => {
        test("Shape class has a constructor, but throws an error when it is used", () => {
            expect(() => new Shape()).toThrow(
                "Cannot instantiate abstract class!"
            );
        });
    });

    describe("Cube Class", () => {
        test("Cube class overwrites the getVolume() method and returns the correct volume of the object, to 3 decimal places", () => {
            const cube = new Cube(10, 100);
            const cube2 = new Cube(17.2, 50);
            expect(() => cube.getVolume()).not.toThrow(
                "Abstract method must be overwritten by subclass!"
            );
            expect(cube.getVolume()).toBe(1000);
            expect(+cube2.getVolume()).toBe(5088.448);
        });

        test("Cube object overwrites the getSurfaceArea() method and returns the correct surface area of the object, to 3 decimal places", () => {
            const cube = new Cube(10, 100);
            const cube2 = new Cube(25.21, 2000);
            expect(() => cube.getSurfaceArea()).not.toThrow(
                "Abstract method must be overwritten by subclass!"
            );
            expect(cube.getSurfaceArea()).toBe(600);
            expect(cube2.getSurfaceArea()).toBe(3813.265);
        });

        test("Cube class overwrites the getDensity() method and returns the correct density of the object, to 3 decimal places", () => {
            const cube = new Cube(10, 100);
            const cube2 = new Cube(14, 10000);
            expect(() => cube.getDensity()).not.toThrow(
                "Abstract method must be overwritten by subclass!"
            );
            expect(cube.getDensity()).toBe(0.1);
            expect(cube2.getDensity()).toBe(3.644);
        });
    });

    describe("Sphere Class", () => {
        test("Cube class overwrites the getVolume() method and returns the correct volume of the object, to 3 decimal places", () => {
            const sphere = new Sphere(5, 10);
            const sphere2 = new Sphere(16.3, 20);
            expect(() => sphere.getVolume()).not.toThrow(
                "Abstract method must be overwritten by subclass!"
            );
            expect(sphere.getVolume()).toBe(523.599);
            expect(sphere2.getVolume()).toBe(18140.591);
        });

        test("Sphere object overwrites the getSurfaceArea() method and returns the correct surface area of the object, to 3 decimal places", () => {
            const sphere = new Sphere(5, 10);
            const sphere2 = new Sphere(13, 301);
            expect(() => sphere.getSurfaceArea()).not.toThrow(
                "Abstract method must be overwritten by subclass!"
            );
            expect(sphere.getSurfaceArea()).toBe(314.159);
            expect(sphere2.getSurfaceArea()).toBe(2123.717);
        });

        test("Sphere class overwrites the getDensity() method and returns the correct density of the object, to 3 decimal places", () => {
            const sphere = new Sphere(5, 10);
            const sphere2 = new Sphere(16.3, 19001);
            expect(() => sphere.getDensity()).not.toThrow(
                "Abstract method must be overwritten by subclass!"
            );
            expect(sphere.getDensity()).toBe(0.019);
            expect(sphere2.getDensity()).toBe(1.047);
        });
    });
});
