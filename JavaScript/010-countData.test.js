const countData = require("./010-countData");

describe("Count the Data Types in an Object", () => {
    test("Returns an empty object when the input object is empty", () => {
        expect(countData({})).toEqual({
            number: 0,
            string: 0,
            boolean: 0,
            array: 0,
            object: 1,
            function: 0,
        });
    });

    test("Returns an object with the relevant type equal to 1, when only 1 key-value pair exists in the object", () => {
        expect(countData({ 1: "hi" })).toEqual({
            number: 0,
            string: 1,
            boolean: 0,
            array: 0,
            object: 1,
            function: 0,
        });
        expect(countData({ 1: 1 })).toEqual({
            number: 1,
            string: 0,
            boolean: 0,
            array: 0,
            object: 1,
            function: 0,
        });
        expect(countData({ 1: true })).toEqual({
            number: 0,
            string: 0,
            boolean: 1,
            array: 0,
            object: 1,
            function: 0,
        });
        expect(countData({ 1: [] })).toEqual({
            number: 0,
            string: 0,
            boolean: 0,
            array: 1,
            object: 1,
            function: 0,
        });
        expect(countData({ 1: {} })).toEqual({
            number: 0,
            string: 0,
            boolean: 0,
            array: 0,
            object: 2,
            function: 0,
        });
        expect(countData({ 1: function () {} })).toEqual({
            number: 0,
            string: 0,
            boolean: 0,
            array: 0,
            object: 1,
            function: 1,
        });
    });

    test("Returns an object with the relevant type incremented as necessary for a single type object", () => {
        expect(countData({ 1: "hi", 2: "no", 3: "yes" })).toEqual({
            number: 0,
            string: 3,
            boolean: 0,
            array: 0,
            object: 1,
            function: 0,
        });
        expect(countData({ 1: 1, 2: 2 })).toEqual({
            number: 2,
            string: 0,
            boolean: 0,
            array: 0,
            object: 1,
            function: 0,
        });
        expect(
            countData({
                1: true,
                2: true,
                3: true,
            })
        ).toEqual({
            number: 0,
            string: 0,
            boolean: 3,
            array: 0,
            object: 1,
            function: 0,
        });
        expect(countData({ 1: [], 2: [], 3: [], 4: [] })).toEqual({
            number: 0,
            string: 0,
            boolean: 0,
            array: 4,
            object: 1,
            function: 0,
        });
        expect(countData({ 1: {}, 2: {}, 3: {} })).toEqual({
            number: 0,
            string: 0,
            boolean: 0,
            array: 0,
            object: 4,
            function: 0,
        });
        expect(
            countData({
                1: function () {},
                2: function () {},
                3: function () {},
                4: function () {},
            })
        ).toEqual({
            number: 0,
            string: 0,
            boolean: 0,
            array: 0,
            object: 1,
            function: 4,
        });
    });

    test("Returns an object with the relevent types incremented in a mixed object", () => {
        expect(
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
        ).toEqual({
            number: 2,
            string: 2,
            boolean: 1,
            array: 2,
            object: 3,
            function: 1,
        });
    });

    test("Returns an object with the relevent types incremented in a nested object", () => {
        const ob = {
            1: 1,
            2: [1, 2, 3],
            3: "hi",
            4: { 1: true, 2: false, 3: [] },
            5: function () {},
            6: [function () {}, function () {}, {}],
        };

        expect(countData(ob)).toEqual({
            string: 1,
            number: 4,
            boolean: 2,
            array: 3,
            object: 3,
            function: 3,
        });
    });

    test("Returns the correct value for each data type in a deeply nested object", () => {
        const ob = {
            1: 1,
            2: [1, 2, 3, { 1: true, 2: function () {}, 3: [1, 2, 3] }],
            3: "hi",
            4: { 1: true, 2: false, 3: ["string", "is", "not", { 1: "here" }] },
            5: function () {},
            6: [
                function () {},
                function () {},
                {
                    1: [[[3, 4, 5, "hi", "northcoders", ["Edd!"]]]],
                    2: "something here",
                    3: function () {},
                },
            ],
        };
        expect(countData(ob)).toEqual({
            string: 9,
            number: 10,
            boolean: 3,
            array: 8,
            object: 5,
            function: 5,
        });
    });

    test("Original object is not mutated in the process of running function", () => {
        const ob = { 1: 1, 2: "hit", 3: true, 4: [] };
        countData(ob);
        expect(ob).toEqual({ 1: 1, 2: "hit", 3: true, 4: [] });
    });

    test("Returns a new object when function is invoked", () => {
        const ob = { 1: 1, 2: "hit", 3: true, 4: [] };
        expect(countData(ob)).not.toBe(ob);
    });
});
