class Node {
    constructor(value) {
        this.value = value;
        this.larger = null;
        this.smaller = null;
    }

    getNode() {
        return {
            value: this.value,
            larger: this.larger,
            smaller: this.smaller,
        };
    }

    insertNode(value) {
        if (value === this.value || isNaN(value)) {
            throw new Error("Unable to insert value");
        }
        let highOrLow = value > this.value ? "larger" : "smaller";
        if (this[highOrLow] == null) {
            this[highOrLow] = new Node(value);
        } else {
            this[highOrLow].insertNode(value);
        }
    }

    contains(value) {
        if (isNaN(value)) {
            return;
        }

        if (value === this.value) {
            return true;
        }

        let highOrLow = value > this.value ? "larger" : "smaller";
        if (this[highOrLow] == null) {
            return false;
        } else {
            return this[highOrLow].contains(value);
        }
    }
}

class BST extends Node {}

module.exports = { Node, BST };
