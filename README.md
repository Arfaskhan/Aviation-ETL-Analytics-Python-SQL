# Aviation-ETL-Analytics-Python-SQL
Real-Time Flight Data Pipeline using AviationStack API and MySQL.

# Overview
This project demonstrates an end-to-end **ETL pipeline** using data from the **AviationStack API**. The pipeline:
- Extracts real-time flight data from the API
- Transforms and cleans the data (null handling, data types)
- Loads it into a MySQL database
- Performs analytical queries to generate real-world business insights

# Tech stack:
- Python (Requests, Pandas, PyMySQL)
- SQL (MySQL)
- Jupyter Notebook
- AviationStack API (Free tier)

# Folder Structure
- notebooks/ – Jupyter notebook with code walkthrough
- scripts/ – Reusable Python ETL scrip
- screenshots/ - 

# Use cases
1	Flights delayed more than 15 minutes
2	Flights operated by Emirates
3	Count of flights per airline
4	Flights on a specific date (e.g., July 3)
5	Top 5 busiest departure airports
6	Most common arrival airport
7	Flights with unknown status
8	Earliest flight each day
9	Flights missing arrival airport
10	Total flights per day
11	Calculate travel time between airports
12	Flights on July 3 using MONTH() and DAY()
13	Last flight of the day with airline name
