class NumberCalculator {
    constructor(...numbers) {
        this.nums = [...numbers];
    }

    generate() {
        const numberSum = Math.ceil(
            this.nums.reduce(function (accumulator, currentValue) {
                return accumulator + currentValue;
            }, 0) / this.nums[this.nums.length - 1]
        );

        this.nums.push(numberSum);

        return this;
    }

    getMidpoint() {
        this.nums.sort(function (a, b) {
            return a - b;
        });
        let midPoint =
            this.nums.length % 2 === 0
                ? this.nums[this.nums.length / 2 - 1]
                : this.nums[Math.floor(this.nums.length / 2)];

        return midPoint;
    }

    getUniqueFactors() {
        let factors = {};
        for (let num of this.nums) {
            for (let i = 1; i <= num; i++) {
                if (num % i == 0) {
                    factors[i] ? factors[i]++ : (factors[i] = 1);
                }
            }
        }
        return Object.keys(factors)
            .filter(function (factor) {
                return factors[factor] === 1;
            })
            .map(function (string) {
                return Number(string);
            });
    }
}

module.exports = NumberCalculator;
