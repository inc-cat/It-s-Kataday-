class Stack {
    constructor(max = 10) {
        this.max = max;
        this.storage = [];
    }

    push(inp) {
        if (this.storage.length < this.max) {
            this.storage.push(inp);
        }
    }

    pop() {
        if (this.storage.length > 0) {
            return this.storage.pop();
        }
    }

    isEmpty() {
        return this.storage.length === 0 ? true : false;
    }

    isFull() {
        return this.storage.length === this.max ? true : false;
    }

    peek() {
        return this.storage[this.storage.length - 1];
    }

    clear() {
        this.storage = [];
    }

    autoFill(inp) {
        if (this.storage.length === this.max) {
            return;
        }

        for (let i = this.storage.length; i < this.max; i++) {
            this.storage.push(inp);
        }
    }

    show() {
        let showStack = {};
        for (
            let stackNumber = 1;
            stackNumber < this.storage.length + 1;
            stackNumber++
        ) {
            showStack[stackNumber] = this.storage[stackNumber - 1];
        }

        return showStack;
    }
}

module.exports = Stack;
