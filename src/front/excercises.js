//   Reverse Integer

// const { elementType } = require("prop-types");

// Solution
// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

// Example 1:

// Input: x = 123
// Output: 321
// Example 2:

// Input: x = -123
// Output: -321
// Example 3:

// Input: x = 120
// Output: 21

// Constraints:

// -231 <= x <= 231 - 1

// #------------------------------------------------------------------------------------------------------------------------------

// function reverseString(num) {
//   const maxRange = Math.pow(2, 31) - 1;
//   const minRange = -Math.pow(2, 31);
//   console.log("Input number:", num);
//   console.log("Max Range:", maxRange);
//   console.log("Min Range:", minRange);

//   const sign =  num < 0 ? -1 : 1;
//   const positiveValue = Math.abs(num)
//   const reverseStr = String(positiveValue).split("").reverse().join("");
//   const converToInt =  sign * parseInt(reverseStr,10);

//   if( converToInt < minRange || converToInt > maxRange){
//     return 0
//   }

//   return converToInt

// }
// console.log(reverseString(-120));

//
// # 🔥 CHALLENGING PYTHON EXERCISE: Data Type Mastery
// # 🧩 Problem: Deep Data Type Analysis Tool
// # You're given a complex nested structure that contains different Python data types: dictionaries, lists, tuples, sets, and strings. Your task is to write a function called analyze_structure(data) that performs the following:

// # ✅ Required Output:
// # Return a dictionary with:

// # 'total_elements': total number of all elements (including nested ones)

// # 'data_types': a dictionary with counts of each data type found ('str', 'int', 'float', 'list', 'dict', 'set', 'tuple', etc.)

// # 'unique_values': the number of unique values across the entire structure (including deeply nested values)

// # 'most_common_type': the type that appears most frequently

// # Handle cycles (e.g., if an object references itself), and avoid infinite recursion.

// # 🧪 Example Input:
// # python
// # Copy
// # Edit
// # sample_data = {
// #     'user1': {
// #         'name': 'Alice',
// #         'scores': [10, 20, 30],
// #         'tags': {'python', 'developer'},
// #     },
// #     'user2': {
// #         'name': 'Bob',
// #         'scores': [25, 20.5, 30],
// #         'tags': ('python', 'mentor'),
// #     },
// #     'misc': [None, True, {'notes': ['good', 'bad']}]
// # }
// # 💡 Output Example:
// # python
// # Copy
// # Edit
// # {
// #     'total_elements': 20,
// #     'data_types': {
// #         'str': 7,
// #         'int': 4,
// #         'float': 1,
// #         'list': 3,
// #         'dict': 5,
// #         'set': 1,
// #         'tuple': 1,
// #         'NoneType': 1,
// #         'bool': 1
// #     },
// #     'unique_values': 15,
// #     'most_common_type': 'str'
// # }
// # ⚠️ Constraints
// # You must recursively explore nested structures.

// # Use the type() function and collections.Counter.

// # Do not mutate the original data.

// # You may need to convert unhashable types when tracking unique values.

// function countingElements(data) {
//   let counter = 0;
//   for (let element of Object.values(data)) {
//     if (typeof element === "object" && element !== null) {
//       if (Array.isArray(element)) {
//         for (let subElement of element) {
//           if (typeof subElement === "boolean" || subElement === null) {
//             counter += 1;
//           }
//           if (typeof subElement === "object" && subElement !== null) {
//             for (let item of Object.values(subElement)) {
//               for (let subItem of item) {
//                 counter += 1;
//               }
//             }
//           }
//         }
//       } else if (!Array.isArray(!element)) {
//         for (let item of Object.values(element)) {
//           if (typeof item === "string") {
//             counter += 1;
//           } else if (Array.isArray(item)) {
//             for (let subItem of item) {
//               counter += 1;
//             }
//           } else if (item instanceof Set) {
//             for (let subItem of item) {
//               counter += 1;
//             }
//           }
//         }
//       }
//     }
//   }
//   return counter;
// }

// const sample_data = {
//   user1: {
//     name: "Alice",
//     scores: [10, 20, 30],
//     tags: new Set(["python", "developer"]), // ✅ Converted Python set
//   },
//   user2: {
//     name: "Bob",
//     scores: [25, 20.5, 30],
//     tags: ["python", "mentor"], // ✅ Converted Python tuple to array
//   },
//   misc: [null, true, { notes: ["good", "bad"] }], // ✅ None → null, True → true
// };

// console.log(countingElements(sample_data), " ---> !!COUNTING!!!");

// // #===============================================================================================================================

// 🧠 Exercise: Event Conflict Resolver
// You are organizing a conference. Each speaker submits a list of time slots when they're available.

// You must find all pairs of speakers who have at least one overlapping time slot, and then resolve the conflict by printing:

// The speaker names

// The overlapping slot(s)

// A decision:

// If both have 2 or more available slots → assign next available non-overlapping time to one.

// If only one has 2+ slots → assign a new time to the one with more slots.

// If both have only 1 slot → log as "Unresolvable Conflict."

// 🔢 Input example:
// python
// Copy
// Edit
// # Python dict example
// speakers = {
//     "Alice": ["10:00", "11:00", "14:00"],
//     "Bob": ["11:00", "13:00"],
//     "Charlie": ["10:00"],
//     "Diana": ["14:00", "15:00"]
// }
// js
// Copy
// Edit
// // JS object equivalent
// const speakers = {
//     Alice: ["10:00", "11:00", "14:00"],
//     Bob: ["11:00", "13:00"],
//     Charlie: ["10:00"],
//     Diana: ["14:00", "15:00"]
// };
// 🧩 Expected Output (example):
// pgsql
// Copy
// Edit
// Alice & Bob have conflict at: 11:00 ➜ Assign Bob to 13:00
// Alice & Charlie have conflict at: 10:00 ➜ Unresolvable Conflict
// Alice & Diana have conflict at: 14:00 ➜ Assign Diana to 15:00
// 🎯 Your Task
// Compare each unique speaker pair (no repeat pairs).

// Check for overlapping time slots.

// Based on how many total slots each speaker has, resolve or label as unresolvable.

// Print the decision clearly.

// function conference(speakersObj) {
//   const namesOfSpeakers = Object.keys(speakersObj);
//   for (let i = 0; i < namesOfSpeakers.length; i++) {
//     for (let j = i + 1; j < namesOfSpeakers.length; j++) {
//       let namesOfSpeakers1 = namesOfSpeakers[i];
//       let namesOfSpeakers2 = namesOfSpeakers[j];

//       let available1 = speakersObj[namesOfSpeakers1];
//       let available2 = speakersObj[namesOfSpeakers2];

//       let common = available1.filter(time => available2.includes(time));

//       if (common.length > 0) {
//         let selected = common[0];
//         console.log(
//           `${namesOfSpeakers1} and ${namesOfSpeakers2} can meet at ${selected}`
//         );
//       } else {
//         console.log(
//           `${namesOfSpeakers1} and ${namesOfSpeakers2} have no coomon time`
//         );
//       }
//     }
//   }
// }

// // JS object equivalent
// const speakers = {
//   Alice: ["10:00", "11:00", "14:00"],
//   Bob: ["11:00", "13:00"],
//   Charlie: ["10:00"],
//   Diana: ["14:00", "15:00"],
// };
// conference(speakers)

// #===============================================================================================================================
//   Delete Node in a Linked List

// Solution
// There is a singly-linked list head and we want to delete a node node in it.

// You are given the node to be deleted node. You will not be given access to the first node of head.

// All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

// Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

// The value of the given node should not exist in the linked list.
// The number of nodes in the linked list should decrease by one.
// All the values before node should be in the same order.
// All the values after node should be in the same order.
// Custom testing:

// For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
// We will build the linked list and pass the node to your function.
// The output will be the entire list after calling your function.

// Example 1:

// Input: head = [4,5,1,9], node = 5
// Output: [4,1,9]
// Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
// Example 2:

// Input: head = [4,5,1,9], node = 1
// Output: [4,5,9]
// Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

// Constraints:

// The number of the nodes in the given list is in the range [2, 1000].
// -1000 <= Node.val <= 1000
// The value of each node in the list is unique.
// The node to be deleted is in the list and is not a tail node.
// JavaScript
// 1
// /**
// 2
//  * Definition for singly-linked list.
// 3
//  * function ListNode(val) {
// 4
//  *     this.val = val;
// 5
//  *     this.next = null;
// 6
//  * }
// 7
//  */
// 8
// /**
// 9
//  * @param {ListNode} node
// 10
//  * @return {void} Do not return anything, modify node in-place instead.
// 11
//  */
// 12
// var deleteNode = function(node) {
// 13

// 14
// };

// function removeNode(node){
//   node.val = node.next.val;
// }
// head = [4, 5, 1, 9], node = 5

// #===============================================================================================================================

// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

// //  Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// // Output: [[7,4,1],[8,5,2],[9,6,3]]
// Constraints:

// n == matrix.length == matrix[i].length
// 1 <= n <= 20
// -1000 <= matrix[i][j] <= 1000

// #------------------------------------------------------------------------------------------------------------------------------
// function rotateImage(matrix) {
//   for (let i = 0; i < matrix.length; i++) {
//     for (let j = i + 1; j < matrix[0].length; j++) {
//       let temp = matrix[i][j];
//       matrix[i][j] = matrix[j][i];
//       matrix[j][i] = temp;
//     }
//   }
//   console.log("!First loop!! -- ", matrix);
//   for (let i = 0; i < matrix.length; i++) {
//     let left = 0;
//     let right = matrix[i].length - 1;

//     while (left < right) {
//       let temp = matrix[i][left];
//       matrix[i][left] = matrix[i][right];
//       matrix[i][right] = temp;
//       left++;
//       right--;
//     }
//   }
//   console.log("!!Second loop!! -- ",matrix);
// }

// m = [
//   [5, 1, 9, 11],
//   [2, 4, 8, 10],
//   [13, 3, 6, 7],
//   [15, 14, 12, 16],
// ];
// rotateImage(m);

// // #===============================================================================================================================
// 🚨 HARD EXERCISE 1: Deep Variable Behavior
// ✅ Problem Description (in both languages)
// You're given a list of employees. Each employee has a name and a list of skills. You must:

// Clone the original list

// Modify one of the inner lists (skills)

// Prove whether your clone is deep or shallow

// Show how variable declarations or object references affect the result
// 🟨 JavaScript Version (Advanced let, const, mutability, clone behavior)
// // ➕ Bonus: Try cloning with .map() + spread operator and then JSON.parse(JSON.stringify(...)) — compare the two.
// 🟦 Expected Concepts Tested:
// const does not make objects immutable

// Shallow copy vs deep copy

// Object references

// Variable declaration ≠ content lock

// #------------------------------------------------------------------------------------------------------------------------------
// function mutatesElement(element){
//   const shallowCopy = element.slice();
//   const deepClone = JSON.parse(JSON.stringify(element))
//   shallowCopy[1]["skills"] = ["aaa","aaaaaa"]
//   deepClone[1]["skills"] = ["aaa","bbbbbb"]
//   console.log("original --", element);
//   console.log("!!shallow copy --",shallowCopy);
//   console.log("!!Deep Copy copy --",deepClone);

// }
// const employees = [
//   { name: "Alice", skills: ["JS", "Python"] },
//   { name: "Bob", skills: ["HTML", "CSS"] }
// ];
// mutatesElement(employees)

// #===============================================================================================================================

//   Longest Common Prefix

// Solution
// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

// Constraints:

// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters if it is non-empty.

// function findPrefix(string) {
//   let prefix = "";
//   let firstWord = string[0];

//   for (let i = 0; i < firstWord.length; i++) {
//     let char = firstWord[i];

//     for (let j = 1; j < string.length; j++) {
//       if (string[j][i] !== char) {
//         return prefix;
//       }
//     }
//     prefix += char;
//   }
//   return prefix;
// }

// strs = ["dog", "racecar", "car"];
// findPrefix(strs);
// console.log(findPrefix(["flower", "flow", "flight"])); // "fl"
// console.log(findPrefix(["dog", "racecar", "car"])); // ""
// console.log(findPrefix(["interview", "interrupt", "integrate", "integral"])); // "int"

// #===============================================================================================================================

// # 🚨 HARD EXERCISE 2: Nested Data Transformation by Type

// ## ✅ Problem Description (in both languages)

// You're given a **deeply nested data structure** (a mix of lists/arrays, dictionaries/objects, strings, numbers, and booleans).

// Your task:

// 1. Traverse the entire structure (deep traversal)
// 2. For each value:
//     - If it's a **string**, convert to uppercase
//     - If it's a **number**, multiply by 10
//     - If it's a **boolean**, flip it
//     - Leave anything else untouched
// 3. Return a **new structure** (don't mutate the original)
// 4. Must support **nested structures of any depth**

// #------------------------------------------------------------------------------------------------------------------------------
// //first solution:
// function dataTypes(obj) {
//   const newObj = {};
//   for (let element in obj) {
//     const value = obj[element];
//     console.log("!!VALUE!! --", value);

//     // 1. Primitive at top-level
//     if (typeof value == "string") {
//       newObj[element] = value.toUpperCase();
//     }

//     // 2. Array at top-level (like "skills")
//     else if (Array.isArray(value)) {
//       const newArray = [];
//       for (let subValue of value) {
//         if (typeof subValue == "string") {
//           newArray.push(subValue.toUpperCase());
//         } else if (typeof subValue == "number") {
//           newArray.push(subValue * 10);
//         }
//       }
//       newObj[element] = newArray;
//     }

//     // 3. preferences object (handled manually)
//     else if (
//       typeof value == "object" &&
//       value != null &&
//       !Array.isArray(value)
//     ) {
//       const newNestedObj = {};
//       for (let key in value) {
//         const subValue = value[key];
//         if (typeof subValue == "boolean") {
//           newNestedObj[key] = !subValue;
//         } else if (typeof subValue == "number") {
//           newNestedObj[key] = subValue * 10;
//         } else if (typeof subValue === "string") {
//           newNestedObj[key] = subValue.toUpperCase();
//         } else if (Array.isArray(subValue)) {
//           const newArray = [];
//           for (let subValueArray of subValue) {
//             if (typeof subValueArray == "string") {
//               newArray.push(subValueArray.toUpperCase());
//             } else if (typeof subValueArray == "boolean") {
//               newArray.push(!subValueArray);
//             } else if (typeof subValueArray == "number") {
//               newArray.push(subValueArray * 10);
//             }
//           }
//           newNestedObj[key] = newArray;
//         }
//       }
//       newObj[element] = newNestedObj
//     } else if (typeof value == "number") {
//       newObj[element] = value * 10;
//     } else if (typeof value == "boolean") {
//       newObj[element] = !value;
//     } else {
//       newObj[element] = value;
//     }
//   }
//   return newObj;
// }

// const input = {
//   name: "alice",
//   age: 25,
//   active: true,
//   skills: ["js", "python", 3],
//   preferences: {
//     darkMode: false,
//     fontSize: 14,
//     tags: ["code", true, 7],
//   },
// };

// console.log(dataTypes(input));

// Your function should return a transformed object with same structure but changed values based on type.

// #------------------------------------------------------------------------------------------------------------------------------
//Second solution:
// function handleDataTypes(obj) {
//   if (typeof obj === "string") {
//     return obj.toUpperCase();
//   } else if (typeof obj == "number") {
//     return obj * 10;
//   } else if (typeof obj === "boolean") {
//     return !obj;
//   }
//   else if(Array.isArray(obj)){
//     return obj.map(function (item){
//       return handleDataTypes(item);
//     })
//   }
//   else if(typeof obj === "object" && obj != null){
//     const newObj = {}
//     for(let key in obj){
//       newObj[key] = handleDataTypes(obj[key])
//     }
//     return newObj
//   }
// }

// const input = {
//   name: "alice",
//   age: 25,
//   active: true,
//   skills: ["js", "python", 3],
//   preferences: {
//     darkMode: false,
//     fontSize: 14,
//     tags: ["code", true, 7],
//   },
// };

// console.log(handleDataTypes(input));

// #===============================================================================================================================
//   Merge Sorted Array

// Solution
// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

// Merge nums1 and nums2 into a single array sorted in non-decreasing order.

// The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

// Example 1:

// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
// Output: [1,2,2,3,5,6]
// Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
// The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
// Example 2:

// Input: nums1 = [1], m = 1, nums2 = [], n = 0
// Output: [1]
// Explanation: The arrays we are merging are [1] and [].
// The result of the merge is [1].
// Example 3:

// Input: nums1 = [0], m = 0, nums2 = [1], n = 1
// Output: [1]
// Explanation: The arrays we are merging are [] and [1].
// The result of the merge is [1].
// Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

// Constraints:

// nums1.length == m + n
// nums2.length == n
// 0 <= m, n <= 200
// 1 <= m + n <= 200
// -109 <= nums1[i], nums2[j] <= 109

// Follow up: Can you come up with an algorithm that runs in O(m + n) time?

// function merginArrays(nums1, m, nums2, n){
//     let i = m - 1
//     let j = n - 1
//     let k = m + n - 1

//     while (i >= 0 && j >= 0){
//         if(nums1[i] > nums2[j]){
//             nums1[k] = nums1[i];
//             i--;
//         }
//         else{
//             nums1[k] = nums2[j]
//             j--;
//         }
//         k--;
//     }
//     while(j >= 0){
//         nums1[k] = nums2[j];
//         j--;
//         k--;
//     }

// }

// let nums1 = [1, 2, 3, 0, 0, 0];
// let nums2 = [2, 5, 6];
// let m = 3, n = 3;

// merginArrays(nums1, m, nums2, n);
// console.log(nums1);  // ➜ [1, 2, 2, 3, 5, 6]

// #===============================================================================================================================

// ## 🚨 HARD EXERCISE 3: Matrix Word Search

// ### ✅ Problem (Both JavaScript & Python):

// You are given a **2D grid** of characters and a **target word**. Write a function that returns `true` if the word exists in the grid.
//  The word can be constructed from letters of sequentially adjacent cells, where **"adjacent"** cells are those horizontally or vertically neighboring.
// //   The same letter cell may **not** be used more than once.txt
// CopyEdit
// Input:
// grid = [
//   ['A','B','C','E'],
//   ['S','F','C','S'],
//   ['A','D','E','E']
// ]
// word = "ABCCED"

// Output: true

// Explanation: The word is found by going:
// A → B → C → C → E → D
// txt
// CopyEdit
// Input:
// word = "ABCB"

// Output: false (B is reused)

// #------------------------------------------------------------------------------------------------------------------------------
// function findWord(element, word) {
//   function compareLetters(i, j, index) {
//     if (index == word.length) {
//       return true;
//     } else if (
//       i < 0 ||
//       i >= element.length ||
//       j < 0 ||
//       j >= element[i].length ||
//       element[i][j] != word[index]
//     ) {
//       return false;
//     }

//     let temp = element[i][j];
//     element[i][j] = "#";

//     let wordFound =
//       compareLetters(i + 1, j, index + 1) ||
//       compareLetters(i - 1, j, index + 1) ||
//       compareLetters(i, j + 1, index + 1) ||
//       compareLetters(i, j - 1, index + 1);
//     element[i][j] = temp;
//     return wordFound;
//   }

//   for (let i = 0; i < element.length; i++) {
//     for (let j = 0; j < element[i].length; j++) {
//       if (element[i][j] == word[0]) {
//           if (compareLetters(i, j, 0)) return true;
//       }
//     }
//   }
//   return false;
// }

// let grid = [
//   ["A", "B", "C", "E"],
//   ["S", "F", "C", "S"],
//   ["A", "D", "E", "E"],
// ];
// let word = "ABCCED";
// result = findWord(grid, word);
// console.log(result);

// // Output: true

// // Explanation: The word is found by going:
// // A → B → C → C → E → D
// #===============================================================================================================================
// 1) SOLUTION 🟡 Top-Down Memoization (Recursive + Cache)
// let counter = 0;
// function climbStairs(steps){
//     counter++;
//     if(steps in memo) return memo[steps];
//     if (steps === 1) return 1;
//     if( steps === 2) return 2;

//     memo[steps] = climbStairs(steps - 1) + climbStairs(steps - 2);
//     return memo[steps]

// }
// let memo = {};

// stepsN = 3
// console.log(climbStairs(30));
// console.log(counter);
// // console.log(memo)

// #===============================================================================================================================
// 2) SOLUTION 🟢 Tabulation (O(1) space):
// function climbStairs(steps){
//     if (steps === 1) return 1
//     if (steps === 2) return 2

//     let first = 1;
//     let second = 2;
//     let current;

//     for (let i = 3; i <= steps; i++){
//         current = first + second
//         console.log(`Step ${i}: ${first} + ${second} = ${current}`);
//         first = second;
//         second = current
//     }
//     return current

// }
// n = 5
// result = climbStairs(n)
// console.log(result);

// #===============================================================================================================================

// ## 🚨 HARD OOP EXERCISE: **"Digital Library System"**

// ### 📚 Problem Description

// You're going to build a **Digital Library System** that manages books, users, and the process of borrowing/returning books.

// ---

// ### ✅ Requirements (apply to **both JavaScript and Python**):

// ### 1. **Class `Book`**

// - Attributes: `title`, `author`, `genre`, `available` (boolean)
// - Method: `toString()` in JS / `__str__()` in Python — prints book info

// ### 2. **Class `User` (Base Class)**

// - Attributes: `name`, `id`, `borrowedBooks` (or `borrowed_books`)
// - Methods:
//     - `borrow(book)`: Can borrow the book only if available
//     - `returnBook(book)`: Removes book from user's list
//     - `listBooks()`: Lists current borrowed books

// ### 3. **Subclasses**

// - `Student` → inherits from `User`, max 3 books
// - `Professor` → inherits from `User`, max 5 books

// ### 4. **Class `Library`**

// - Attributes:
//     - `books`: list of all books
//     - `users`: list of all users
// - Methods:
//     - `addBook(book)`
//     - `registerUser(user)`
//     - `findBookByTitle(title)`
//     - `showAllBooks()`
//     - `showUsers()`

// ---

// ### ➕ Bonus Challenges (Optional but Advanced)

// - Prevent returning books that weren’t borrowed
// - Track borrow dates and calculate late return penalties
// - Use **composition** for a `LoanManager` helper class
// - Use `static` methods or decorators (Python)

// ---

// class Book {
//   constructor(title, author, genre) {
//     this.title = title;
//     this.author = author;
//     this.genre = genre;
//     this.available = true;
//   }
//   toString() {
//     return `${this.title} by ${this.author} - ${this.genre}`;
//   }
// }

// class User {
//   constructor(name, id) {
//     this.name = name;
//     this.id = id;
//     this.borrowedBooks = [];
//   }
//   borrow(book) {
//     if (book.available) {
//       this.borrowedBooks.push(book);
//       book.available = false;
//       console.log(`${this.name} has borrowed '${book.title}'`);
//     } else {
//       console.log(`'${book.title}' is not available`);
//     }
//   }
//   returnBook(book) {
//     const hasBook = this.borrowedBooks.includes(book);
//     if (hasBook) {
//       const index = this.borrowedBooks.indexOf(book);
//       this.borrowedBooks.splice(index, 1);
//       book.available = true;
//       console.log(`${this.name} has returned '${book.title}'`);
//     } else {
//       console.log(`${this.name} doesn't have '${book.title}' borrowed`);
//     }
//   }
//   toString(){
//    return `${this.name} (ID: ${this.id}) - Borrowed Books: ${this.borrowedBooks.length}`;
//   }
// }

// class Student extends User {
//   borrow(book) {
//     if (this.borrowedBooks.length >= 3) {
//       console.log(`${this.name} has reached the borrowing limit (3 books).`);
//     } else {
//       super.borrow(book);
//     }
//   }
// }

// class Professor extends User {
//   borrow(book) {
//     if (this.borrowedBooks.length >= 5) {
//       console.log(`${this.name} has reached the borrowing limit (3 books).`);
//     } else {
//       super.borrow(book);
//     }
//   }
// }
// class Library {
//   constructor() {
//     this.books = [];
//     this.users = [];
//   }
//   addBook(book) {
//     this.books.push(book);
//     console.log(`'${book.title}' added to the library.`);
//   }
//   registerUser(user) {
//     const alreadyExists = this.users.some((u) => u.id === user.id);
//     if (alreadyExists) {
//       console.log(`User with ID ${user.id} is already registered.`);
//     } else {
//       this.users.push(user);
//       console.log(`'${user.name}' registered successfully.`);
//     }
//   }
//   findBookByTitle(title) {
//     const findBook = this.books.find((b) => b.title == title);
//     if (findBook) {
//       return findBook;
//     } else {
//       console.log(`No book found with title '${title}'`);
//       return null;
//     }
//   }
//   showAllBooks() {
//     if (this.books.length === 0) {
//       console.log("No books available");
//     } else {
//       console.log("Books in the library:");
//       for (let book of this.books) {
//         console.log(` - ${book}`);
//       }
//     }
//   }
//     showAllUsers() {
//     if (this.users.length === 0) {
//       console.log("No users registered");
//     } else {
//       console.log("Users registered:");
//       for (let user of this.users) {
//         console.log(` - ${user}`);
//       }
//     }
//   }
// }

// // 📚 Create some books
// const book1 = new Book("1984", "George Orwell", "Dystopian");
// const book2 = new Book("Clean Code", "Robert C. Martin", "Tech");
// const book3 = new Book("The Hobbit", "J.R.R. Tolkien", "Fantasy");
// const book4 = new Book("Sapiens", "Yuval Noah Harari", "Non-fiction");
// const book5 = new Book("Brave New World", "Aldous Huxley", "Sci-Fi");
// const book6 = new Book("The Alchemist", "Paulo Coelho", "Fiction");

// // 🧑‍🎓 Create users
// const student = new Student("Alice", 101);
// const professor = new Professor("Dr. Smith", 201);

// // 📖 Create the library and register users
// const library = new Library();

// library.registerUser(student);
// library.registerUser(professor);

// // 📘 Add books to the library
// library.addBook(book1);
// library.addBook(book2);
// library.addBook(book3);
// library.addBook(book4);
// library.addBook(book5);
// library.addBook(book6);

// // 👓 Show all books and users
// console.log("\n--- INITIAL STATE ---");
// library.showAllBooks();
// library.showAllUsers();

// // 📥 Student borrows up to the limit
// student.borrow(book1);
// student.borrow(book2);
// student.borrow(book3);
// student.borrow(book4); // ❌ This should fail due to limit

// // 🧪 Show borrowed books
// console.log("\n--- STUDENT BORROWED ---");
// student.borrowedBooks.forEach(b => console.log("Student:", b.toString()));

// // 📥 Professor borrows some books
// professor.borrow(book4); // This was denied to student
// professor.borrow(book5);
// professor.borrow(book6);

// // 🔁 Return a book and retry
// student.returnBook(book2);    // ✔️ Valid return
// student.returnBook(book5);    // ❌ Not borrowed by student

// #===============================================================================================================================

//   Pascal's Triangle

// Solution
// Given an integer numRows, return the first numRows of Pascal's triangle.

// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

// Example 1:

// Input: numRows = 5
// Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
// Example 2:

// Input: numRows = 1
// Output: [[1]]

// Constraints:

// 1 <= numRows <= 30

// function pascalTriangle(rows){
//     const result = [];
//     for(let i = 0; i < rows; i++ ){
//         const row = [];
//         for(let j =0; j <=i; j++){
//             if(j === 0 || j === i){
//                 row.push(1);
//             }
//              else{
//                 const prev = result[i - 1];
//                 row.push(prev[j-1] + prev[j])
//              }
//         }
//         result.push(row)
//     }
//     return result
// }
// let numRows = 5
// console.log(pascalTriangle(numRows));

//===============================================================================================================================
// function generate(numRows){
//     const results = [[1]];
//     for (let i =1; i < numRows; i++){
//         const prev = results[i-1]
//         const row = [1]
//         for(let j=1; j < i; j++){
//             row[j] = prev[j-1] + prev[j]
//         }
//         row.push(1)
//         results.push(row)

//     }
//     return results
// }
// let n = 5
// console.log(generate(n));

//===============================================================================================================================

// function findWords(s, wordDict) {
//   const result = [];
//   const wordSet = new Set(wordDict);

//   function backTrack(start, path) {
//     // Log each recursive call
//     console.log(
//       `🔁 backTrack called with start=${start}, path=[${path.join(" ")}]`
//     );
//     // Base case: reached the end of the string
//     if (start === s.length) {
//       console.log(`✅ Complete sentence found: ${path.join(" ")}`);
//       result.push(path.join(" "));
//       return;
//     }
//     for (let end = start + 1; end <= s.length; end++) {
//       const word = s.slice(start, end);
//       console.log(`🔍 Checking word: '${word}' (from s[${start}:${end}])`);

//       if (wordSet.has(word)) {
//         console.log(
//           `✔ Found valid word: '${word}' — calling backTrack(${end}, [...path, '${word}'])`
//         );
//         backTrack(end, [...path, word]);
//       } else {
//         console.log(`❌ '${word}' is not in wordDict`);
//       }
//     }
//   }
//   backTrack(0, []);

//   return result;
// }

// const s = "catsanddog";
// const wordDict = ["cat", "cats", "and", "sand", "dog"];
// const output = findWords(s, wordDict);

// console.log("\n🎉 Final Result:");
// console.log(output);

//===============================================================================================================================
//   First Bad Version

// Solution
// You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

// Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

// You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

// Example 1:

// Input: n = 5, bad = 4
// Output: 4
// Explanation:
// call isBadVersion(3) -> false
// call isBadVersion(5) -> true
// call isBadVersion(4) -> true
// Then 4 is the first bad version.
// Example 2:

// Input: n = 1, bad = 1
// Output: 1

// Simulate a global bad version value for testing
// let bad = 4;

// function findBadVersion(n) {
//     let left = 1;
//     let right = n;

//     // Simulated API to test if a version is bad
//     function isBadVersion(version) {
//         return version >= bad;
//     }

//     console.log(`Initial range: left = ${left}, right = ${right}`);
//     console.log(`Looking for the first bad version out of ${n} versions...`);
//     console.log(`Bad version is simulated as: ${bad}`);

//     while (left < right) {
//         let mid = Math.floor((left + right) / 2);

//         // Log the current state
//         console.log(`\n🔍 Checking mid = ${mid}`);
//         console.log(`Current range → left = ${left}, right = ${right}`);

//         if (isBadVersion(mid)) {
//             console.log(`❌ Version ${mid} is BAD → Move RIGHT to mid = ${mid}`);
//             right = mid;
//         } else {
//             console.log(`✅ Version ${mid} is GOOD → Move LEFT to mid + 1 = ${mid + 1}`);
//             left = mid + 1;
//         }
//     }

//     console.log(`\n🎯 First bad version found: ${left}`);
//     return left;
// }
// findBadVersion(5);

//===============================================================================================================================

//   Rotate Array

// Solution
// Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

// Example 1:

// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]
// Example 2:

// Input: nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]
// Explanation:
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]

// Constraints:

// 1 <= nums.length <= 105
// -231 <= nums[i] <= 231 - 1
// 0 <= k <= 105

// Follow up:

// Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
// Could you do it in-place with O(1) extra space?
//    Show Hint #1
//    Show Hint #2
//    Show Hint #3

//------------------------------------------------------------------------------------------------------------------------------

// Not in place:
// function rotateArray(nums, k) {
//   const createSlotsArray = new Array(nums.length).fill(0);
//   for (let i = 0; i < nums.length; i++) {
//     const newIndex = (i + k) % nums.length;
//     createSlotsArray[newIndex] = nums[i];
//   }
//   return createSlotsArray;
// }

// let nums = [1, 2, 3, 4, 5, 6, 7];
// let k = 3;
// let result = rotateArray(nums, k);
// console.log(result);

//===============================================================================================================================
//In place
// function rotate(nums,k){
//     k = k % nums.length
//     let count = 0
//     let start = 0

//     while (count < nums.length){
//         let currentIndex = start
//         let prevNumber = nums[start];

//         while(true){
//             let nextIndex = (currentIndex + k) % nums.length;
//             let temp = nums[nextIndex]
//             nums[nextIndex] = prevNumber
//             prevNumber = temp
//             currentIndex = nextIndex
//             count += 1

//             if (currentIndex == start) break;
//         }
//         start += 1
//     }
// }

// let nums = [1, 2, 3, 4, 5, 6, 7];
// let k = 3;
// rotate(nums, k);           // modifies nums in place
// console.log(nums);         // print the updated array

//===============================================================================================================================

// class Account {
//   #balance;
//   constructor(owner, balance) {
//     this.owner = owner;
//     this.#balance = balance;
//   }

//   deposit(amount) {
//     if (amount <= 0) {
//       throw new Error("Deposit amount must be positive.");
//     }
//     this.#balance += amount;
//   }
//   withdraw(amount) {
//     if (amount <= 0) {
//       throw new Error("withdraw amount must be positive.");
//     }
//     if (amount > this.#balance) {
//       throw new Error("Insufficient funds");
//     }
//     this.#balance -= amount;
//   }
//   getBalance() {
//     return this.#balance;
//   }
// }

// class CheckingAccount extends Account {
//   constructor(owner, balance) {
//     super(owner, balance);
//   }
//   withdraw(amount) {
//     if (amount <= 0) {
//       throw new Error("Withdrawal amount must be positive.");
//     }
//     const currentBalance = this.getBalance();

//     if (amount > currentBalance) {
//       console.log("Overdraft! You will be charged a $10 fee.");
//       super.deposit(-(amount + 10));
//     }
//   }
// }

// class SavingsAccount extends Account {
//   constructor(owner, balance) {
//     super(owner, balance);
//   }
//   withdraw(amount) {
//     if (amount <= 0) {
//       throw new Error("Withdrawal amount must be positive.");
//     }
//     const currentBalance = this.getBalance();
//     if (amount > currentBalance) {
//       throw new Error("Savings accounts do not allow overdrafts.");
//     }
//     super.withdraw(amount);
//   }
// }

// class Bank{
//   constructor(){
//     this.accounts = {}
//     this.nextId = 1;
//   }
//   createAccount(type,owner,initialBalance){
//     let account;
//     if(type === "checking"){
//       account = new CheckingAccount(owner,initialBalance)
//     }
//     else if(type === "savings"){
//       account = new SavingsAccount ( owner,initialBalance)
//     }
//     else{
//       throw new Error("Invalid Account type")
//     }
//     const accountId = this.nextId;
//     this.accounts[accountId] = account;
//     this.nextId ++;
//     return accountId

//   }
//   getAccount(id){
//     const account = this.accounts[id];
//     if(!account){
//       throw new Error("Account not found")
//     }
//     return account
//   }

//   transfer(fromId,toId,amount){
//     const fromAccount = this.getAccount(fromId);
//     const toAccount = this.getAccount(toId);

//     try{
//       fromAccount.withdraw(amount);
//       toAccount.deposit(amount)
//        console.log(`Transferred $${amount} from Account ${fromId} to Account ${toId}`);
//     }
//     catch(err){

//     }

//   }
//   listAccounts(){
//     for(const [id, account] of Object.entries(this.accounts)){
//       console.log(`Account ${id} - Owner: ${account.owner}, Type: ${account.constructor.name}, Balance: $${account.getBalance()}`);
//           }

//   }
// }

// const bank = new Bank();

// const id1 = bank.createAccount("checking", "Israel", 100);
// const id2 = bank.createAccount("savings", "Ana", 50);

// bank.transfer(id1, id2, 60); // Should succeed
// bank.transfer(id2, id1, 200); // ❌ Should fail: overdraft not allowed in savings

// console.log(bank.getAccount(id1).getBalance()); // 40
// console.log(bank.getAccount(id2).getBalance()); // 110

// bank.listAccounts()

//===============================================================================================================================

//   Contains Duplicate

// Solution
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example 1:

// Input: nums = [1,2,3,1]

// Output: true

// Explanation:

// The element 1 occurs at the indices 0 and 3.

// Example 2:

// Input: nums = [1,2,3,4]

// Output: false

// Explanation:

// All elements are distinct.

// Example 3:

// Input: nums = [1,1,1,3,3,4,3,2,4,2]

// Output: true

// Constraints:

// 1 <= nums.length <= 105
// -109 <= nums[i] <= 109
// //===============================================================================================================================

// // 1st solution
// function checkArray(nums) {
//   let frequencyOfNums = {};
//   for (let num of nums) {
//     if (!(num in frequencyOfNums)) {
//       frequencyOfNums[num] = (frequencyOfNums[num] || 0) + 1
//     } else {
//       return true;
//     }
//   }
//   return false;
// }
// let nums1 = [1,1,1,3,3,4,3,2,4,2]
// let result1 = checkArray(nums1)
// console.log(result1);

// // ------------------------------------------------------------------------------------------------------------------------------
// // 2)
// function checkArray(nums){
//   let setOfNumbers = new Set()
//   for(let num of nums){
//     if(setOfNumbers.has(num))return true 
//     setOfNumbers.add(num) 
      
//   }
//   return false;
// }

// let nums = [1,1,1,3,3,4,3,2,4,2]
// let result = checkArray(nums)
// console.log(result);