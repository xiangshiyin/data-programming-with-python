**Table of Content**
- [Lecture 05: Pandas and Data Frame](#lecture-05-pandas-and-data-frame)
  - [Topics](#topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 05: Pandas and Data Frame

## Topics
Here are the topics we are going to cover
* [ ] Python basics (extended topic)
  * [ ] Class and objects
  * [ ] Files and I/O


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

## Course materials
* slides [[link](TBD)]

# Suggested reading
* [If available] Chapter 5 of **Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter** (3rd Edition by Wes McKinney)
* Online resources
  * Intro to `pandas` [[link](https://pandas.pydata.org/docs/getting_started/index.html#intro-to-pandas)]
  * `pandas` user guide [[link](https://pandas.pydata.org/docs/user_guide/index.html)]
  * 10 mins to `pandas` [[link](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#)]
  * Time series data in `pandas` [[link](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#time-series)]