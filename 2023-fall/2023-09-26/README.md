
**Table of Content**
- [Lecture 06: Pandas Data Table Practice](#lecture-06-pandas-data-table-practice)
  - [Topics](#topics)
  - [Concepts](#concepts)
    - [What represents missing/null value in `pandas`](#what-represents-missingnull-value-in-pandas)
    - [The SQL joins](#the-sql-joins)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 06: Pandas Data Table Practice

## Topics
Here are the topics we are going to cover
* [ ] Pandas basic operation
* [ ] Hands-on practice on common `dataframe` operations


## Concepts
### What represents missing/null value in `pandas`
  * When viewing a dataframe/series with missing value, these are the common markers indicating missing/null values
    * `NaN`
    * `None`
    * `NaT`
  * In terms of the actual values, here are the common markers
    * `np.nan` - the primary marker used to represent missing values in pandas. It is a special floating-point value that can be used for numerical and non-numerical data types. You can use pandas methods like `isna()`, `isnull()`, `fillna()`, and others to work with `np.nan` values.
    * `None` - the built-in Python None type
    * Custom missing value markers - depends on the actual data you have
      * Could be empty string
      * Could be intuitive string values of `N/A`, `NULL`, etc.
  * In `pd.read_csv()` and `pd.read_excel()`, you could use the `na_values` parameter to tell pandas what should be treated as missing/null values
    * [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
    * [`read_excel()`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)

### The SQL joins
* Reference: https://www.w3schools.com/sql/sql_join.asp
* The visual representation ![](./pics/joins.jpg)


## Course materials
* slides [[link](TBD)]

# Suggested reading
* [If available] Chapter 7-8 of **Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter** (3rd Edition by Wes McKinney)
* Online resources
  * Merge, join, concatenate and compare in `dataframe` [[link](https://pandas.pydata.org/docs/user_guide/merging.html)]
  * IO tools available in `pandas` to deal with the processing of different file types [[link](https://pandas.pydata.org/docs/user_guide/io.html#io-tools-text-csv-hdf5)]
  * Work with `time series` data in `pandas` [[link](https://pandas.pydata.org/docs/user_guide/timeseries.html)]
  * Work with missing data [[link](https://pandas.pydata.org/docs/user_guide/missing_data.html)]
