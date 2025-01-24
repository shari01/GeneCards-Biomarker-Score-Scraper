# Web Scraping Gene Data from GeneCards for Biomarkers and Scores

This repository contains a Python script that automates the process of scraping gene-related data from GeneCards for a predefined list of biomarkers. The script uses Selenium WebDriver to search GeneCards for each biomarker, extract gene symbols and their associated scores, and save the results in a CSV file for further analysis.

## Features

- **Web Scraping**: Uses Selenium to navigate GeneCards and extract relevant gene data.
- **Data Extraction**: For each biomarker, the script scrapes gene symbols and associated scores, only extracting data for matching biomarkers.
- **Automation**: Automatically iterates over a list of biomarkers, processes each one in a fresh browser session, and handles any potential errors gracefully.
- **Data Saving**: The results are stored in a CSV file, which can be easily downloaded and used for further research or analysis.

## How It Works

1. A list of biomarker names is provided.
2. For each biomarker, the script searches for it on the GeneCards website.
3. The script extracts gene symbols and scores for the corresponding biomarker.
4. It handles page loading with an automatic wait to ensure that the data is fully loaded.
5. The extracted data is saved into a CSV file for easy access.

## Dependencies

- Selenium WebDriver
- ChromeDriver
- Pandas
- Time

## Installation

1. Install the required dependencies:
    ```bash
    pip install selenium pandas
    ```

## Usage

- Simply run the Python script to scrape gene data for the list of biomarkers:
    ```bash
    python scrape_genecards.py
    ```

- The results will be saved in `biomarkers_scores.csv` in the specified directory.

Feel free to contribute to this project by suggesting improvements, reporting issues, or submitting pull requests!

## License

This project is licensed under the MIT License.
