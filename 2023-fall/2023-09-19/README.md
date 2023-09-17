**Table of Content**
- [Lecture 05: Pandas and DataFrame](#lecture-05-pandas-and-dataframe)
  - [Topics](#topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 05: Pandas and DataFrame

## Topics
Here are the topics we are going to cover
* [ ] Python basics (extended topic)
  * [ ] Class and objects
  * [ ] Files and I/O
* [ ] `pandas` and `dataframe`
  * [ ] Create a `pandas` dataframe (from hard-coded information, csv, excel spreadsheet, etc.)
  * [ ] Manipulate a `pandas` dataframe


## Concepts
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
  * With a blueprint of **class**, we could create an **object** or an instance out of it, which people normally call *instantiating a class*.
* File I/O
  * Major tool/function: `open(file, mode)` (https://docs.python.org/3/library/functions.html#open)
  * The default mode is `'r'` (open for reading text, synonym of `'rt'`). The available modes:
    | Character | Meaning                                                         |
    | --------- | --------------------------------------------------------------- |
    | 'r'       | open for reading (default)                                      |
    | 'w'       | open for writing, truncating the file first                     |
    | 'x'       | open for exclusive creation, failing if the file already exists |
    | 'a'       | open for writing, appending to the end of the file if it exists |
    | 'b'       | binary mode                                                     |
    | 't'       | text mode (default)                                             |
    | '+'       | open for updating (reading and writing)                         |
* `pandas` - the library
  * It contains data structures and data manipulation tools designed to make data cleaning and analysis fast and convenient in Python.
  * `pandas` adopts significant parts of NumPy’s idiomatic style of array-based computing, especially array-based functions and a preference for data processing without for loops.
* 

## Course materials
* slides [[link](TBD)]

# Suggested reading
* [If available] Chapter 5 of **Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter** (3rd Edition by Wes McKinney)
* Online resources
  * Intro to `pandas` [[link](https://pandas.pydata.org/docs/getting_started/index.html#intro-to-pandas)]
  * `pandas` user guide [[link](https://pandas.pydata.org/docs/user_guide/index.html)]
  * 10 mins to `pandas` [[link](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#)]
  * Time series data in `pandas` [[link](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#time-series)]
  * `Merge` and `Join` in `pandas` [[link](https://pandas.pydata.org/docs/user_guide/merging.html)]