#  NBA Season Stats Scraper (ETL Pipeline)

An automated web scraping tool built with Python that navigates the official NBA website, extracts the current season's top 5 performing players across 9 different statistical categories, and formats the data into a clean, analysis-ready CSV file.

##  Tech Stack
* **Python 3**
* **Selenium:** Used for automated browser navigation, handling dynamic pop-ups, and extracting raw HTML data.
* **Pandas:** Used to transform the raw arrays into a structured DataFrame and export to CSV.

##  How It Works (The ETL Process)
1. **Extract:** The script initializes a Chrome WebDriver, navigates to `nba.com/stats`, and uses explicit waits to bypass cookie consent banners. It then locates the "Season Leaders" tables using targeted CSS selectors and extracts the raw text.
2. **Transform:** The raw data is isolated into three distinct lists (Categories, Names, and Values). The categories are programmatically expanded using list comprehensions to achieve a perfect 1-to-5 relational mapping.
3. **Load:** The synchronized lists are compiled into a Pandas dictionary, converted into a DataFrame, and exported as a clean `nba_players_season_state.csv` without index numbers.

##  Sample Output
The final dataset is perfectly structured for database ingestion or exploratory data analysis (EDA).

| Category | Value | Name | Rank |
| :--- | :--- | :--- | :--- |
| POINTS PER GAME | 32.7 | Luka Dončić | 1 |
| POINTS PER GAME | 31.9 | Shai Gilgeous-Alexander | 2 |
| REBOUNDS PER GAME | 12.6 | Nikola Jokić | 1 |
| REBOUNDS PER GAME | 11.7 | Karl-Anthony Towns | 2 |

##  How to Run Locally
1. Clone this repository.
2. Ensure you have Google Chrome installed.
3. Install the required libraries:
   `pip install selenium pandas`
4. Run the script:
   `python main.py`
