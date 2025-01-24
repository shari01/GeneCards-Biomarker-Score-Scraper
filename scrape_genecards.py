from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


# Initialize the WebDriver (make sure to specify the path to your WebDriver if not in PATH)
def scrape_scores(driver, biomarker):
    url = f"https://www.genecards.org/Search/Keyword?queryString={biomarker}"
    driver.get(url)
   
    # Automatically wait for 5 seconds for CAPTCHA solving or page load
    print(f"Waiting for 5 seconds for {biomarker} page to load...")
    time.sleep(5)  # Adjust this delay if needed, or you can set a longer wait if CAPTCHA solving takes more time
   
    scores = []
    genes = []
   
    # Find rows in the search result table
    rows = driver.find_elements(By.CSS_SELECTOR, "#searchResults tbody tr")
   
    # Iterate over search results and extract gene symbol and score
    for row in rows:
        gene_symbol = row.find_element(By.CSS_SELECTOR, "td.gc-gene-symbol a").text
       
        # Only extract the score if the gene symbol matches the searched biomarker
        if gene_symbol.lower() == biomarker.lower():
            score = row.find_element(By.CSS_SELECTOR, "td.score-col").text
            genes.append(gene_symbol)
            scores.append(score)
   
    return genes, scores


# List of biomarkers to scrape
biomarkers = [
    'tp53', 'WRAP53', 'MDM2', 'RRM2B', 'ATP2B3', 'BMP5', 'BTG2', 'CEBPA', 'CHD1', 'CYSLTR2',
    'DCAF12L2', 'DEPDC1', 'ERBB4', 'FANCF', 'FBLL1', 'FES', 'FOS', 'FOXD3', 'FOXL2', 'FSTL3',
    'HLA-B', 'IGF2', 'IGF2BP2', 'IL1B', 'LCP1', 'LYVE1', 'MIR181D', 'MUC5B', 'MUC6', 'NR4A3',
    'OR11A1', 'OR11H4', 'OR2C1', 'OR2M7', 'OR6A2', 'OR7D4', 'OR8B12', 'PGR', 'POU5F1',
    'PRDM16', 'PTENP1', 'PTGS2', 'PTX3', 'ROBO3', 'RUNX1T1', 'SCGB1D4', 'SIM2', 'SIX1', 'TERC',
    'TFF3', 'TNFAIP3', 'TRH', 'UHRF1', 'UNC5D', 'VAV1'
]
all_results = pd.DataFrame()


# Loop through each biomarker, restarting WebDriver for each one to reset session
for biomarker in biomarkers:
    # Initialize a new WebDriver instance for each biomarker
    driver = webdriver.Chrome()  # You can specify the path if necessary, e.g., executable_path='path/to/chromedriver'
   
    try:
        # Scrape the gene and score data for the current biomarker
        genes, scores = scrape_scores(driver, biomarker)
       
        # Only add results if there is data for the biomarker
        if genes and scores:
            temp_df = pd.DataFrame({'Gene': genes, 'Score': scores, 'Biomarker': biomarker})
            all_results = pd.concat([all_results, temp_df], ignore_index=True)
   
    except Exception as e:
        print(f"An error occurred for {biomarker}: {e}")
   
    finally:
        # Close the browser after scraping each biomarker
        driver.quit()


# Save all results to a CSV file after processing all biomarkers
all_results.to_csv('C:/Users/Sheryar Malik/Downloads/cgc/genecrd/biomarkers_scores.csv', index=False)



