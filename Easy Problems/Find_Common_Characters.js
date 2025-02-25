/*
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
*/

/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function (words) {
    let commonChars = [];

    for (let char of words[0]) {
        let isCommonChar = true;
        for (let i = 1; i < words.length; i++) {
            if (!words[i].includes(char)) {
                isCommonChar = false;
                break;
            }

            words[i] = words[i].replace(char, '');
        }
        if (isCommonChar) {
            commonChars.push(char);
        }
    }

    return commonChars;
};

let words = ["bella", "label", "roller"];
console.log(commonChars(words)); 