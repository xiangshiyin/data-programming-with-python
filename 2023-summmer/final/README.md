# Welcome to the Final Project of MSA8010!

## Final Project Requirement
* Who
    * Team of up to 2 students [[groups](https://docs.google.com/spreadsheets/d/14h3mP0HyN61y7EVzSoOL1G89wi6DEH-tSpAMkMh9Mtk/edit#gid=0)]
* What
    * **Solve a data analytics problem with the Python tools and programming**
        * Any dataset that you think is interesting to analyze
        * Datasets from your domain (Actuarial Science, Statistics, etc.) are highly welcome
    * Suggested operations
        * Define the problem to solve, or the question to answer
        * Data ingestion
        * Data cleaning/transformation
        * Explore the data
        * Detect the patterns in the data with descriptive statistics and visualization
        * Extract insights from the data, answer your original question
    * Advanced operations (Good to Have)
        * `Use machine learning models to help answer the original question`
        * `Dashboard report on the data analysis`: you could try the following tools to build a dashboard to present the data analysis work
            * Tableau
            * Plotly
                * Documentation: https://plotly.com/python/
                * Tutorial: https://plotly.com/python/getting-started/
            * Bokeh
                * Documentation: https://docs.bokeh.org/en/latest/index.html
                * Tutorial: https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb
            * Streamlit
                * Documentation: https://docs.streamlit.io/en/stable/
* When
    * `2023-07-03`: Release a list of suggested project topics
    * `2023-07-10`: Finalize project topics
    * **`2023-07-24`: Final project presentation**
        * **Each team will have 10 minutes to present their results and 2 minutes to answer questions.**
    * **`2023-07-27`: Submit project report and source code**
    * **Each team member’s contribution needs to be specified**
        * **Team members who don't have contributions listed will not get credit from the final project**
    * **Each team member will be graded based on the team’s overall project quality if they have a contribution listed in the final project.**
* Required Submissions (**DUE TIME: 23:59PM @ 2023-07-27 EST**)
    * Source Code (`Python`)
        * Jupyter Notebok file containing all the source code and testing results you used in your data analysis and modeling
    * PowerPoint presentation slides (or any format you presented in the final presentation)
    * A brief report on the project
        * Background information of the project/dataset/ideas (**Required**)
        * Illustration on the methodologies and findings from the data analysis (**Required**)
        * Each team member's contribution on the project (**Required**)

## Suggested Topics (check attachment for relevant data and info)

### Project 01. US real estate market trend
* The US real estate market has shown some interesting trends since Covid hit in early 2020. Find some open source datasets and apply some data analysis, see if you can find any interesting insights in pricing, inventories, listing ages, geo-locations, etc. You can either analyze the whole US market or pick several metro areas (such as the metro Atlanta area) for your analysis.
* Suggested data source: 
  * Open source dataset from Redfin [[link](https://www.redfin.com/news/data-center/)]
* Feel free to explore and use other open source datasets if you like

### Project 02: US job market trend
* Take a look at the open sourced dataset on employment and job openings from the [US bureau of labor statistics](https://www.bls.gov/data/) and see if you can find any interesting trends, such as
  * The overall trend in earnings in the past 3 years since Covid hit, are there any differences across different industry sectors?
  * What kind of job is getting the most increase in earning in the past 3 years?
  * What kind of job is getting the most demand in the past 3 years?
* Feel free to explore and use other open source datasets if you like

### Project 03: Crime report data from the Atlanta Police Department
* Utilize the open source dataset shared by the Atlanta Police Department, see if you can find any interesting patterns in crime cases, such as region, time, crime type, etc. The dataset also contains latitude/longitude information, so there is also a chance to create some awesome visualizations on geo-locations!
* Data source: https://opendata.atlantapd.org/

### Project 04: Air quality data from OpenAQ
* Analyze the air quality data from OpenAQ and air pollution trend over time and by countries/regions
* Data source:
  * The recommended way to get the air quality data is via the official API, with which you could fetch data by location, time frame, and parameters. Official doc on the API can be found [here](https://docs.openaq.org/docs/getting-started). This might be a little challenging since you need to figure out the appropriate way to fetch the data from the API following the [official documentation](https://docs.openaq.org/docs/getting-started)
  * If you have a google/gmail account, you could also sign up for free google cloud access and get a sample data from OpenAQ in the bigquery table `bigquery-public-data.openaq.global_air_quality` under the `bigquery-public-data` catalog. This could also be challenging since you would need to figure out a way to let Python script talk to BigQuery on Google Cloud and submit queries in order to fetch the dataset you need.

### Project 05: Soccer player dataset analysis
* Analyze the FIFA23 data 
  * see if you could find any attributes that are strongly impacting the players' potential and value
  * See if you could build a model to predict players' market value or potential
  * See if there is any common features among the top 50 players in market value
* Data source:
  * Official FIFA players dataset hosted on Kaggle [[link](https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database)]


### Other Data Sources
* `Google Data Search`: https://datasetsearch.research.google.com/
* `Kaggle`: https://www.kaggle.com/
