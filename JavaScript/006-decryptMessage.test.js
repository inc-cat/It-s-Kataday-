const decryptMessage = require("./006-decryptMessage");

describe("Decrypt the Message", () => {
    test("Returns the same string when the message is not encrypted", () => {
        expect(decryptMessage("", 0)).toBe("");
        expect(decryptMessage("hello", 0)).toBe("hello");
    });

    test("Returns the decrypted message when the shift is negative", () => {
        expect(decryptMessage("dpejoh", -1)).toBe("coding");
        expect(decryptMessage("rdxyjwntzx", -5)).toBe("mysterious");
    });

    test("Returns the decrypted message when the shift is positive", () => {
        expect(decryptMessage("q", 10)).toBe("a");
        expect(decryptMessage("qjgbc", 2)).toBe("slide");
    });

    test("Returns the decrypted message if there is capitalisation - result should be in the correct case", () => {
        expect(decryptMessage("XKYARZ JUKY TKKJ ZU HK OT AVVKXIGYK", -6)).toBe(
            "RESULT DOES NEED TO BE IN UPPERCASE"
        );
        expect(decryptMessage("SCRiX GfJk", 9)).toBe("BLArG PoSt");
    });

    test("Returns the decrypted message if there is capitalisation and an abnormal shift number", () => {
        expect(decryptMessage("mabl bl t oxkr vktsr mxlm...", -253)).toBe(
            "this is a very crazy test..."
        );
        expect(decryptMessage("Jul ner jr qbvat guvf?", 1027)).toBe(
            "Why are we doing this?"
        );
    });
});
