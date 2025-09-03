# import random
# import copy

# #   Reverse Integer

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

# ------------------------------------------------------------------------------------------------------------------------------
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

# ===============================================================================================================================

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

# 1)
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


# ===============================================================================================================================
# 1)
# def find_double(arr):
#     arr.sort()
#     for i in range(0, len(arr) - 1, 2):
#         if arr[i] != arr[i + 1]:
#             return arr[i]
#     return arr[len(arr) - 1]


# nums = [1,5,6,4,5,6,4,1,8]
# result = find_double(nums)
# print(result)

# ------------------------------------------------------------------------------------------------------------------------------
# #2)
# def find_double(arr):
#     result = 0
#     for num in arr:
#         result ^= num
#     return result

# nums = [1,5,6,4,5,6,4,1,8]
# result = find_double(nums)
# print(result)
# //===============================================================================================================================

# 🚗 Exercise: Vehicle Rental System
# 🧠 Objective:
# Build a system that allows users to rent vehicles. You should be able to add different types of vehicles (e.g., cars, bikes), track their availability, calculate rental costs based on duration, and manage returns.

# ✅ Requirements:
# Base Class: Vehicle
# Properties:

# brand

# model

# rental_rate_per_day

# is_available (default: True)

# Methods:

# rent() → changes availability

# return_vehicle() → changes availability

# calculate_rental_cost(days)

# Subclasses:
# Car

# Extra property: num_doors

# Override calculate_rental_cost → add 10% tax

# Bike

# Extra property: engine_capacity

# Override calculate_rental_cost → flat discount of $5 if rented for more than 3 days

# 🧪 Sample Behavior:
# plaintext
# Copy
# Edit
# car = Car("Toyota", "Camry", 50, 4)
# car.rent() → marks it as not available
# car.calculate_rental_cost(3) → 50*3 + 10% = $165
# car.return_vehicle() → now available

# bike = Bike("Yamaha", "MT-07", 30, 700)
# bike.calculate_rental_cost(4) → (30*4 - 5) = $115
# 🧩 What You Will Practice:
# Inheritance and method overriding

# Encapsulation (optional challenge: make attributes private)

# Object instantiation and class interaction

# Logical branching and real-world modeling


# class Vehicle:
#     def __init__(self,brand,model,is_available,rental_rate_per_day):
#         self.brand = brand
#         self.model = model
#         self.is_available = is_available
#         self.rental_rate_per_day = rental_rate_per_day

#     def __str__(self):
#      status = "available" if self.is_available else "not available"
#      return f"{self.brand} {self.model} - {status}, ${self.rental_rate_per_day}/day"


#     def rent(self):
#         if self.is_available:
#             self.is_available = False
#             print(f"{self.brand} {self.model} has been rented")
#         else:
#             print(f"{self.brand} {self.model} is not available")

#     def return_vehicle(self):
#         self.is_available = True
#         print(f"{self.brand} {self.model} has been returned and is now available.")


#     def calculate_rental_cost(self,days):
#         return self.rental_rate_per_day * days


# class Car(Vehicle):
#     def __init__(self, brand, model, is_available, rental_rate_per_day, number_of_doors):
#         super().__init__(brand, model, is_available, rental_rate_per_day)
#         self.number_of_doors = number_of_doors

#     def calculate_rental_cost(self, days):
#         base_cost = super().calculate_rental_cost(days)
#         tax = base_cost * 0.10
#         return base_cost + tax


# class Bike(Vehicle):
#         def __init__(self, brand, model, is_available, rental_rate_per_day,engine_capacity):
#              super().__init__(brand, model, is_available, rental_rate_per_day)
#              self.engine_capacity = engine_capacity

#         def calculate_rental_cost(self, days):
#             rental_cost = super().calculate_rental_cost(days)
#             if days > 3:
#                 rental_cost -= 0.5
#             return rental_cost


# print("🔧 Testing regular Vehicle:")
# v1 = Vehicle("Honda", "Civic", True, 40)
# print(v1)
# v1.rent()
# print(v1)
# print("Rental cost for 2 days:", v1.calculate_rental_cost(2))
# v1.return_vehicle()
# print(v1)
# print("")

# print("🚗 Testing Car (with 10% tax):")
# car = Car("BMW", "3 Series", True, 100, 4)
# print(car)
# car.rent()
# print("Rental cost for 5 days:", car.calculate_rental_cost(5))  # Should be 550
# car.return_vehicle()
# print(car)
# print("")

# print("🏍️ Testing Bike (with discount after 3 days):")
# bike = Bike("Yamaha", "MT-07", True, 30, 689)
# print(bike)
# bike.rent()
# print("Rental cost for 4 days:", bike.calculate_rental_cost(4))  # Should be 119.5
# bike.return_vehicle()
# print(bike)

# ===============================================================================================================================

# def decode_doc(url):
#     import requests
#     from bs4 import BeautifulSoup

#     response = requests.get(url)  # fetch the raw HTML content from the internet.
#     converted_to_read = BeautifulSoup(response.content, 'html.parser')# turn that HTML into something you can search and extract data from.

#     coord = []

#     rows = converted_to_read.find_all('tr')[1:] # Skip the header row
#     for row in rows:
#      cells = row.find_all('td')
#      cleaned = [cell.text.strip() for cell in cells]
#      if len(cleaned) == 3:  # Ensure there are exactly 3 columns
#         x = int(cleaned[0])
#         char = cleaned[1]
#         y = int(cleaned[2])
#         coord.append((x, y, char))

#     max_x = max(p[0] for p in coord)
#     max_y = max(p[1] for p in coord)
#     grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

#     for x, y, char in coord:
#      grid[y][x] = char

#     for row in grid:
#      print(''.join(row))


# decode_doc("https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub")

# ===============================================================================================================================
#   Intersection of Two Arrays II

# Solution
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# #1)
# def intersection_arr(arr1,arr2):
#     dict_arr1 = {}
#     dict_arr2 = {}
#     result = []

#     for number in arr1:
#         dict_arr1[number] = dict_arr1.get(number,0) + 1

#     for number in arr2:
#         dict_arr2[number] = dict_arr2.get(number,0) + 1

#     for num in dict_arr1:
#         if num in dict_arr2:
#             min_count = min(dict_arr1[num],dict_arr2[num])
#             for _ in range(min_count):
#                 result.append(num)

#     return result


# nums1 = [4,9,5,4,4,4,9]
# nums2 = [9,4,9,8,4,4,9,9,9]
# result =  intersection_arr(nums1,nums2)
# print(result)


# ===============================================================================================================================
# 2)
# from collections import defaultdict
# def intersection(arr1,arr2):
#     count = defaultdict(int)
#     result = []

#     for num in arr1:
#         count[num] = 0

#     for num in arr2:
#         if count[num] > 0:
#             result.append(num)
#             count[num] -= 1
#     return result
# ===============================================================================================================================
# 3)Hash Map (Frequency Counter)
# def intersection(arr1,arr2):
#     count = {}
#     result = []

#     for num in arr1:
#         count[num] = count.get(num,0) + 1

#     for num in arr2:
#         if num in count and count[num] > 0:
#             result.append(num)
#             count[num] -= 1
#     return result

# ===============================================================================================================================
#   Plus One

# Solution
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

# ===============================================================================================================================
# 1)
# def add_digit(arr):
#     for i in range(len(arr) - 1, -1, -1):
#         if arr[i] < 9:
#             arr[i] += 1
#             return arr
#         arr[i] = 0
#     return [1] + arr

# digits = [1,2,3]
# reslut = add_digit(digits)
# print(reslut)
# ===============================================================================================================================
#   Move Zeroes

# Solution
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


# Follow up: Could you minimize the total number of operations done?
# ===============================================================================================================================
# 1))
# def move_zeros(arr):
#     counter_of_zeros = 0

#     for i in range(len(arr)):
#         if arr[i] == 0:
#             counter_of_zeros += 1
#         elif counter_of_zeros > 1:
#             arr[i - counter_of_zeros] = arr[i]
#             arr[i] = 0
#     return arr


# nums = [0, 1, 0, 3, 12]
# result = move_zeros(nums)
# print(result)
# # ===============================================================================================================================
# # 2)
# def move_zeros(arr):
#     counter = 0

#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[counter] = arr[i]
#             counter += 1

#     for i in range(counter, len(arr)):
#         arr[i] = 0

#     return arr


# nums = [0, 1, 0, 3, 12]
# result = move_zeros(nums)
# print(result)
# ===============================================================================================================================
# 1) Brute force  Time = O(n²)   Space =	O(1)
# def two_sums(arr,target):
#     for i in range(len(arr)):
#         for j  in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target:
#              return [i , j]


# nums = [2,7,11,15]
# target = 9
# result = two_sums(nums,target)
# print(result)
# ===============================================================================================================================
# 2)Hash map  (Optimized – Time Complexity O(n)
# def two_sums(arr,target):
#     map_numbers = {}

#     for i,num in enumerate(arr):
#         complement = target - num
#         if complement in map_numbers:
#             return [map_numbers[complement], i]
#         map_numbers[num] = i


# nums = [2,7,11,15]
# target = 9
# result = two_sums(nums,target)
# print(result)

# 1)d
# def find_double(board):
#     rows = [set() for _ in range(9)]
#     columns = [set() for _ in range(9)]
#     boxes = [set() for _ in range(9)]

#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             cell = board[i][j]
#             if cell == ".":
#                 continue
#             if cell  in rows[i]:
#              return False
#             rows[i].add(cell)

#             if cell in columns[j]:
#                return False
#             columns[j].add(cell)

#             box_number = i // 3 * 3 + j // 3
#             if cell in boxes[box_number]:
#                 return False
#             boxes[box_number].add(cell)
#     return True

# board = [
#  ["5","5",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]
# ]
# result = find_double(board)
# print(result)


# ===============================================================================================================================
# 1)
# def first_non_repeating(str):
#    n = len(str)
#    for i in range(n):
#       unique = True
#       for j in range(n):
#          if i != j and str[i] == str[j]:
#             unique = False
#             break
#       if unique:
#             return i
#    return -1

# s = "agfagf"
# print(first_non_repeating(s))
# ===============================================================================================================================
# 2)
# from collections import Counter

# def first_non_repeating(str):
#     freq = Counter(str)
#     for i,value in enumerate(s):
#         if freq[value] == 1:
#             return i
#     return -1


# s = "agfagf"
# first_non_repeating(s)
# print(first_non_repeating(s))

# ===============================================================================================================================


#       Valid Anagram

# Solution
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# ===============================================================================================================================

# 1)
# from collections import Counter


# def find_anagram(s1,s2):
#     return Counter(s1) == Counter(s2)

# s = "rat"
# t = "tar"
# print(find_anagram(s,t))
# ===============================================================================================================================

# 2)

# def find_anagram(s1,s2):
#     if len(s1) != len(s2):
#         return False

#     freq_s1 = {}
#     for char in s1:
#         freq_s1[char] = freq_s1.get(char,0) + 1

#     for char in s2:
#         if char not in freq_s1:
#             return False
#         freq_s1[char] -= 1
#         if freq_s1[char] < 0:
#             return False

#     for count in freq_s1.values():
#         if count > 0:
#             return False

#     return True


# s = "rat"
# t = "tar"
# print(find_anagram(s,t))
# //===============================================================================================================================
#   Valid Palindrome

# Solution
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
# ===============================================================================================================================
# 1)  build cleaned string + reverse

# def is_palindrome(s):
#     cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
#     return cleaned == cleaned[::-1]

# s = "A man, a plan, a canal: Panama"
# # result = is_palindrome(s)
# print(is_palindrome("A man, a plan, a canal: Panama"))  # expect True
# print(is_palindrome("race a car"))                      # expect False
# print(is_palindrome("0P"))                              # expect False
# print(is_palindrome(".,,"))                             # expect True
# print(is_palindrome("a"))                               # expect True
# # //===============================================================================================================================
# # 2)Two Pointers (Skip & Compare):

# def is_palindrome(s):
#     i = 0
#     j = len(s) - 1

#     while i < j:
#         while i < j and not s[i].isalnum():
#             i +=1

#         while i < j and not s[j].isalnum():
#             j -=1

#         if s[i].lower() != s[j].lower():
#             return False

#         i += 1
#         j -= 1

#     return True

# s = "A man, a plan, a canal: Panama"
# # result = is_palindrome(s)
# print(is_palindrome("A man, a plan, a canal: Panama"))  # expect True
# print(is_palindrome("race a car"))                      # expect False
# print(is_palindrome("0P"))                              # expect False
# print(is_palindrome(".,,"))                             # expect True
# print(is_palindrome("a"))                               # expect True


# // #===============================================================================================================================
# //   String to Integer (atoi)

# // Solution
# // Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# // The algorithm for myAtoi(string s) is as follows:

# // Whitespace: Ignore any leading whitespace (" ").
# // Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# // Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# // Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# // Return the integer as the final result.


# // Example 1:

# // Input: s = "42"

# // Output: 42

# // Explanation:

# // The underlined characters are what is read in and the caret is the current reader position.
# // Step 1: "42" (no characters read because there is no leading whitespace)
# //          ^
# // Step 2: "42" (no characters read because there is neither a '-' nor '+')
# //          ^
# // Step 3: "42" ("42" is read in)
# //            ^
# // Example 2:

# // Input: s = " -042"

# // Output: -42

# // Explanation:

# // Step 1: "   -042" (leading whitespace is read and ignored)
# //             ^
# // Step 2: "   -042" ('-' is read, so the result should be negative)
# //              ^
# // Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
# //                ^
# // Example 3:

# // Input: s = "1337c0d3"

# // Output: 1337

# // Explanation:

# // Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
# //          ^
# // Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
# //          ^
# // Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
# //              ^
# // Example 4:

# // Input: s = "0-1"

# // Output: 0

# // Explanation:

# // Step 1: "0-1" (no characters read because there is no leading whitespace)
# //          ^
# // Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
# //          ^
# // Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
# //           ^
# // Example 5:

# // Input: s = "words and 987"

# // Output: 0

# // Explanation:

# // Reading stops at the first non-digit character 'w'.


# // Constraints:

# // 0 <= s.length <= 200
# // s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

# def fix_string(s):
#     i = 0
#     result = 0
#     n = len(s)
#     sign = 1

#     while i < n and ord(s[i] == 32):
#         i += 1

#     if i < n and (s[i] == "-" or s[i] == "+"):
#         sign = -1 if s[i] == "-" else 1
#         i += 1

#     ABS_LIMIT =  2147483647  if sign == 1 else 2147483648
#     CUT = ABS_LIMIT // 10
#     LIMIT = ABS_LIMIT % 10

#     while i < n:
#         code = ord(s[i])
#         if code < 48 or code > 57:
#             break

#         d = code - 48

#         if result > CUT or (result == CUT and d > LIMIT):
#             return 2147483647 if sign == 1 else -2147483648

#         result = result * 10 + d
#         i += 1


# print(fix_string("   -042"))         # -42
# print(fix_string("1337c0d3"))        # 1337
# print(fix_string("0-1"))             # 0
# print(fix_string("words and 987"))   # 0
# print(fix_string("000abc"))          # 0
# print(fix_string("21474836460"))     # 2147483647 (clamped)
# print(fix_string("-21474836490"))    # -2147483648 (clamped)
# print(fix_string("   +000"))         # 0
# print(fix_string("   +000 123"))     # 0
# ===============================================================================================================================
#   Implement strStr()

# Solution
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.
# #===============================================================================================================================
# #1)
# def strStr(haystack, needle):
#     n,m = len(haystack), len(needle)

#     if m == 0:
#         return 0

#     for i in range(n - m + 1):
#         if haystack[i:i+m] == needle:
#             return i

#     return -1


# haystack = "abcdeasfde"
# needle = "de"
# # //===============================================================================================================================
# #2)
# def strStr(haystack, needle):
#     return haystack.find(needle)


# ===============================================================================================================================

#   Delete Node in a Linked List

# Solution
# There is a singly-linked list head and we want to delete a node node in it.

# You are given the node to be deleted node. You will not be given access to the first node of head.

# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

# Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

# The value of the given node should not exist in the linked list.
# The number of nodes in the linked list should decrease by one.
# All the values before node should be in the same order.
# All the values after node should be in the same order.
# Custom testing:

# For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
# We will build the linked list and pass the node to your function.
# The output will be the entire list after calling your function.


# Example 1:


# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
# Example 2:


# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


# Constraints:

# The number of the nodes in the given list is in the range [2, 1000].
# -1000 <= Node.val <= 1000
# The value of each node in the list is unique.
# The node to be deleted is in the list and is not a tail node.

# ===============================================================================================================================
# 1)
# class ListNode:
#     def __init__(self, val=0, next = None):
#         self.val = val
#         self.next = next

# head = ListNode(4)
# head.next = ListNode(5)
# head.next.next = ListNode(1)
# head.next.next.next = ListNode(9)

# def delete_node(node):
#     next = node.next
#     node.val = next.val
#     node.next = next.next


# def print_list(head):
#     vals = []
#     while head:
#         vals.append(head.val)
#         head = head.next
#     print(" -> ".join(map(str, vals)))

# print("Before deletion:")
# print_list(head)

# delete_node(head.next)  # delete the node with value 5

# print("After deletion:")
# print_list(head)
# ===============================================================================================================================
#   Remove Nth Node From End of List

# Solution
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Follow up: Could you do this in one pass?
# ===============================================================================================================================
# class ListNode:
#     def __init__(self,val=0, next=None):
#         self.val = val
#         self.next = next

# def build_list(values):
#     """Create a linked list from a Python list and return head."""
#     if not values:
#         return None
#     head = ListNode(values[0])
#     curr = head
#     for v in values[1:]:
#         curr.next = ListNode(v)
#         curr = curr.next
#     return head

# def to_list(head):
#     """Convert a linked list back to a Python list for easy viewing."""
#     out = []
#     while head:
#         out.append(head.val)
#         head = head.next
#     return out

# def print_list(head, label="list"):
#     print(label, "→", " -> ".join(map(str, to_list(head))) if head else "[]")


# def removeNthFromEnd(head,n):
#     length = 0
#     node = head

#     while node:
#         length += 1
#         node = node.next

#     index_to_remove  = length - n

#     if index_to_remove == 0:
#         return head.next

#     curr = head
#     for _ in range(index_to_remove - 1):
#         curr = curr.next
#     curr.next = curr.next.next

#     return head


# # Example 1
# head = build_list([1,2,3,4,5])
# print_list(head, "before")
# head = removeNthFromEnd(head, 2)
# print_list(head, "after n=2")     # expect 1 -> 2 -> 3 -> 5

# # Example 2
# head = build_list([1])
# print_list(head, "before")
# head = removeNthFromEnd(head, 1)
# print_list(head, "after n=1")     # expect []

# # Example 3
# head = build_list([1,2])
# print_list(head, "before")
# head = removeNthFromEnd(head, 1)
# print_list(head, "after n=1")     # expect 1

# # Extra head-removal check
# head = build_list([1,2,3])
# print_list(head, "before")
# head = removeNthFromEnd(head, 3)
# print_list(head, "after n=3")     # expect 2 -> 3
# //===============================================================================================================================
#   Palindrome Linked List

# Solution
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false


# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9


# Follow up: Could you do it in O(n) time and O(1) space?
# //===============================================================================================================================+

# 1)
# def check_palindrome(head):
#     values = []
#     curr = head

#     while curr:
#         values.append(curr.value)
#         curr = curr.next

#     return values == values[::-1]


# //===============================================================================================================================

# //   Linked List Cycle

# // Solution
# // Given head, the head of a linked list, determine if the linked list has a cycle in it.

# // There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# // Return true if there is a cycle in the linked list. Otherwise, return false.


# // Example 1:


# // Input: head = [3,2,0,-4], pos = 1
# // Output: true
# // Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# // Example 2:


# // Input: head = [1,2], pos = 0
# // Output: true
# // Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# // Example 3:


# // Input: head = [1], pos = -1
# // Output: false
# // Explanation: There is no cycle in the linked list.


# // Constraints:

# // The number of the nodes in the list is in the range [0, 104].
# // -105 <= Node.val <= 105
# // pos is -1 or a valid index in the linked-list.


# // Follow up: Can you solve it using O(1) (i.e. constant) memory?


# //===============================================================================================================================
# Linked list

# class LinkedList:
#     def __init__(self,val=0, next=None):
#           self.val = val
#           self.next = next

# def building_linked_list(arr):
#     if len(arr) == 0:
#         return None

#     head = LinkedList(arr[0])
#     curr = head

#     for i in range(1, len(arr)):
#         curr.next = LinkedList(arr[i])
#         curr = curr.next

#     return head

# nodes = building_linked_list([3, 2, 0, -4]);
# print(nodes)

# #Solution:
# def check_cycle(head):
#     slow,fast = head,head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast: return True
#     return False
# //------------------------------------------------------------------------------------------------------------------------------


#   Maximum Depth of Binary Tree

# Solution
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2


# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100
#  //------------------------------------------------------------------------------------------------------------------------------
# 1)DFS (Depth-First Search) Solution:

# Blueprint to build tree.
# from collections import deque

# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def tree(values):
#     if not values:
#         return None

#     root = TreeNode(values[0])
#     q = deque([root])
#     i = 1

#     while q and i < len(values):
#         node = q.popleft()

#         #left pointer:
#         if values[i] is not None:
#             node.left = TreeNode(values[i])
#             q.append(node.left)
#         i += 1

#         if i < len(values) and values[i] is not None:
#             node.right = TreeNode(values[i])
#             q.append(node.rigth)
#         i += 1

#         return root


# input = [3,9,20,None,None,15,7]

from collections import deque
from typing import Optional, List, Any

# ----- Node -----


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    # Pretty print for debugging (so printing a node or a deque of nodes is readable)
    def __repr__(self) -> str:
        return f"TreeNode({self.val})"

# ----- Debug helpers -----


def print_queue(q: deque):
    """Show only the .val of nodes currently in the queue."""
    print("Queue:", [n.val for n in q])


def print_tree_level_order(root: Optional[TreeNode]):
    """Print the built tree level-by-level (values only)."""
    if not root:
        print("Tree: []")
        return
    out, q = [], deque([root])
    while q:
        level_vals = []
        for _ in range(len(q)):
            node = q.popleft()
            level_vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level_vals)
    print("Tree levels:", out)

# ----- Build tree from level-order list with debug prints -----


def build_tree(values: List[Any]) -> Optional[TreeNode]:
    """
    Build a binary tree from level-order list like [3,9,20,None,None,15,7].
    Prints queue state at each step so you can see BFS construction.
    """
    if not values:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    i = 1

    print("Start building:")
    print_queue(q)

    while q and i < len(values):
        node = q.popleft()
        print(f"\nProcessing parent node: {node.val}")

        # Left child
        if values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
            print(f"  Added LEFT  child {values[i]}")
        else:
            print("  Skipped LEFT  child (None)")
        i += 1

        # Right child (guard i, because we just advanced it)
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
            print(f"  Added RIGHT child {values[i]}")
        elif i < len(values):
            print("  Skipped RIGHT child (None)")
        i += 1

        print_queue(q)  # show queue after processing this parent

    print("\nFinished building.")
    print_tree_level_order(root)
    return root

# ----- DFS: Maximum Depth -----


def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    # Postorder: compute children first, then use 1 + max(left, right)
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# ----- Quick demo/tests -----
if __name__ == "__main__":
    # Example 1 from the problem
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("Max depth (example 1) =", maxDepth(root1))  # expected 3

    # Example 2
    root2 = build_tree([1, None, 2])
    print("Max depth (example 2) =", maxDepth(root2))  # expected 2

    # Extra checks
    root3 = build_tree([])  # empty
    print("Max depth (empty) =", maxDepth(root3))      # expected 0

    root4 = build_tree([1, 2, 3, 4, 5])  # a fuller shape
    print("Max depth (extra) =", maxDepth(root4))
