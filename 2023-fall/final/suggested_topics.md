# Suggested Topics

## Project 01: Crime report data from the Atlanta Police Department
* **Idea**: Utilize the open source dataset shared by the Atlanta Police Department, see if you can find any interesting patterns in crime cases, such as region, time, crime type, etc. The dataset also contains latitude/longitude information, so there is also a chance to create some awesome visualizations on geo-locations!
  * If you looking at visualizations on satellite maps, `folium` might be an option to look into (https://github.com/python-visualization/folium)
  * Commercial softwares such as Tableau, Power BI, Looker Studio, etc. all provide powerful visualization functionalities
* Data source: https://opendata.atlantapd.org/

## Project 02: Soccer player dataset analysis
* **Idea**: Analyze the FIFA23 data 
  * See if you could find any attributes that are strongly impacting the players' potential and value
  * See if you could build a model to predict players' market value or potential
  * See if there is any common features among the top 50 players in market value
* Data source:
  * Official FIFA players dataset hosted on Kaggle [[link](https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database)]

## Project 03: Build a ChatBot with OpenAI's Python API
* **Idea**: Build a program on top of OpenAI's Python APIs of their GPT models to help answer questions on a given or any document
  * Example: Build a program to answer questions about the book "Harry Potter and the Sorcerer's Stone", such as summarizing the book
  * **Some more ideas**:
    * Copy the document into a text file (such as a `*.txt` file)
    * Use the OpenAI python API to 
      * Tokenize the file, break the whole document into paragraphs
      * Generate text embeddings (vector representation of a text string) of each paragraph of the original document
      * Calculate the embeddings (vector) of the input question, such as "What happened when Harry first meet with Hagrid?"
      * Find out the top 10 paragraphs that are most relevant to the input questions (by calculating the cosine similarities between the input question embedding and the corresponding paragraph embedding)
      * Answer the question based on the top 10 paragraphs selected
* **Resources**: 
  * OpenAI provides many pre-built Python API, packages, and examples to help make application building quick and easy. Here are some good readings
    * Official documents: https://platform.openai.com/overview
    * Cookbook with code examples: https://github.com/openai/openai-cookbook/tree/main

## Project 04: Analyze the Wikipedia pageview data
* **Idea**: Analyze the historical trending of the pageview traffic on a set of given wikipedia pages and see if you could find any interesting pattern
  * Example: Pull the historical stock price of Tesla and the historical pageview traffics on the tesla company wikipedia page and see if there are any interesting correlations.
* **Resources**:
  * Wikipedia provides open source APIs for users to retrieve the pageview counts of any wikipedia page at any time https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews
  * Yahoo finance API [[official document](https://developer.yahoo.com/api/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAKvlJLE5QdpZeV_en5bZAkuTixtjujVMnt79-mfnSxtfXLD0P_pdatRLkaCYXs12eGWlOxHOAtOs9__-onep1-H_AVEkX3NJdMuJk2tgb74e3YcFl8Gr6k90orEX-6omaBylYfpO7tA3X9pfI8CUCFaVOrBAZ_-9K6j1mh0FxERP)]
  * Yahoo finance API application tutorial: https://algotrading101.com/learn/yahoo-finance-api-guide/

## Project 05: US job market trend
* **Idea**: Take a look at the open sourced dataset on employment and job openings from the [US bureau of labor statistics](https://www.bls.gov/data/) and see if you can find any interesting trends, such as
  * The overall trend in earnings in the past 3 years since Covid hit, are there any differences across different industry sectors?
  * What kind of job is getting the most increase in earning in the past 3 years?
  * What kind of job is getting the most demand in the past 3 years?
* Feel free to explore and use other open source datasets if you like

## Project 06: Earthquake data analysis
* **Idea**
  * Build a Python function to easily pull historical earthquake events for any input region, time, and magnitude scale. 
  * Analyze the earthquake events in the past, see if there are any interesting patterns in location and time
  * Build visualizations of earthquake events on a satellite map and find the regions where earthquakes frequently happened
* The `USGS` (United States Geological Survey) website https://www.usgs.gov/programs/earthquake-hazards/tools provides open sourced datasets on historical and recent earthquake events all around the world.

## Project 07: Oil price vs. GDP analysis
The **Organization of the Petroleum Exporting** Countries (**OPEC**, /ˈoʊpɛk/ OH-pek) is an organization enabling the co-operation of leading oil-producing countries in order to collectively influence the global oil market and maximize profit. It was founded on 14 September 1960 in Baghdad by the first five members (Iran, Iraq, Kuwait, Saudi Arabia, and Venezuela). The 13 member countries account for an estimated 30 percent of global oil production.
* **Idea**: Analyze the historical countrywise GDP data and historical crude oil price and see if there are any correlations for OPEC members
* **Resources**
  * GDP:
    * World bank data: https://data.worldbank.org/
    * IMF data: https://data.imf.org/?sk=388dfa60-1d26-4ade-b505-a05a558d9a42
    * OECD data: https://data.oecd.org/
  * Oil price:
    * EIA crude oil price: https://www.eia.gov/dnav/pet/pet_pri_spt_s1_d.htm
    * Nasdaq data link: https://data.nasdaq.com/data/ODA/POILWTI_USD-crude-oil-petroleum-west-texas-intermediate-40-api-midland-texas-us-per-barrel
    * World bank data: https://data.worldbank.org/


## Other Data Sources
* `Google Data Search`: https://datasetsearch.research.google.com/
* `Kaggle`: https://www.kaggle.com/
