const decryptMessage = (message, shift) => {
    const realisticShift = shift % 26;
    const letters = "abcdefghijklmnopqrstuvwxyz";
    const shiftedMessage = message.split("").map(function (char) {
        if (letters.indexOf(char.toLowerCase()) === -1) {
            return char;
        }
        const charIndex =
            (letters.indexOf(char.toLowerCase()) + 26 + realisticShift) % 26;
        const capitalise = char.toUpperCase() === char;

        if (capitalise) {
            return letters[charIndex].toUpperCase();
        } else {
            return letters[charIndex];
        }
    });

    return shiftedMessage.join("");
};

module.exports = decryptMessage;
