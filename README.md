# Web Scraping Assignment: Scraping Hospital and Doctor Data from airomedical.com

## Objective:
The objective of this project was to scrape data about hospitals and doctors from the website [airomedical.com](https://airomedical.com/hospitals) using Python, and store the scraped data in CSV files.

## Tasks Completed:
1. Utilized Python for web scraping.
2. Scraped the following details for each hospital:
   - Hospital Name
   - Address
   - About the hospital
3. Scraped the following details for each doctor:
   - Doctor Name
   - About
4. Stored the scraped data in separate CSV files with appropriate headers.
5. Handled errors and exceptions that occurred during scraping.
6. Ensured that the extracted data is stored in a well-organized format in the CSV files.

## Approach:
1. **Scraping Hospital Data:**
   - Identified the HTML elements containing the required information such as hospital name, address, and about section.
   - Used the BeautifulSoup library to parse the HTML and extract the relevant data.
   - Handled any errors that occurred during the scraping process.

2. **Scraping Doctor Data:**
   - Similarly, identified the HTML elements containing the required information for doctors.
   - Extracted the doctor's name and about section using BeautifulSoup.
   - Ensured error handling to deal with any issues encountered during scraping.

3. **Storing Data in CSV Files:**
   - Utilized the CSV module in Python to write the scraped data to CSV files.
   - Ensured that the CSV files have appropriate headers and are well-organized.

## File Structure:
- `web_scraping_airomedical.py`: Python script containing the web scraping code.
- `hospital_data.csv`: CSV file containing data scraped from hospital pages.
- `doctor_data.csv`: CSV file containing data scraped from doctor pages.

## Usage:
1. Clone the repository to your local machine.
2. Run the `web_scraping_airomedical.py` script to scrape data from airomedical.com.
3. Check the generated CSV files (`hospital_data.csv` and `doctor_data.csv`) for the scraped data.

## Dependencies:
- Python 3.x
- BeautifulSoup library
- requests library
- csv module

## Author:
SHIVAM RISHINARAYAN SINGH

