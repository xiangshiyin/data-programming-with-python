**Table of Content**
- [Lecture 03: Python Crash Course (p3)](#lecture-03-python-crash-course-p3)
  - [Topics](#topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 03: Python Crash Course (p3)

## Topics
We will continue with the Python language basics in our class, here are the topics
* [x] Control flows
  * [x] Conditional statements
  * [x] Loops
    * [x] `while` loop
    * [x] `for` loop
    * [ ] List comprehension
    * [ ] Iterate through different Python data types
* [x] Indentations in Python
* [x] Functions
  * [x] Create a function in Python
  * [x] Use a function in Python
  * [ ] Common built-in functions in Python
* [ ] Class and objects
* [ ] Files and I/O
* [x] Hands-on practices

## Concepts
* Similarities between `set` and `dictionary`
  * Both are unordered collection
  * Both are mutable
  * Both have uniquess property (using the `hasing` mechanism)
  * Both are iterable
* `Conditions` in Python
  * The program will evaluate the boolean value of the expression to decide which statement to execute
  * The general code pattern looks like this:


      ```python
      if <exp>:
          <statement>
      elif <exp>:
          <statement>
      else:
          <statement>
      ```

  * The `<exp>` is generally an expression returnning a boolean value of `True/False`, common patterns include
    * `<variable/expression> == True` or `<variable/expression>` (equals to True) or `<variable/expression> != False`
    * `<variable/expression> == False` or `not <variable/expression>` (equals to False) or `<variable/expression> != True`
    * `<variable/expression> != None` or `<variable/expression>`
    * `<variable/expression> == None` or `not <variable/expression>` 
    * `variable_a` > `variable_b` (comparison operator could be `>`, `<`, `==`, `!=`, `>=`, `<=`)
  * You need to indent each line of the `<statement>` code block by the **same number of whitespace**. It is a required practice to indicate what block of code a statement belongs to. **Default indentation uses 4 spaces. You could use any number that works to you, but a minimum of 1 space has to be used.**
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
* To build a looping logic, you need a condition that could
  * Get your code into repeated iterations
  * Change over iterations such that you have a chance to jump out of the loop
* `while` loop vs. `for` loop - instead of controling the loop via a "*conditio*n", we can control the loop via a precise "*counter*"
    ```mermaid
    ---
    title: while loop
    ---
    stateDiagram-v2
        Condition_check: If condition == True
        Plan_A: Plan A
        Plan_B: Plan B
        [*] --> Condition_check
        Condition_check --> Plan_A: True/Yes
        Plan_A --> Condition_check
        Condition_check --> Plan_B: False/No
    ```

    ```mermaid
    ---
    title: for loop
    ---
    stateDiagram-v2
        Condition_check: Is this the "last iteration"
        Plan_A: Plan A
        Plan_B: Plan B
        [*] --> Condition_check
        Condition_check --> Plan_A: True/Yes
        Plan_A --> Condition_check
        Condition_check --> Plan_B: False/No
    ```
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
* `Object` vs. `Class` - Example: Describe a table
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
* slides [[link](https://docs.google.com/presentation/d/15pB4adripXMd1-PTQyZObfxlD2-ablKSpDUrfIiKPFQ/edit?usp=sharing)]

# Suggested reading
* [If available] Chapter 3 of **Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter** (3rd Edition by Wes McKinney)
  * Released August 2022
  * Publisher(s): O'Reilly Media, Inc.
  * ISBN: 9781098104030
* Online resources
  * `loops` in Python [[link](https://www.geeksforgeeks.org/loops-in-python/)]
  * `function` in Python [[link](https://www.w3schools.com/python/python_functions.asp)]
  * File operations in Python [[link](https://www.programiz.com/python-programming/file-operation)]
  * Common Python libraries [[link](https://learnpython.com/blog/python-libraries-for-beginners/)]
