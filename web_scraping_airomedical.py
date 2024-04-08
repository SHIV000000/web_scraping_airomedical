import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape hospital data
def scrape_hospitals(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')
        hospitals = []
        for hospital_div in soup.find_all('div', class_='HospitalCard_container__sjVZU'):
            hospital_name = hospital_div.find('h2', class_='HospitalCard_name__UZRIa').text.strip()
            address_element = hospital_div.find('div', class_='HospitalCard_address__1rF_M')
            address = address_element.text.strip() if address_element else "Address not available"
            about_element = hospital_div.find('div', class_='HospitalCard_description__WdCpb')
            about = about_element.text.strip() if about_element else "About not available"
            hospitals.append({
                'Hospital Name': hospital_name,
                'Address': address,
                'About': about
            })
        print("Hospitals Data:", hospitals)  
        return hospitals
    except requests.exceptions.RequestException as e:
        print("Failed to fetch hospital data:", e)
        return None

# Function to scrape doctor data
def scrape_doctors(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')
        doctors = []
        for doctor_div in soup.find_all('div', class_='DoctorCard_container__XQSpd'):
            doctor_name = doctor_div.find('h2', class_='DoctorCard_name__05xCl').text.strip()
            about_element = doctor_div.find('div', class_='DoctorCard_about__1jjEc')
            about = about_element.text.strip() if about_element else "About not available"
            doctors.append({
                'Doctor Name': doctor_name,
                'About': about
            })
        print("Doctors Data:", doctors)  
        return doctors
    except requests.exceptions.RequestException as e:
        print("Failed to fetch doctor data:", e)
        return None

# Main function
if __name__ == "__main__":
    hospitals_url = "https://airomedical.com/hospitals"  
    doctors_url = "https://airomedical.com/doctors"  

    # Scraping hospital data
    hospitals_data = scrape_hospitals(hospitals_url)

    # Scraping doctor data
    doctors_data = scrape_doctors(doctors_url)

    if hospitals_data is not None and doctors_data is not None:
        try:
            # Writing hospital data to CSV
            with open('hospital_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Hospital Name', 'Address', 'About']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for hospital in hospitals_data:
                    writer.writerow(hospital)

            # Writing doctor data to CSV
            with open('doctor_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Doctor Name', 'About']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for doctor in doctors_data:
                    writer.writerow(doctor)

            print("Scraping and CSV creation completed successfully.")
        except Exception as e:
            print("Failed to write data to CSV:", e)
    else:
        print("Failed to scrape data.")
