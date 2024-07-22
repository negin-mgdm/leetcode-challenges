/*
You are given an array of strings names, and an array heights that consists of distinct positive integers.
Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

Example 1:
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

Example 2:
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

Constraints:
n == names.length == heights.length
1 <= n <= 103
1 <= names[i].length <= 20
1 <= heights[i] <= 105
names[i] consists of lower and upper case English letters.
All the values of heights are distinct.
*/

/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function (names, heights) {
    // Create an array of objects where each object contains a name and its corresponding height.
    let people = names.map((name, index) => ({ name: name, height: heights[index] }));

    // Sort the array of objects based on the heights in descending order.
    people.sort((a, b) => b.height - a.height);

    // Extract the sorted names from the array of objects
    let sortedNames = people.map(person => person.name);

    return sortedNames;
};

let names = ["Alice", "Bob", "Bob"];
let heights = [155, 185, 150];
console.log(sortPeople(names, heights));



/**
 * @param {string[]} names1
 * @param {number[]} heights1
 * @return {string[]}
 */
var sortPeople1 = function (names1, heights1) {
    for (let i = 0; i < names1.length; i++) {
        for (let j = 0; j < heights1.length - 1; j++) {
            if (heights1[j] < heights1[j + 1]) {
                [heights1[j + 1], heights1[j]] = [heights1[j], heights1[j + 1]];
                [names1[j + 1], names1[j]] = [names1[j], names1[j + 1]];
            }
        }
    }
    return names1;
};

let names1 = ["Mary", "John", "Emma"];
let heights1 = [180, 165, 170];
console.log(sortPeople1(names1, heights1));
