# It's Kataday!

A series of katas I have done for programming exercise, ranging in diffculty in the JavaScript and Python languages (though more languages may be added as I continue to expand).

-   These katas have been sourced from various locations which will be shown with each individual kata information.
-   Previously completed katas may be updated as my skills increase over time and as I find better ways to implement solutions.
-   I want my code to be universally understandable, so I won't be playing code golf.
-   If you want to suggest a kata for me to do, please feel free to post an issue and I will consider it.
-   All katas have been completed with test driven development (TTD).

# Katas

## 001: 100 Doors:

There are 100 doors in a row that are all initially closed. You make 100 passes by the doors. The first time through, visit every door and 'toggle' the door (if the door is closed, open it; if it is open, close it).The second time, only visit every 2nd door (i.e., door #2, #4, #6, ...) and toggle it. The third time, visit every 3rd door (i.e., door #3, #6, #9, ...), etc., until you only visit the 100th door. \
Implement a function to determine the state of the doors after the last pass. Return the final result in an array, with only the door numbers included in the array if they are open. \
[![freecodecamp]][freecodecamp-url]

[freecodecamp-url]: https://www.freecodecamp.org/learn/coding-interview-prep/rosetta-code/100-doors
[freecodecamp]: https://img.shields.io/badge/Source-freecodecamp.org-navy?style=for-the-badge&logo=freecodecamp

## 002: Are these Numbers Co-Prime?

In maths, a prime number is a number that is only divisible by itself and 1 (e.g. 13 is only divisible by 13 and 1).
Co-Primes are 2 numbers such that their only common divisor is 1. For example, 9 and 20 are co-prime, no divisors (1, 2, 3, 4, 5, 9, 10 and 20) go perfectly into the other except 1. Notice that neither 9 or 20 are prime themselves. This means that the numbers we choose don't have to be prime for them to be co-prime. But it does help if one number is prime. 100 and 756 on the other hand aren't co-prime because 2 divides both with no remainder (100/2 = 50, 756/2 = 378).
But, 100 and 111 are co-prime because 100 is divisible only by 1, 2, 4, 5, 10, 20, 25, 50 and 100 whereas 111 is only divisible by 1, 3, 37, and 111. Thus, the only 2 numbers in both lists that are a factor of both 100 and 111 is 1. Hence, 100 and 111 are co-prime.

### Task:

Write a function that will return true if provided numbers are co-prime and false if they aren't. \
[![anon]][anon-url]

[anon-url]: https://www.google.com/
[anon]: https://img.shields.io/badge/Source-Anon-red?style=for-the-badge

## 003: Difference to Next Fibonacci Number

The Fibonacci sequence is the set of numbers that you get when you add the two previous numbers in the sequence you get your next number. This sequence starts of with the numbers 0 & 1, giving us the following sequence:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

This is the Fibonacci sequence that we all know and love.

### Task:

Find the difference between that number and the first Fibonacci number greater than our given number.

For example, given a number, 10, we want our function to return 3. This is because 13 is the first Fibonacci number that is greater than 10, thus 13 - 10 = 3.

If the given number is a Fibonacci number, return 0; \
[![anon]][anon-url]

## 004: Update Inventory

Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. Update the current existing inventory item quantities (in `arr1`). If an item cannot be found, add the new item and quantity into the inventory array. The returned inventory array should be in alphabetical order by item. \
[![freecodecamp]][freecodecamp2-url]

[freecodecamp2-url]: https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/inventory-update

## 005: Reverse Capitalisation

Create a function that takes a string and reverses each letter into its upper or lower case counterpart.

E.g. \
`Hello WORLD` becomes `hELLO world`. \
[![anon]][anon-url]

## 006: Decrypt the Message

In this challenge, a secret message has been encrypted by shifting the letters forward or back in the alphabet to different locations.

All the letters experience the same shift, for example if the shift is `+4` then `a` becomes `e`, `b` becomes `f`, `c` becomes `g`, etc...

Any letters at the end, such as z, will continue from the start of the alphabet: `w` becomes `a`, `x` becomes `b`, `y`, becomes `c`, `z` becomes `d`.

If the shift happens in the opposite direction, the start of the alphabet will shift to the end of the alphabet.

### Task:

Given a jumbled string and a number representing the total shift, determine what the original message was before the encryption happened. \
[![anon]][anon-url]

## 007: Are these 2 Objects Identical?

Sometimes, it is worth while to know if 2 pieces of data are identical. Now, this is easy with primitive values because you can just compare them with the "===" operator.

However, if you try to do this with objects and array, it won't work because the memory references of the objects could be different... Even if the contents are exactly the same.

### Task:

Create a function that allows us to compare 2 objects and will determine if the contents are an exact match \
[![anon]][anon-url]

## 008: Prevent Mutations for nested Arrays and Objects

In the Functional Programming, avoiding mutation is a critically important task.

If you do have even one function that mutates data, unwittingly, your entire code base is susceptible to a near impossible bug to resolve.

### Task:

Create a function that prevents mutation for nested arrays and objects. \
[![anon]][anon-url]

## 009: Object Filter

Create a function objFilter, that takes an object and a predicate and returns only the key-value pairs in a new object that pass the predicate test.

e.g.

`const obj = {1: 1, 2: 2, 3: 3, 4: 4}`

`const divisibleBy2 = objFilter(obj, function (value) {
        return value % 2 === 0;
    })` becomes `{2: 2, 4: 4};` \
 [![anon]][anon-url]

## 010: Count Data

Sometimes, we need to know metadata about our information as the total quantity of info can be overwhelming or won't give us a good trend to go off of for analysis.

Here, we're going to attempt to analyse our objects and investigate what types of data they will be using.

We want to make sure it works for nested objects, too!

### Task:

Build a function that receives an object and returns an object sharing the quantity of data types inside of it. It must work for nested objects.

e.g. `countData({1:[2,3,4]})` will output `{array: 1, number: 3, object: 1}` for JavaScript and `{list: 1, dict: 1 int: 3}` for Python. \
 [![anon]][anon-url]

## 011: Create a Stack Class

Create a Stack class.

A stack is a way of storing data. It is only open at one end and can only have items added or removed, one at a time, from that end. Like stacking bowls on top of each other.

Your stack will need:

-   A push() method
-   A pop() method
-   An isEmpty() method
-   An isFull() method
-   A peek() method
-   A clear() method
-   An autoFill() method

[![anon]][anon-url]
