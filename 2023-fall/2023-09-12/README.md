**Table of Content**
- [Lecture 04: Python Basic Wrapup and Numpy (p3)](#lecture-04-python-basic-wrapup-and-numpy-p3)
  - [Topics](#topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 04: Python Basic Wrapup and Numpy (p3)

## Topics
Here are the topics we are going to cover
* [x] Python basics wrapup
  * [x] Control flows
      * [x] Iterate through different Python data types
      * [x] List comprehension (exploration topic)
  * [x] Functions
    * [x] Different forms of function definition and calling
    * [x] Common built-in functions in Python (exploration topic, will cover later)
  * ~~[ ] Class and objects~~ (skipped)
  * ~~[ ] Files and I/O~~ (skipped)
* [x] Numpy and Linear Algebra
  * Numpy Array Indexing
  * Numpy Array Operations
  * Linear Algebra with Numpy

## Concepts
* `Indentation` in Python
  * The Python language design is distinguished by its emphasis on readability, simplicity, and explicitness. Some people go so far as to liken it to "executable pseudocode"
  * Python uses whitespace (tabs or spaces) to structure code instead of using braces as in many other languages like R, C++, Java, and Perl. Consider a for loop from a sorting algorithm, such as:
      ```python
      if x >= 5:
          print(f"x is greater or equal to 5")
      else:
          print(f"x is smaller than 5")
      ```
  * A colon denotes the start of an indented code block after which all of the code must be indented by the **same amount** until the end of the block
  * `Indentation` here means - **X consecutive spaces**
    * There is no restrictions on the amount of spaces to use as long as you always stick to the same amount. However, **4 consecutive spaces** is the general standard people follow
    * Many text editors have a setting that will replace tab stops with spaces automatically
  * Semicolons can be used, however, to separate multiple statements on a single line:
      ```python
      a = 5; b = 6; c = 7
      ```
    * Putting multiple statements on one line is generally discouraged in Python as it can make code less readable.
* `function` 
  * Definition pattern
    ```python
    def function_name(param1, param2, ..., paramN):
        <function logic with appropriate indentations>
        <return statement>
    ```
  * Call pattern 
    ```python
    function_name(param1_value, param2_value, ..., paramN_value)
    ```
    or
    ```python
    function_name(
      param1 = param1_value, 
      param2 = param2_value, 
      ..., 
      paramN = paramN_value
    )
    ```
    * In case you want to reuse the returned value from a function, you could assign it to a variable, such as 
    ```python
    variable_a = function_name(param1_value, param2_value, ..., paramN_value)
    ```
* ~~`Object` vs. `Class` - Example: Describe a table~~ (skipped)
  * How do you describe a table?
  ```mermaid
  classDiagram
      class table_1
      table_1: l = 1
      table_1: w = 2
      table_1: h = 3
      table_1: Has a flat top
      table_1: Can hold weight
  ```

  * How about 2 tables?
  ```mermaid
  classDiagram
      class table_1
      table_1: l = 1
      table_1: w = 2
      table_1: h = 3
      table_1: Has a flat top
      table_1: Can hold weight

      class table_2
      table_2: l = 2
      table_2: w = 3
      table_2: h = 4    
      table_2: Has a flat top
      table_2: Can hold weight
  ```

  * How about many tables?
  ```mermaid
  classDiagram
      class table_1
      table_1: l = 1
      table_1: w = 2
      table_1: h = 3
      table_1: Has a flat top
      table_1: Can hold weight

      class table_2
      table_2: l = 2
      table_2: w = 3
      table_2: h = 4
      table_2: Has a flat top
      table_2: Can hold weight

      class table_N
      table_N: l = N
      table_N: w = N+1
      table_N: h = N+2    
      table_N: Has a flat top
      table_N: Can hold weight
  ```

  * How do you describe the concept `table` to an audience who doesn't know what a table is?
  ```mermaid
  classDiagram
      class table_1
      table_1: l = 1
      table_1: w = 2
      table_1: h = 3
      table_1: Has a flat top
      table_1: Can hold weight

      class table_2
      table_2: l = 2
      table_2: w = 3
      table_2: h = 4
      table_2: Has a flat top
      table_2: Can hold weight

      class table_N
      table_N: l = N
      table_N: w = N+1
      table_N: h = N+2    
      table_N: Has a flat top
      table_N: Can hold weight

      class table
      table: int l
      table: int w
      table: int h
      table: boolean has_a_flat_top
      table: hold_weight()

      table_1 --> table
      table_2 --> table
      table_N --> table
  ```
  * Do you see what happened here?
    * We created a **class** `table` to represent a group of **objects** - tables
    * All table **objects** of the **class** `table` share some common **properties** and **functions**
    * Different **objects** might have different values for the same **attribute**

## Course materials
* slides [[link](https://docs.google.com/presentation/d/1jAWipDh-pWC9fwWJUXanqwU7RUOeYEg29_Rkp6bZldU/edit?usp=sharing)]

# Suggested reading
* [If available] Chapter 4 of **Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter** (3rd Edition by Wes McKinney)
  * Released August 2022
  * Publisher(s): O'Reilly Media, Inc.
  * ISBN: 9781098104030
* Online resources
  * `list comprehension` [[reference](https://www.w3schools.com/python/python_lists_comprehension.asp)]
  * Python built-in functions 
    * [official doc](https://docs.python.org/3/library/functions.html)
    * [Online reference](https://www.w3schools.com/python/python_ref_functions.asp)
  * Numpy quickstart [[link](https://numpy.org/doc/stable/user/quickstart.html)]
  * Numpy: the absolute basics for beginners [[link](https://numpy.org/doc/stable/user/absolute_beginners.html)]