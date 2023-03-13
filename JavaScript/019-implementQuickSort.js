function implementQuickSort(arrOriginal) {
    let arr = [...arrOriginal];

    let hi = arr.length - 1;

    function quicksort(arr, lo, hi) {
        // Ensure indices are in correct order
        if (lo >= hi || lo < 0) {
            return;
        }

        // Partition array and get the pivot index
        let p = partition(arr, lo, hi);

        // Sort the two partitions
        console.log(p);
        quicksort(arr, lo, p - 1); // Left side of pivot
        quicksort(arr, p + 1, hi); // Right side of pivot
    }
    // Divides array into two partitions
    function partition(arr, lo, hi) {
        let pivot = arr[hi]; // Choose the last element as the pivot

        // Temporary pivot index
        let i = lo - 1;

        for (let j = lo; j <= hi - 1; j++) {
            // If the current element is less than or equal to the pivot
            if (arr[j] <= pivot) {
                // Move the temporary pivot index forward
                i++;
                // Swap the current element with the element at the temporary pivot index
                swap(arr, i, j);
            }
        }
        // Move the pivot element to the correct pivot position (between the smaller and larger elements)
        i++;
        swap(arr, i, hi);
        return i;
    }

    function swap(array, one, two) {
        const swap2 = array[two];
        const swap1 = array[one];
        array[one] = swap2;
        array[two] = swap1;

        return array;
    }

    quicksort(arr, 0, hi);
    return arr;
}

module.exports = implementQuickSort;
