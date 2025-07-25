import random
import copy
#   Reverse Integer

# Solution
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


# Constraints:

# -231 <= x <= 231 - 1

# ------------------------------------------------------------------------------------------------------------------------------
# def reverse_num(num):
#     print(f"Input number: {num}")
#     max_range = 2 ** 31 - 1
#     min_range = -2 ** 31
#     print(f"32-bit range: [{min_range}, {max_range}]")

#     sign = -1 if num < 0 else 1
#     print(f"Sign determined: {sign}")
#     conver_to_positive = abs(num)
#     print(f"Absolute number (no sign): {conver_to_positive}")
#     reverse_nums = int(str(conver_to_positive)[::-1])
#     print(f"Reversed string: {reverse_nums}")

#     reverse_nums *= sign
#     print(f"Reversed number (after applying sign): {reverse_nums}")

#     if reverse_nums < min_range or reverse_nums > max_range:
#         print(f"Reversed number is out of 32-bit range. Returning 0.")
#         return 0

#     print(f"Final result (within range): {reverse_nums}")
#     return reverse_nums


# reverse_num(-120)

# ------------------------------------------------------------------------------------------------------------------------------

# 🔥 CHALLENGING PYTHON EXERCISE: Data Type Mastery
# 🧩 Problem: Deep Data Type Analysis Tool
# You're given a complex nested structure that contains different Python data types: dictionaries, lists, tuples, sets, and strings. Your task is to write a function called analyze_structure(data) that performs the following:

# ✅ Required Output:
# Return a dictionary with:

# 'total_elements': total number of all elements (including nested ones)

# 'data_types': a dictionary with counts of each data type found ('str', 'int', 'float', 'list', 'dict', 'set', 'tuple', etc.)

# 'unique_values': the number of unique values across the entire structure (including deeply nested values)

# 'most_common_type': the type that appears most frequently

# Handle cycles (e.g., if an object references itself), and avoid infinite recursion.

# 🧪 Example Input:
# python
# Copy
# Edit
# sample_data = {
#     'user1': {
#         'name': 'Alice',
#         'scores': [10, 20, 30],
#         'tags': {'python', 'developer'},
#     },
#     'user2': {
#         'name': 'Bob',
#         'scores': [25, 20.5, 30],
#         'tags': ('python', 'mentor'),
#     },
#     'misc': [None, True, {'notes': ['good', 'bad']}]
# }
# 💡 Output Example:
# python
# Copy
# Edit
# {
#     'total_elements': 20,
#     'data_types': {
#         'str': 7,
#         'int': 4,
#         'float': 1,
#         'list': 3,
#         'dict': 5,
#         'set': 1,
#         'tuple': 1,
#         'NoneType': 1,
#         'bool': 1
#     },
#     'unique_values': 15,
#     'most_common_type': 'str'
# }
# ⚠️ Constraints
# You must recursively explore nested structures.

# Use the type() function and collections.Counter.

# Do not mutate the original data.

# You may need to convert unhashable types when tracking unique values.


# def analyze_structure(data):
#     counter = 0
#     for value in data.values():
#         if isinstance(value,dict):
#             for sub_value in value.values():
#                 if isinstance(sub_value,(str)):
#                     counter += 1
#                 elif isinstance(sub_value,(list,set,tuple)):
#                     for item in sub_value:
#                         counter += 1

#         elif isinstance(value,(list,set,tuple)):
#             for element in value:
#                 if isinstance(element,(bool,type(None))):
#                     counter += 1
#                 elif isinstance(element,dict):
#                     for item in element.values():
#                         for jtem in item:
#                             counter += 1

#     return counter

# sample_data = {
#     'user1': {
#         'name': 'Alice',
#         'scores': [10, 20, 30],
#         'tags': {'python', 'developer'},
#     },
#     'user2': {
#         'name': 'Bob',
#         'scores': [25, 20.5, 30],
#         'tags': ('python', 'mentor'),
#     },
#     'misc': [None, True, {'notes': ['good', 'bad']}]
# # }
# print(analyze_structure(sample_data),"!!COUNTING!!")

# ===============================================================================================================================


# // 🧠 Exercise: Event Conflict Resolver
# // You are organizing a conference. Each speaker submits a list of time slots when they're available.

# // You must find all pairs of speakers who have at least one overlapping time slot, and then resolve the conflict by printing:

# // The speaker names

# // The overlapping slot(s)

# // A decision:

# // If both have 2 or more available slots → assign next available non-overlapping time to one.

# // If only one has 2+ slots → assign a new time to the one with more slots.

# // If both have only 1 slot → log as "Unresolvable Conflict."

# // 🔢 Input example:
# // python
# // Copy
# // Edit
# // # Python dict example
# // speakers = {
# //     "Alice": ["10:00", "11:00", "14:00"],
# //     "Bob": ["11:00", "13:00"],
# //     "Charlie": ["10:00"],
# //     "Diana": ["14:00", "15:00"]
# // }
# // js
# // Copy
# // Edit
# // // JS object equivalent
# // const speakers = {
# //     Alice: ["10:00", "11:00", "14:00"],
# //     Bob: ["11:00", "13:00"],
# //     Charlie: ["10:00"],
# //     Diana: ["14:00", "15:00"]
# // };
# // 🧩 Expected Output (example):
# // pgsql
# // Copy
# // Edit
# // Alice & Bob have conflict at: 11:00 ➜ Assign Bob to 13:00
# // Alice & Charlie have conflict at: 10:00 ➜ Unresolvable Conflict
# // Alice & Diana have conflict at: 14:00 ➜ Assign Diana to 15:00
# // 🎯 Your Task
# // Compare each unique speaker pair (no repeat pairs).

# // Check for overlapping time slots.

# // Based on how many total slots each speaker has, resolve or label as unresolvable.

# // Print the decision clearly.

# def organize_schedule(name_of_speakers):
#     speakers_names = list(name_of_speakers.keys())
#     for index in range(len(speakers_names)):
#         for subindex in range(index + 1, len(speakers_names)):
#             speaker1 = speakers_names[index]
#             speaker2 = speakers_names[subindex]

#             timeavailable1 = name_of_speakers[speaker1]
#             timeavailable2 =  name_of_speakers[speaker2]

#             commontime = list(filter(lambda t: t in timeavailable2, timeavailable1))

#             if commontime:
#                 assigned_time = commontime[0]
#                 assigned_speaker = random.choice([speaker1,speaker2])
#                 print(f"{speaker1} and {speaker2} have conflict at: {commontime} ➜Assign '{assigned_time}' to {assigned_speaker} ")
#             else:
#                 print(f"{speaker1} and {speaker2} have no coomon time")


# speakers = {
#      "Alice": ["10:00", "11:00", "14:00"],
#      "Bob": ["11:00", "13:00"],
#      "Charlie": ["10:00"],
#      "Diana": ["14:00", "15:00"]
#  }
# organize_schedule(speakers)

# ===============================================================================================================================
#   Rotate Image

# Solution
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000


# def matrix_grades(matrix):
#     for i in range(len(matrix)):
#         for j in range(i + 1,len(matrix[i])):
#             temp_num = matrix[i][j]
#             matrix[i][j] = matrix[j][i]
#             matrix[j][i] = temp_num

#     for i in range(len(matrix)):
#         left = 0
#         rigth = len(matrix) - 1
#         while left < rigth:
#             temp =  matrix[i][left]
#             matrix[i][left] = matrix[i][rigth]
#             matrix[i][rigth] = temp
#             left +=1
#             rigth -= 1
#     print(*matrix, sep="\n")


# m = [
#   [5, 1, 9, 11],
#   [2, 4, 8, 10],
#   [13, 3, 6, 7],
#   [15, 14, 12, 16],
# ]
# matrix_grades(m)

# ===============================================================================================================================
# 🚨 HARD EXERCISE 1: Deep Variable Behavior
# ✅ Problem Description (in both languages)
# You're given a list of employees. Each employee has a name and a list of skills. You must:

# Clone the original list

# Modify one of the inner lists (skills)

# Prove whether your clone is deep or shallow

# Show how variable declarations or object references affect the result
# 🟧 Python Version (Advanced typing + mutability + identity)
# ➕ Bonus: Use id() to track object references
# 🧠 What You're Proving
# In both languages, shallow copies copy references, not nested values

# Mutating inner structures affects both unless you deep clone

# const in JS only protects the variable, not the content

# Python’s variables are just names bound to objects; types are dynamic

# ------------------------------------------------------------------------------------------------------------------------------

# def var_behavior(list_of_objs):
#     deep_copy = copy.deepcopy(list_of_objs)
#     clone_obj = list_of_objs.copy()
#     clone_obj[1]["skills"] = "JS"
#     deep_copy[1]["skills"] = "YanyAan!"
#     print("!!ORIGINAL//ID!! --",id(list_of_objs))
#     print("!!COPY//ID!! --",id(clone_obj))
#     print("!!DeepCopy//ID!! --", id(deep_copy))
#     print("!!ORIGINAL//INNER!! --",id(list_of_objs[1]["skills"]))
#     print("!!COPY//INNER!! --",id(clone_obj[1]["skills"]))
#     print("!!DeepCopy//INNER!! --", id(deep_copy[1]["skills"]))


# employees = [
#     {"name": "Alice", "skills": ["JS", "Python"]},
#     {"name": "Bob", "skills": ["HTML", "CSS"]}
# ]

# var_behavior(employees)

# ===============================================================================================================================
#   Longest Common Prefix

# Solution
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

# def findPrefix(string):
#     prefix = ""
#     first_word = string[0]

#     for i in range(len(first_word)):
#         chars = first_word[i]

#         for j in range(1,len(string)):
#             if i >= len(string[j]) or string[j][i] != chars:
#                 return prefix
#         prefix += chars
#     return prefix


# print(findPrefix(["flower", "flow", "flight"])); # "fl"
# print(findPrefix(["dog", "racecar", "car"])); # ""
# print(findPrefix(["interview", "interrupt", "integrate", "integral"])); # "int"

# ===============================================================================================================================


#    Merge Sorted Array

# // Solution
# // You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# // Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# // The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# // Example 1:

# // Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# // Output: [1,2,2,3,5,6]
# // Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# // The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# // Example 2:

# // Input: nums1 = [1], m = 1, nums2 = [], n = 0
# // Output: [1]
# // Explanation: The arrays we are merging are [1] and [].
# // The result of the merge is [1].
# // Example 3:

# // Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# // Output: [1]
# // Explanation: The arrays we are merging are [] and [1].
# // The result of the merge is [1].
# // Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


# // Constraints:

# // nums1.length == m + n
# // nums2.length == n
# // 0 <= m, n <= 200
# // 1 <= m + n <= 200
# // -109 <= nums1[i], nums2[j] <= 109


# // Follow up: Can you come up with an algorithm that runs in O(m + n) time?
# def replace_index(nums1, m, nums2, n):
#     i = m - 1
#     j = n - 1
#     k = m + n - 1

#     while i >= 0 and j >= 0:
#         if nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#             k -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#             k -= 1

#     while j >= 0:
#         nums1[k] =nums2[j]
#         k -=1
#         j -= 1


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# replace_index(nums1, m, nums2, n)
# print(nums1)

# ===============================================================================================================================

# 🚨 HARD EXERCISE 2: Nested Data Transformation by Type

# // ## ✅ Problem Description (in both languages)

# // You're given a **deeply nested data structure** (a mix of lists/arrays, dictionaries/objects, strings, numbers, and booleans).

# // Your task:

# // 1. Traverse the entire structure (deep traversal)
# // 2. For each value:
# //     - If it's a **string**, convert to uppercase
# //     - If it's a **number**, multiply by 10
# //     - If it's a **boolean**, flip it
# //     - Leave anything else untouched
# // 3. Return a **new structure** (don't mutate the original)
# // 4. Must support **nested structures of any depth**

# def findTypes(input):
#     if isinstance(input,dict):
#         return {key:findTypes(value) for key,value in input.items()}

#     elif isinstance(input,list):
#         return [findTypes(value)for value in input]

#     elif isinstance(input,str):
#         return input.upper()

#     elif isinstance(input,bool):
#         return not input

#     elif isinstance(input,(int,float)):
#          return input * 10
#     else:
#         return input


# obj = {
#   "name": "alice",
#   "info": {
#     "age": 25,
#     "active": True,
#     "hobbies": ["reading", False, 3],
#     "preferences": {
#       "theme": "dark",
#       "fontsize": 12
#     }
#   }
# }
# result = findTypes(obj)
# print(result)

# ===============================================================================================================================

# 🚨 HARD EXERCISE: Matrix Word Search
# ✅ Problem (Both JavaScript & Python):
# You are given a 2D grid of characters and a target word. Write a function that returns true if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# 📘 Example:
# txt
# Copy
# Edit
# Input:
# grid = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED"

# Output: true

# Explanation: The word is found by going:
# A → B → C → C → E → D
# txt
# Copy
# Edit
# Input:
# word = "ABCB"

# Output: false (B is reused)
# 🎯 Requirements
# Use loops, not built-in search utilities

# Must use control flow (if, for, while, etc.)

# Handle edge cases (empty grid, word longer than grid, etc.)

# You can implement DFS with backtracking manually using loops (not recursion)


# def exits(grid,word):
#     def helper_function(row,column,index):


#         if index == len(word):
#             return True

#         if (row < 0 or row >= len(grid) or
#             column < 0 or column >= len(grid[row]) or
#             grid[row][column] != word[index]):
#             return False

#         print(f"Visiting: ({row}, {column}) = {grid[row][column]}, index = {index}")
#         temp = grid[row][column]
#         grid[row][column] = "#"

#         found = ( helper_function(row + 1, column, index + 1) or
#                   helper_function(row - 1, column, index + 1) or
#                   helper_function(row , column + 1, index + 1) or
#                   helper_function(row , column - 1, index + 1)
#                   )

#         grid[row][column] = temp
#         return found


#     for row in range(len(grid)):
#         for column in range(len(grid[row])):
#             if grid[row][column] == word[0]:
#                 if helper_function(row,column,0):
#                     return True
#     return False


# input = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED"
# result = exits(input, word)


# # Output: true
# # Explanation: The word is found by going:
# # A → B → C → C → E → D
# ===============================================================================================================================
# def find_steps(steps):
#     if steps == 1: return 1
#     if steps == 2: return 2

#     first = 1
#     second = 2
#     current = 0

#     for i in range(3, steps + 1):
#      current = first + second
#      print(f"Step {i}: {first} + {second} = {current}")
#      first = second
#      second = current

#     return current


# n = 5
# result = find_steps(n)
# print(result)

# ===============================================================================================================================

# Absolutely! Here's a challenging OOP exercise designed for both JavaScript and Python. It focuses on deep understanding and application of:

# Encapsulation

# Inheritance

# Polymorphism

# Class methods

# Composition

# Clean logic and real-world modeling

# 🚨 HARD OOP EXERCISE: "Digital Library System"
# 📚 Problem Description
# You're going to build a Digital Library System that manages books, users, and the process of borrowing/returning books.

# ✅ Requirements (apply to both JavaScript and Python):
# 1. Class Book
# Attributes: title, author, genre, available (boolean)

# Method: toString() in JS / __str__() in Python — prints book info

# 2. Class User (Base Class)
# Attributes: name, id, borrowedBooks (or borrowed_books)

# Methods:

# borrow(book): Can borrow the book only if available

# returnBook(book): Removes book from user's list

# listBooks(): Lists current borrowed books

# 3. Subclasses
# Student → inherits from User, max 3 books

# Professor → inherits from User, max 5 books

# 4. Class Library
# Attributes:

# books: list of all books

# users: list of all users

# Methods:

# addBook(book)

# registerUser(user)

# findBookByTitle(title)

# showAllBooks()

# showUsers()

# ➕ Bonus Challenges (Optional but Advanced)
# Prevent returning books that weren’t borrowed

# Track borrow dates and calculate late return penalties

# Use composition for a LoanManager helper class

# Use static methods or decorators (Python)

# 📦 JavaScript Skeleton (Class Syntax):
# js
# Copy
# Edit
# class Book {
#   constructor(title, author, genre) {
#     this.title = title;
#     this.author = author;
#     this.genre = genre;
#     this.available = true;
#   }

#   toString() {
#     return `${this.title} by ${this.author} [${this.genre}]`;
#   }
# }

# class User {
#   constructor(name, id) {
#     this.name = name;
#     this.id = id;
#     this.borrowedBooks = [];
#   }

#   borrow(book) {
#     // to implement
#   }

#   returnBook(book) {
#     // to implement
#   }

#   listBooks() {
#     // to implement
#   }
# }

# // class Student extends User ...
# // class Professor extends User ...
# // class Library { ... }
# 🐍 Python Skeleton:
# python
# Copy
# Edit
# class Book:
#     def __init__(self, title, author, genre):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.available = True

#     def __str__(self):
#         return f"{self.title} by {self.author} [{self.genre}]"

# class User:
#     def __init__(self, name, user_id):
#         self.name = name
#         self.user_id = user_id
#         self.borrowed_books = []

#     def borrow(self, book):
#         pass

#     def return_book(self, book):
#         pass

#     def list_books(self):
#         pass

# # class Student(User)
# # class Professor(User)
# # class Library
# 🧠 Concepts You’ll Practice
# Class structure & attributes

# Encapsulation (e.g. #private or _protected)

# Inheritance + Method overriding

# Logical constraints (max books per user type)

# Composition (optional)

# State tracking (borrowed vs available)

# Clean and reusable OOP design

# class Book:
#     def __init__(self, title, author, genre, ):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.available = True

#     def __str__(self):
#         return f"{self.title} by {self.author} [{self.genre}]"


# class User:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         self.borrowed_books = []

#     def __str__(self):
#         return f"{self.name}: {self.id}"

#     def borrow(self, book):
#         if book.available:
#             self.borrowed_books.append(book)
#             book.available = False
#             print(f"{self.name} has borrowed '{book.title}'")
#         else:
#             print(f"'{book.title}' is not available")

#     def returnBook(self, book):
#         if book in self.borrowed_books:
#             self.borrowed_books.remove(book)
#             book.available = True
#             print(f"{self.name} has returned '{book.title}'")
#         else:
#             print(f"{self.name} doesn't have '{book.title}' borrowed")

#     def list_books(self):
#         if not self.borrowed_books:
#             print(f"{self.name} has no books borrowed.")
#         else:
#             print(f"{self.name} has borrowed:")
#             for book in self.borrowed_books:
#                 print(f" - {book}")


# class Student(User):
#     def borrow(self, book):
#         if len(self.borrowed_books) >= 3:
#             print(f"{self.name} has reached the borrowing limit (3 books).")
#         else:
#             super().borrow(book)


# class Professor(User):
#     def borrow(self, book):
#         if len(self.borrowed_books) >= 5:
#             print(f"{self.name} has reached the borrowing limit (3 books).")
#         else:
#          super().borrow(book)


# class Library:
#     def __init__(self):
#         self.books = []
#         self.users = []

#     def addBook(self, book):
#         self.books.append(book)
#         print(f"'{book.title}' added to the library.")

#     def registerUser(self, user):
#         self.users.append(user)
#         print(f"'{user.name}' added to the library.")

#     def findBookByTitle(self, title):
#         for book in self.books:
#             if book.title == title:
#                 return book
#         print(f"No book with title '{title}' found.")
#         return None

#     def showAllBooks(self):
#         if not self.books:
#             print("No books to show")
#         else:
#             print("Books in the library:")
#             for i, book in enumerate(self.books, 1):
#                 print(f"{i}. {book}")

#     def showUsers(self):
#         if not self.users:
#             print("No users found")
#         else:
#             print("Registered users:")
#             for i, user in enumerate(self.users, 1):
#                 print(f"{i}. {user}")


# library = Library()

# # 2. Add Books
# books = [
#     Book("1984", "George Orwell", "Dystopian"),
#     Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
#     Book("Sapiens", "Yuval Noah Harari", "Non-fiction"),
#     Book("Brave New World", "Aldous Huxley", "Sci-fi"),
#     Book("The Alchemist", "Paulo Coelho", "Fiction"),
#     Book("Clean Code", "Robert C. Martin", "Tech")
# ]

# for b in books:
#     library.addBook(b)

# # 3. Add Users
# student = Student("Alice", 101)
# professor = Professor("Dr. Smith", 201)
# library.registerUser(student)
# library.registerUser(professor)

# # 4. Borrowing
# student.borrow(books[0])
# student.borrow(books[1])
# student.borrow(books[2])
# student.borrow(books[3])  # ❌ Limit

# professor.borrow(books[3])
# professor.borrow(books[4])
# professor.borrow(books[5])

# # 5. Show Users/Books
# print("\n--- BORROWED BOOKS ---")
# student.list_books()
# professor.list_books()

# print("\n--- LIBRARY STATE ---")
# library.showAllBooks()
# library.showUsers()

# ===============================================================================================================================
#   Pascal's Triangle

# Solution
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]


# Constraints:

# 1 <= numRows <= 30

# 1):
# def triangle_pascal(rows):
#     result = []
#     for i in range(rows):
#         row = []
#         for j  in range(i + 1):
#             if j == 0 or j == i :
#                 row.append(1)
#             else:
#                 prev = result[i - 1]
#                 row.append(prev[j-1] + prev[j])
#         result.append(row)
#     return result


# n=5
# print(triangle_pascal(n))
# #------------------------------------------------------------------------------------------------------------------------------
# def wordBreak(s, wordDict):
#     word_set = set(wordDict)
#     result = []

#     def backtrack(start,path):
#         if start == len(s):
#             result.append(" ".join(path))
#             return

#         for end in range(start + 1, len(s) + 1):
#             word = s[start:end]
#             if word in word_set:
#                 backtrack(end, path + [word])
#         backtrack(0,[])
#         return result


# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]

# print(wordBreak(s, wordDict))
# //===============================================================================================================================
# def firstBadVersion(n):
#     left = 1
#     right = n

#     def isBadVersion(version):
#         return version >= bad  # Simulates that every version from 'bad' onward is bad

#     while left < right:
#         mid = (left + right) // 2
#         print(f"Checking version {mid} (left: {left}, right: {right})")

#         if isBadVersion(mid):
#             print(f"Version {mid} is bad, moving right to {mid}")
#             right = mid
#         else:
#             print(f"Version {mid} is good, moving left to {mid + 1}")
#             left = mid + 1
#     return left


# n = 5
# bad = 3

# print("First bad version is:", firstBadVersion(n))  # Output: 4

# //===============================================================================================================================
#   Rotate Array

# Solution
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
 

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

#------------------------------------------------------------------------------------------------------------------------------
# Aditional array
# def rotate(nums,k):
#     result = [0] * len(nums)
#     for i in range(len(nums)):
#         new_index = (i + k) % len(nums)
#         result[new_index] = nums[i]
#     return result  


# nums = [1,2,3,4,5,6,7]
# k = 3
# result = rotate(nums,k)
# print(result)  # ✅ [5, 6, 7, 1, 2, 3, 4]
# ------------------------------------------------------------------------------------------------------------------------------
# In place
# def rotate(nums, k):
#     k = k % len(nums)
#     count = 0
#     start = 0

#     print(f"🔄 Rotating by {k} steps")
#     print(f"📦 Initial array: {nums}\n")

#     while count < len(nums):
#         current_index = start
#         prev = nums[start]
#         print(f"🚀 Starting new cycle from index {start} (value = {prev})")

#         while True:
#             next_index = (current_index + k) % len(nums)
#             print(f"➡️ Moving value {prev} to index {next_index}")

#             temp = nums[next_index]
#             print(f"🧠 Saving current value at index {next_index}: {temp}")

#             nums[next_index] = prev
#             print(f"📌 Placing {prev} at index {next_index}")

#             prev = temp
#             current_index = next_index
#             count += 1

#             print(f"🔁 Next round: carry = {prev}, new current_index = {current_index}, count = {count}\n")

#             # If we returned to the start of the cycle, break
#             if current_index == start:
#                 print("⛔ End of cycle reached. Breaking to start next cycle.\n")
#                 break

#         start += 1  # try a new cycle if needed (for unvisited elements)

#     print(f"✅ Final rotated array: {nums}")


# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# rotate(nums, k)
# print(nums)  # ✅ [5, 6, 7, 1, 2, 3, 4]

#===============================================================================================================================
    
#          Contains Duplicate

# Solution
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109 

##1)
# def check_Array(nums):
#     freq_num = {}
#     for num in nums:
#         if num not in freq_num:
#             freq_num[num] = freq_num.get(num,0) + 1  
#         else:
#             return True
#     return False

# nums = [1, 2, 3, 4]  # You can change this input to test other cases
# result = check_Array(nums)
# print("Contains duplicate:", result)
# #===============================================================================================================================
# #2)
# def sorteArray(nums):
#     set_of_nums = set()
#     for num in nums:
#         if num not in set_of_nums:
#             set_of_nums.add(num)
#         else:
#             return True
#     return False      


# nums = [1, 2, 3, 4,5,6,2]  # You can change this input to test other cases
# result = sorteArray(nums)
# print("Contains duplicate:", result)  


