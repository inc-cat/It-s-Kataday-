const reverseCapitalisation = (str) => {
    const rev = str.split("").map(function (char) {
        if (
            "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM".includes(
                char
            )
        ) {
            if (char.toUpperCase() === char) {
                return char.toLowerCase();
            } else {
                return char.toUpperCase();
            }
        } else {
            return char;
        }
    });
    return rev.join("");
};

module.exports = reverseCapitalisation;
