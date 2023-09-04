**Table of Content**
- [Lecture 03: Python Crash Course (p3)](#lecture-03-python-crash-course-p3)
  - [Topics](#topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 03: Python Crash Course (p3)

## Topics
We will continue with the Python language basics in our class, here are the topics
* [ ] Control flows
  * [ ] Conditional statements
  * [ ] Loops
    * [ ] `while` loop
    * [ ] `for` loop
    * [ ] List comprehension
    * [ ] Iterate through different Python data types
* [ ] Indentations in Python
* [ ] Functions
  * [ ] Create a function in Python
  * [ ] Use a function in Python
  * [ ] Common built-in functions in Python
* [ ] Class and objects
* [ ] Files and I/O
* [ ] Hands-on practices

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

## Course materials
* slides [[link](https://docs.google.com/presentation/d/15pB4adripXMd1-PTQyZObfxlD2-ablKSpDUrfIiKPFQ/edit?usp=sharing)]

# Suggested reading
* [If available] Chapter 3 of **Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter** (3rd Edition by Wes McKinney)
  * Released August 2022
  * Publisher(s): O'Reilly Media, Inc.
  * ISBN: 9781098104030
