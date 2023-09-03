**Table of Content**
- [Lecture 02: Python Crash Course (p2)](#lecture-02-python-crash-course-p2)
  - [Topics](#topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 02: Python Crash Course (p2)

## Topics
We will continue with the Python language basics in our class, here are the topics
* [x] Primitive data types
  * [x] Numbers
  * [x] Strings
  * [x] Boolean
* [x] Non-primitive data types
  * [x] List
  * [x] Tuple
  * [x] Set
  * [x] Dictionary
* ~~[ ] Control flows~~ (didn't get time to cover)
  * ~~[ ] Conditional statements~~
  * ~~[ ] Loops~~

## Concepts
* Common arithmetic oeprations with numbers
  | Operation | Result                           |
  | --------- | -------------------------------- |
  | x + y     | sum of x and y                   |
  | x - y     | difference of x and y            |
  | x * y     | product of x and y               |
  | x / y     | quotient of x and y              |
  | x // y    | floored quotient of x and y      |
  | x % y     | remainder of x / y               |
  | -x        | x negated                        |
  | +x        | x unchanged                      |
  | abs(x)    | absolute value or magnitude of x |
  | pow(x, y) | x to the power y                 |
  | x ** y    | x to the power y                 |
* With `string` data, you could
  * Check the length of a string with `len()`
  * `+` and `*` operators
  * Change the cases with `str.lower()` and `str.upper()`
  * Replace part of the string with `str.replace()`
  * Check if a substring is a part of a given string with the `in` operator
  * String indexing
    * Each character of the string is assigned a index number representing its position in the string, and index number starts from 0
    * General indexing format - `StringValue[<lower_index>:<upper_index>]`
      * `<lower_index>` is inclusive
      * `<upper_index>` is exclusive
      * Negative indexing
* `Reference` vs. `Copy` (see details in the code sample in [./notebook/code_demo.ipynb](./notebook/code_demo.ipynb))
* `Set` operations
  | Operation            | Python Code                            |
  | -------------------- | -------------------------------------- |
  | union                | `A \| B` or `A.union(B)`               |
  | intersect            | `A & B` or `A.intersection(B)`         |
  | difference           | `A - B` or `A.difference(B)`           |
  | symmetric difference | `A ^ B` or `A.symmetric_difference(B)` |


## Course materials
* slides [[link](https://docs.google.com/presentation/d/1MtZjQIogqJ5UZQ9jz4DkItPFH_b0XlTxbfzPgU207AQ/edit?usp=sharing)]

# Suggested reading
* [If available] Chapter 1-3 of **Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter** (3rd Edition by Wes McKinney)
  * Released August 2022
  * Publisher(s): O'Reilly Media, Inc.
  * ISBN: 9781098104030
* `list` [[link](https://www.geeksforgeeks.org/python-lists/)]
* Blog post about the non-primitive data types covered in our class [[link](https://www.geeksforgeeks.org/python-tuples/)]
* Differences and Applications of List, Tuple, Set and Dictionary in Python [[link](https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/)]
* `Shallow` & `Deep` Copy
  * [Blog #1](https://towardsdatascience.com/assignment-shallow-or-deep-a-story-about-pythons-memory-management-b8fad87bfa6c)
  * [Blog #2](https://www.programiz.com/python-programming/shallow-deep-copy)
